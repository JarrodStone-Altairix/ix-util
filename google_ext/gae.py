import json
from google.cloud import storage


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
    return "\n\n>===<\n\n".join(msgs)


def preprocess_log(fp):
  fd = open(fp)
  text = fd.read()
  fd.close()
  return preprocess_log_str(text)


def preprocess_log_str(text):
  text = text.replace("}\n", "},\n", text.count("}\n") - 1)
  return json.loads(f"[{text}]")


def parse_log_str(log, paths=[], regex_func=None, include_msg=True):

  paths_list = [p.split(".") for p in paths]
  out = []
  for line in log:
    msg = _resolve_app_msgs(line)

    if msg is None:
      continue

    row = [_resolve_path(line, p) for p in paths_list]
    if regex_func is not None:
      matches = regex_func(msg)
      if matches is None:
        continue
      row.extend(regex_func(msg))

    if include_msg:
      row.append(msg)

    out.append(row)

  return out


def parse_log_storage(bucket_name, bucket_prefix, log_paths=[],
                      regex_func=None, include_msg=True):
  client = storage.Client()
  ret = []
  for blob in client.list_blobs(bucket_name, prefix=bucket_prefix):
    ret.extend(parse_log_str(
        preprocess_log_str(blob.download_as_string().decode("utf-8")),
        log_paths, regex_func, include_msg))

  return ret
