from threading import Thread
import git
from config.git import Config as Cfg
import ix.const as const

adf_repo = git.Repo(Cfg.ADF_REPO)
bx_repo = git.Repo(Cfg.BX_REPO)
local_repo = git.Repo(Cfg.LOCAL_REPO)
remote_name = "origin/"


def _rebase_repo(repo, src_branch, dst_branch):
  repo.git.checkout(dst_branch)
  repo.git.rebase(remote_name + src_branch)
  repo.remote().push(force=True)


def _merge_repo(repo, src_branch, dst_branch, push_upstream):
  repo.git.checkout(dst_branch)
  repo.git.merge(remote_name + src_branch)
  if push_upstream:
    repo.remote().push()


def rebase_changes_all():
  """Rebase all changes according to current configuration"""
  for dst, src in const.GIT_TRACKING.items():
    rebase_changes(src, dst)


def rebase_changes(src_branch, dst_branch):
  """Be careful with this, since this uses a rebase ensure that the
  destination branch is not a public branch!"""
  print(f"Rebasing {src_branch} into {dst_branch}")
  adf_thread = Thread(target=_rebase_repo,
                      args=(adf_repo, src_branch, dst_branch))
  bx_thread = Thread(target=_rebase_repo,
                     args=(bx_repo, src_branch, dst_branch))

  adf_thread.start()
  bx_thread.start()

  adf_thread.join()
  bx_thread.join()
  print(f"Rebased {src_branch} into {dst_branch}")


def propagate_changes(src_branch, dst_branch, push_upstream):
  """Ensure that the leaf_branch is not a public branch,
  i.e no one else is working on that branch"""
  print(f"Propagating {src_branch} into {dst_branch}")
  adf_thread = Thread(
      target=_merge_repo,
      args=(adf_repo, src_branch, dst_branch, push_upstream))
  bx_thread = Thread(
      target=_merge_repo,
      args=(bx_repo, src_branch, dst_branch, push_upstream))

  adf_thread.start()
  bx_thread.start()

  adf_thread.join()
  bx_thread.join()
  print(f"Propagated {src_branch} into {dst_branch}")
