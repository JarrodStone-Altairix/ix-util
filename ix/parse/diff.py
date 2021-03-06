import os
import filecmp


class Dir_Cmp_Ext:

  common_dirs = []
  common_files = []
  diff_common_files = []
  left_dirs = []
  left_files = []
  right_dirs = []
  right_files = []

  def __init__(self, left, right):
    self.left_fp = left
    self.right_fp = right
    self._diffr("", filecmp.dircmp(left, right))
    self.diff_common_files = [
        f for f in self.common_files
        if not filecmp.cmp(os.path.join(left, f),
                           os.path.join(right, f))]

  def _diffr(self, root, dc):

    self.common_dirs.extend([os.path.join(root, x) for x in dc.common_dirs])
    self.common_files.extend([os.path.join(root, x) for x in dc.common_files])

    dirs, files = _check_fp_type(dc.left, dc.left_only)
    self.left_dirs.extend(dirs)
    self.left_files.extend(files)

    dirs, files = _check_fp_type(dc.right, dc.right_only)
    self.right_dirs.extend(dirs)
    self.right_files.extend(files)

    for dir_name, dc_sub in dc.subdirs.items():
      self._diffr(os.path.join(root, dir_name), dc_sub)

  def __repr__(self):
    return (
        f"Common dirs: {os.linesep}{os.linesep.join(self.common_dirs)}"
        f"{os.linesep}{os.linesep}Common files: {os.linesep}"
        f"{os.linesep.join(self.common_files)}"
        f"{os.linesep}{os.linesep}Left directories only: {os.linesep}"
        f"{os.linesep.join(self.left_dirs)}"
        f"{os.linesep}{os.linesep}Right directories only: {os.linesep}"
        f"{os.linesep.join(self.right_dirs)}"
        f"{os.linesep}{os.linesep}Left files only: {os.linesep}"
        f"{os.linesep.join(self.left_files)}"
        f"{os.linesep}{os.linesep}Right files only: {os.linesep}"
        f"{os.linesep.join(self.right_files)}")


def _check_fp_type(root, ls):
  return (
      [f for f in ls if os.path.isdir(os.path.join(root, f))],
      [f for f in ls if os.path.isfile(os.path.join(root, f))])


def diffr(left, right):
  return Dir_Cmp_Ext(left, right)


def _prepend_dir(rootdir, dir_list):
  return [os.path.join(rootdir, d) for d in dir_list]


def _diff(dir_a, dir_b):
  report = filecmp.dircmp(dir_a, dir_b)
  left_only = report.left_only.copy()
  right_only = report.right_only.copy()
  common = report.common.copy()
  comm_dirs = report.common_dirs.copy()

  while len(comm_dirs) > 0:
    subdir = comm_dirs.pop()

    report = filecmp.dircmp(
        os.path.join(dir_a, subdir), os.path.join(dir_b, subdir))
    left_only.extend(_prepend_dir(subdir, report.left_only))
    right_only.extend(_prepend_dir(subdir, report.right_only))

    common.extend(_prepend_dir(subdir, report.common))
    comm_dirs.extend(_prepend_dir(subdir, report.common_dirs))

  # Compare common files
  comm_same = []
  comm_diff = []
  for f in common:
    f1 = os.path.join(dir_a, f)
    f2 = os.path.join(dir_b, f)
    if os.path.isfile(f1) and not filecmp.cmp(f1, f2, False):
      comm_diff.append(f)
    else:
      comm_same.append(f)

  return comm_same, comm_diff, left_only, right_only
