import os
import filecmp
from argparse import ArgumentParser


def compare_dirs_recur(dir0, dir1):

  filecmp.dircmp(dir0, dir1).report()

  for root, dirs, _, in os.walk(dir0):

    rel_root = os.path.relpath(root, dir0)
    if rel_root == '.':
      rel_root = ""

    for d in dirs:
      target_dir1 = os.path.join(dir1, rel_root, d)

      if os.path.exists(target_dir1):
        filecmp.dircmp(os.path.join(root, d), target_dir1).report()
      else:
        print(f"Differing subdirectory : {os.path.join(root, d)} "
              f"-- {target_dir1}")


def compare(fd0, fd1):
  if os.path.isdir(fd0) and os.path.isdir(fd1):
    compare_dirs_recur(fd0, fd1)
  elif os.path.isfile(fd0) and os.path.isfile(fd1):
    print(filecmp.cmp(fd0, fd1, shallow=False))
  else:
    print("descriptors did not match or were neither files nor directories")


compare(
    r"C:\Users\Jarrod\Downloads\eclipse-jarrod",
    r"C:\Users\Jarrod\Downloads\eclipse-deploy")
exit()

if __name__ == "__main__":
  parser = ArgumentParser(
      description="Diff two directories or two files")
  parser.add_argument("file_desc0", help="Path to a file or directory")
  parser.add_argument("file_desc1", help="Path to a file or directory")

  args = parser.parse_args()
  compare(args.file_desc0, args.file_desc1)
