import asyncio
import click
from ix.web_assess.update_config import update_config_coroutine
from ix.web_assess.find_and_replace import find_and_replace as fnr


@click.group()
def cli():
  pass


@cli.command()
@click.argument("identities", nargs=-1)
def update_config(identities):
  asyncio.run(update_config_coroutine(identities))


@cli.command()
@click.argument("find", type=click.STRING)
@click.argument("replace", type=click.STRING)
@click.argument("identities", nargs=-1)
@click.option("--regex", type=click.BOOL, default=False,
              is_flag=True, help="search by regex")
def find_and_replace(identities, find, replace, regex):
  fnr(identities, find, replace, regex)
