from functools import reduce
import ix.parse.ixjson as ixjson

_msg = 'msg'
_unmatched = 'unmatched'


def read_log(filepath, severities, *paths, **kwargs):
  """Reads a GAE log and returns them in an array of JSON like objects. If a
  pattern is matched on a data object, but there are messages that are not
  matched or ignored they are added to the resulting object in an array called
  'unmatched'

  Parameters:
    filepath : str
      Path to the file that will be loaded
    pathtuple : list(path.to.gae.value, output.path.name)
      paths to be copied
    msgtuple : list(path.in.gae.line, output.path.name)
      this may or may not exist, msg paths to be copied
    patterntuple : list(output.path.name, Regex Search Pattern)
      patterns to be matched
    ignorelist : list(output.path.name, Regex Search Pattern)
      patterns to be ignored

  returns a list of errors and messages that were neither matched nor ignored
  """
  data = ixjson.load(filepath)

  msg_paths = kwargs.get("msg_paths")
  pattern_pairs = kwargs.get("pattern_pairs")
  ignore_pairs = kwargs.get("ignore_pairs")

  errors = []
  outstanding = []
  for d in data:

    if d['severity'] not in severities:
      continue

    err = {
        _msg: {},
        _unmatched: []
    }

    for path in paths:
      val = ixjson.resolvePath(d, path)
      err[path] = val

    err_msgs = [x for x in d['protoPayload']['line']
                if x['severity'] in severities]

    for name, pattern in patterntuple:

      vic = None
      for msg in err_msgs:

        m = pattern.search(msg['logMessage'])
        if m is not None:

          err[_msg][name] = {}
          for path, msg_name in msgtuple:
            err[_msg][name][msg_name] = ixjson.resolvePath(msg, path)

          err[_msg][name]['matches'] = m.groups()
          vic = msg
          break

      if vic is not None:
        err_msgs.remove(vic)

    errors.append(err)

    for msg in err_msgs:
      if reduce(lambda a, b: a or b,
                map(lambda ig: ig.search(msg['logMessage']) is None,
                    ignorelist), False):
        outstanding.append(msg)
      else:
        um = {key: ixjson.resolvePath(msg, path) for path, key in msgtuple}
        um['message'] = msg['logMessage']
        err[_unmatched].append(um)

  return errors, outstanding


def _read_err_msgs(err_list, pattern_pairs, msg_paths):

  for err_msg in err_list:
    pass

  for name, pattern in pattern_pairs:
    pass
