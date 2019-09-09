import click
import ix.git_ext as ixgit


@click.group()
def cli():
  click.echo("Fetching from upstream...")
  # Fetch from upstream for all commands
  ixgit.adf_repo.remote().fetch()
  ixgit.bx_repo.remote().fetch()


@cli.command()
@click.argument("src", type=click.STRING)
@click.argument("dst", type=click.STRING)
def rebase(src, dst):
  click.echo(f"Rebasing from {src} into {dst}.")
  ixgit.rebase_changes(ixgit.adf_repo, src, dst)
  ixgit.rebase_changes(ixgit.bx_repo, src, dst)


@cli.command()
@click.argument("src", type=click.STRING)
@click.argument("dst", type=click.STRING)
@click.option("--auto_push", is_flag=True)
def propagate(src, dst, auto_push):
  click.echo(f"Propagating changes from {src} into {dst}")
  ixgit.propagate_changes(ixgit.adf_repo, src, dst, auto_push)
  ixgit.propagate_changes(ixgit.bx_repo, src, dst, auto_push)


@cli.command()
@click.argument("src", type=click.STRING)
@click.argument("dst", type=click.STRING)
@click.option("--auto_push", is_flag=True)
def update(src, dst, auto_push):
  click.echo(f"Rebasing from {src} into {dst}.")
  ixgit.rebase_changes(ixgit.adf_repo, src, dst)
  ixgit.rebase_changes(ixgit.bx_repo, src, dst)

  click.echo(f"Propagating changes from {dst} into {src}")
  ixgit.propagate_changes(ixgit.adf_repo, src, dst, auto_push)
  ixgit.propagate_changes(ixgit.bx_repo, src, dst, auto_push)

  click.echo(f"Rebasing new changes in from {src} into {dst}.")
  ixgit.rebase_changes(ixgit.adf_repo, src, dst)
  ixgit.rebase_changes(ixgit.bx_repo, src, dst)


if __name__ == "__main__":
  cli()
