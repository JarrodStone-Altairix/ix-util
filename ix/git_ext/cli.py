import click
import ix.const as const
import ix.git_ext as ixgit


@click.group()
def cli():
  click.echo("Fetching from upstream...")
  # Fetch from upstream for all commands
  ixgit.adf_repo.remote().fetch()
  ixgit.bx_repo.remote().fetch()
  ixgit.local_repo.remote().fetch()


@cli.command()
def pull_all():
  ixgit.adf_repo.git.pull()
  ixgit.bx_repo.git.pull()
  ixgit.local_repo.git.pull()


@cli.command()
@click.argument("dst", type=click.STRING)
def rebase(dst):
  src = const.GIT_TRACKING.get(dst)
  if src is None:
    click.echo(f"Unable to find source branch for ({dst}).")
  else:
    ixgit.rebase_changes(src, dst)


@cli.command()
def rebase_all():
  ixgit.rebase_changes_all()


@cli.command()
@click.argument("src", type=click.STRING)
@click.option("-p", "--push_upstream", is_flag=True)
def propagate(src, push_upstream):
  dst = const.GIT_TRACKING.get(src)
  if dst is None:
    click.echo(f"Unable to find source branch for ({dst}).")
  else:
    ixgit.propagate_changes(src, dst, push_upstream)


if __name__ == "__main__":
  cli()
