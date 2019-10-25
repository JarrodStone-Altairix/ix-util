import json


def _resolve_path(obj, path):
  ret = obj

  for p in path:
    if isinstance(p, int):
      if p < len(ret):
        ret = ret[p]
      else:
        return None
    elif p in ret:
      ret = ret[p]
    else:
      return None

  return ret


def _resolve_app_msgs(obj):
  lines = _resolve_path(obj, ["protoPayload", "line"])
  if lines is None:
    return None
  else:
    msgs = map(lambda l: l["logMessage"], lines)
    return "\n".join(msgs)


def parse_log(in_fp, paths=[]):
  log = json.load(open(in_fp))
  out = []

  for line in log:
    row = [_resolve_app_msgs(line)]
    row.extend([_resolve_path(line, p) for p in paths])

    out.append(row)

  return out
