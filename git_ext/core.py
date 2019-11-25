import git
import ix.const as const

adf_repo = git.Repo(const.ADF_REPO)
bx_repo = git.Repo(const.BX_REPO)
local_repo = git.Repo(const.LOCAL_REPO)
remote_name = "origin/"


def rebase_changes(repo, src_branch, dst_branch):
  """Be careful with this, since this uses a rebase ensure that the
  destination branch is not a public branch!"""
  repo.git.checkout(dst_branch)
  repo.git.rebase(remote_name + src_branch)
  repo.remote().push(force=True)


def propagate_changes(repo, root_branch, leaf_branch, auto_push=False):
  """Ensure that the leaf_branch is not a public branch,
  i.e no one else is working on that branch"""
  # Push changes upstream
  repo.git.checkout(root_branch)
  repo.git.merge(remote_name + root_branch)
  repo.git.merge(leaf_branch)

  if auto_push:
    repo.remote().push()
