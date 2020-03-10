import click
from ix.db.cli import cli as cli_db
from ix.git_ext.cli import cli as cli_git
from ix.parse.cli import find, locate, subr, diffr
from ix.web_assess.cli import cli as cli_web_assess


@click.group()
def cli():
  pass


cli.add_command(cli_db, name="db")
cli.add_command(cli_git, name="git")
cli.add_command(find)
cli.add_command(locate)
cli.add_command(subr)
cli.add_command(diffr)
cli.add_command(cli_web_assess, name="wa")

if __name__ == "__main__":
  cli()
