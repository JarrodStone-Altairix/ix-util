import re
import pandas as pd
from csv import writer
from google.cloud import storage
from ix.google_ext.gae import (
    preprocess_log, preprocess_log_str, parse_log_str)

log_paths = [
    "protoPayload.traceId",
    "protoPayload.responseSize"]

req_pttrn = re.compile(r"Request\((.+?)\)")
used_pttrn = re.compile(r"Used Memory:  (\d+) \/ (\d+) \/ \+?(-?\d+)")
free_pttrn = re.compile(r"Free Memory:  (\d+) \/ (\d+)")
total_pttrn = re.compile(r"Total Memory: (\d+)( \/ \d+)?")
max_pttrn = re.compile(r"Max Memory:   (\d+)( \/ \d+)?")


def regex(msg):
  req_m = req_pttrn.search(msg)

  used_m = used_pttrn.search(msg)
  total_m = total_pttrn.search(msg)
  max_m = max_pttrn.search(msg)

  if used_m is None or total_m is None or max_m is None:
    return None

  return [
      req_m.group(1) if req_m is not None else "None",
      used_m.group(3),
      *total_m.groups(),
      *max_m.groups()
  ]


def get_logs(path):
  client = storage.Client()
  bucket_name = "brainex-prod.appspot.com"
  path = "appengine.googleapis.com/request_log/" + path

  logs = []
  for blob in client.list_blobs(bucket_name, prefix=path):
    logs.extend(parse_log_str(
        preprocess_log_str(blob.download_as_string().decode("utf-8")),
        log_paths, regex, False))

  return logs


def get_sample_logs():
  logs = parse_log_str(
      preprocess_log("C:/Users/Jarrod/Downloads/log.json"),
      log_paths, regex, False)

  return logs


def write_csv(logs, fp):
  csv_file = writer(open(fp, "w+"))
  csv_file.writerow([
      "Id", "Size", "Method", "Used Delta", "Total Start",
      "Total End", "Max Start", "Max End"])
  csv_file.writerows(logs)


def analysis(fp):
  df = pd.read_csv(fp)

  ud = df.groupby(["Method"])["Used Delta"]
  stats = pd.concat(
      [ud.mean(), ud.median(), ud.var(), ud.count(), ud.nunique()],
      axis=1, sort=False)
  stats.columns = ["Mean", "Median", "Variance", "Count", "Unique"]
  stats.to_csv("stats.csv")


file_ptr = "out.csv"

# write_csv(get_sample_logs(), file_ptr)
write_csv(get_logs("2019/12/02"), file_ptr)

analysis(file_ptr)
