import asyncio
import click
from ix.web_assess.update_config import update_config_coroutine


@click.group()
def cli():
  pass


@cli.command()
@click.argument("identities", nargs=-1)
def update_config(identities):
  asyncio.run(update_config_coroutine(identities))
