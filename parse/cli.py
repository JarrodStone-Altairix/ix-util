import os
import click
from ix.config import Cfg
import ix.regex as ixre
import ix.parse.diff as ixdiff


@click.group()
def cli():
  pass


@cli.command()
@click.argument("regex_match")
@click.option("-fr", "--file-regex", type=click.STRING, default=r"\.java",
              help="regex pattern to match files")
@click.option("-d", "--directory", type=click.STRING, default=Cfg.git_repo,
              help="directory to recursively search")
def find(regex_match, file_regex, directory):
  ixre.findr(directory, file_regex, regex_match)


@cli.command()
@click.argument("file_regex")
@click.option("-d", "--directory", type=click.STRING, default=Cfg.git_repo,
              help="directory to recursively search")
def locate(file_regex, directory):
  ixre.findr(directory, file_regex, None)


@cli.command()
@click.argument("regex_match")
@click.argument("regex_replace")
@click.option("-fr", "--file-regex", type=click.STRING, default=r"\.java",
              help="regex pattern to match files")
@click.option("-d", "--directory", type=click.STRING, default=Cfg.git_repo,
              help="directory to recursively search")
def subr(regex_match, regex_replace,
         file_regex=r"\.java", directory=Cfg.git_repo):
  ixre.subr(directory, file_regex, regex_match, regex_replace)


@cli.command()
@click.argument("dir_left", type=click.STRING)
@click.argument("dir_right", type=click.STRING)
@click.option("-f", "--output_fmt", type=click.STRING, default="")
def diffr(dir_left, dir_right, output_fmt):

  if not os.path.isdir(dir_left):
    click.echo("dir_left must be a directory.")
    return
  if not os.path.isdir(dir_right):
    click.echo("dir_right must be a directory.")
    return

  dc = ixdiff.diffr(dir_left, dir_right)
  if output_fmt == "dirs" or output_fmt == "directories":
    print(f"{os.linesep}Directories only in '{dir_left}':")
    print(os.linesep.join(dc.left_dirs))
    print(f"{os.linesep}Directories only in '{dir_right}':")
    print(os.linesep.join(dc.right_dirs))
  elif output_fmt == "files":
    print(f"Differing common files:")
    print(os.linesep.join(dc.diff_common_files))
    print(f"{os.linesep}Files only in '{dir_left}':")
    print(os.linesep.join(dc.left_files))
    print(f"{os.linesep}Files only in '{dir_right}':")
    print(os.linesep.join(dc.right_files))
  else:
    print(dc)
