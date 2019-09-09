import json
import csv
import re

_PATH_DELIM = '.'
DFT_INDENT = '  '
_index_pttrn = re.compile(r"(.+)\[(\d+)\]")


def load(filepath):
  """Loads a json object from filepath"""

  return json.load(open(filepath))


def _decompose(data, indent):
  if isinstance(data, dict):
    inner = "\n".join(
        f"{indent}{DFT_INDENT}{k}{_decompose(v, indent + DFT_INDENT)}"
        for k, v in data.items())
    return f"\n{indent}{{\n{inner}\n{indent}}}"
  if isinstance(data, list) or isinstance(data, tuple):
    inner = f"".join(
        f"{_decompose(d, indent + DFT_INDENT)}" for d in data)
    return f"\n{indent}[{inner}\n{indent}]"

  return ""


def decompose(data):
  """returns a string of the skeleton structure of the data"""

  return _decompose(data, '')


def resolvePath(obj, path, invalid=None):
  """Resolves the path in the obj, if it is
  invalid it returns invalid[default:None]
  """

  ret = obj
  paths = path.split(_PATH_DELIM)

  for i in range(0, len(paths)):
    if paths[i] in ret:
      ret = ret[paths[i]]
    else:
      m = _index_pttrn.search(paths[i])
      if m is not None and m.group(1) in ret:
        ret = ret[m.group(1)][int(m.group(2))]
      else:
        return invalid

  return ret


def joinPath(*paths):
  """Joins any number of paths using the Path Deliminiator"""

  return _PATH_DELIM.join(s for s in paths if not s == "")


def _flatten(data, path, keymap):
  if isinstance(data, list) or isinstance(data, tuple):
    for n, d in enumerate(data):
      _flatten(d, joinPath(path, str(n)), keymap)
  elif isinstance(data, dict):
    for k, v in data.items():
      _flatten(v, joinPath(path, k), keymap)
  else:
    keymap[path] = data


def flatten(data):
  """Converts a hierarchical JSON object into a flat dictionary,
  Each key is the full path to each object"""

  keymap = {}
  _flatten(data, "", keymap)
  return keymap


def flatten_data(*data):
  """Flattens data from an list of JSON like objects"""

  n = len(data)
  results = {}

  for i, d in enumerate(data):

    keymap = flatten(d)

    for k, v in keymap.items():
      if k not in results:
        results[k] = [None] * n

      results[k][i] = v

  return results


def flatten_list_to_csv(fileObj, *data):
  """Flattens data from an array of JSON like objects
  then writes it to a file
  """

  results = flatten_data(*data)

  csvfile = csv.writer(fileObj)
  csvfile.writerow(results.keys())
  for i in range(0, len(data)):
    csvfile.writerow([x[i] for x in results.values()])
