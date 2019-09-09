import os
import json

_cfg_file = json.load(
    open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                      'config.json')))


def _resolve(*paths):
  return os.path.join(*[_cfg_file[p] for p in paths])


def home():
  return _cfg_file['home']


def gitRepo():
  return _resolve('home', 'gitRepo')


def adfRepo():
  return _resolve('home', 'gitRepo', 'adfRepo')


def bxRepo():
  return _resolve('home', 'gitRepo', 'bxRepo')


def adfCommon():
  return _resolve('home', 'gitRepo', 'adfRepo', 'adfCommon')


def adfServer():
  return _resolve('home', 'gitRepo', 'adfRepo', 'adfServer')


def adfSync():
  return _resolve('home', 'gitRepo', 'adfRepo', 'adfSync')


def adfAsync():
  return _resolve('home', 'gitRepo', 'adfRepo', 'adfAsync')


def adfGWT():
  return _resolve('home', 'gitRepo', 'adfRepo', 'adfGWT')


def bxCommon():
  return _resolve('home', 'gitRepo', 'bxRepo', 'bxCommon')


def bxServer():
  return _resolve('home', 'gitRepo', 'bxRepo', 'bxServer')


def bxSync():
  return _resolve('home', 'gitRepo', 'bxRepo', 'bxSync')


def bxAsync():
  return _resolve('home', 'gitRepo', 'bxRepo', 'bxAsync')


def bxGWT():
  return _resolve('home', 'gitRepo', 'bxRepo', 'bxGWT')


def bxServerFile():
  return _cfg_file['bxServerFile']


def bldDir():
  return _cfg_file['bldDir']


def srcDir():
  return _cfg_file['srcDir']


def adfTemplateDir():
  return _resolve('srcDir', 'adfTemplateDir')


def bxTemplateDir():
  return _resolve('srcDir', 'bxTemplateDir')


def inputTextFile():
  return _resolve('inputTextFile')


def outputTextFile():
  return _resolve('outputTextFile')


def inputTextFilepath():
  return _resolve('srcDir', 'inputTextFile')


def outputTextFilepath():
  return _resolve('bldDir', 'outputTextFile')


def downloadsDir():
  return os.path.join(os.getenv('USERPROFILE'), 'Downloads')


TODO_Tag = "TODO_JS"
TODO_Impl = f"// {TODO_Tag} Implement this method"


class Cfg:
  home = "C:\\Altairix"
  git_repo = home + "\\Git Repository"
  adf_repo = git_repo + "\\ADF"
  adf_common = adf_repo + "\\Altairix ADF - Common\\src\\com\\altairix\\comm\\adf" # noqa
  adf_server = adf_repo + "\\Altairix ADF - Server\\src\\com\\altairix\\adf"
  adf_sync = adf_repo + "\\Altairix ADF - Sync\\src\\com\\altairix\\adf"
  adf_async = adf_repo + "\\Altairix ADF - Async\\src\\com\\altairix\\async\\adf" # noqa
  adf_GWT = adf_repo + "\\Altairix ADF - GWT\\src\\com\\altairix\\gwt"
  bx_repo = git_repo + "\\Brainex"
  bx_common = bx_repo + "\\Arrowsmith - Common\\src\\com\\arrowsmith\\comm"
  bx_server = bx_repo + "\\Arrowsmith - Server\\src\\com\\arrowsmith"
  bx_sync = bx_repo + "\\Arrowsmith - Sync\\src\\com\\arrowsmith"
  bx_async = bx_repo + "\\Arrowsmith - Async\\src\\com\\arrowsmith\\async"
  bx_GWT = bx_repo + "\\Arrowsmith - GWT\\src\\com\\arrowsmith\\gwt"
  downloads_dir = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
