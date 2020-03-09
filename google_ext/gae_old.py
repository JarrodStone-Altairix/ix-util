from functools import reduce
import ix.parse.ixjson as ixjson

_msg = 'msg'
_unmatched = 'unmatched'


def read_log(filepath, pathtuple, msgtuple, patterntuple, ignorelist):
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
    ignorelist : list(str(output.path.name), Regex Search Pattern)
      patterns to be ignored

  returns a list of errors and messages that were neither matched nor ignored
  """
  data = ixjson.load(filepath)

  errors = []
  outstanding = []
  for d in data:

    if not d['severity'] == 'ERROR':
      continue

    err = {
        _msg: {},
        _unmatched: []
    }

    for path, name in pathtuple:
      val = ixjson.resolvePath(d, path)
      err[name] = val

    err_msgs = [x for x in d['protoPayload']['line']
                if x['severity'] == 'ERROR']

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