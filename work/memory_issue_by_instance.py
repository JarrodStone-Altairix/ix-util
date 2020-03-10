import re
import pandas as pd
import datetime
import os
from csv import writer
import ix.google_ext.gae as gae
import matplotlib.pyplot as plt


log_paths = [
    "protoPayload.traceId", "protoPayload.responseSize",
    "timestamp", "protoPayload.instanceId", "protoPayload.host",
    "protoPayload.resource", "protoPayload.userAgent"]

req_pttrn = re.compile(r"Request\((.+?)\)")
used_pttrn = re.compile(r"Used Memory:  (\d+) \/ (\d+) \/ \+?(-?\d+)")
free_pttrn = re.compile(r"Free Memory:  (\d+) \/ (\d+)")
total_pttrn = re.compile(r"Total Memory: (\d+)(?: \/ (\d+))?")
max_pttrn = re.compile(r"Max Memory:   (\d+)(?: \/ (\d+))?")


def _read_csv(fp):
  return pd.read_csv(
      fp, parse_dates=["Timestamp"],
      date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%dT%H:%M:%S.%fZ"))


def regex(msg):
  req_m = req_pttrn.search(msg)

  used_m = used_pttrn.search(msg)
  total_m = total_pttrn.search(msg)
  max_m = max_pttrn.search(msg)

  if used_m is None or total_m is None or max_m is None:
    return None

  return [
      req_m.group(1) if req_m is not None else "None",
      used_m.group(1), used_m.group(2), used_m.group(3),
      *total_m.groups(),
      *max_m.groups()
  ]


def download_parse_logs(fp, path):
  logs = gae.parse_log_storage(
      "brainex-prod.appspot.com",
      "appengine.googleapis.com/request_log/2019/" + path,
      log_paths, regex, False)
  csv_file = writer(open(fp, "w+"))
  csv_file.writerow([
      "Id", "Size", "Timestamp", "Instance", "Host", "Resource", "User Agent",

      "Method", "Used Start", "Used End", "Used Delta", "Total Start",
      "Total End", "Max Start", "Max End"])
  csv_file.writerows(logs)


def analysis(fp):
  df = _read_csv(fp)

  for tsp in df["Instance"].unique():
    df[df["Instance"] == tsp].plot(
        title=tsp, kind="line", x="Timestamp",
        y=["Used Start", "Total Start", "Max Start"])

    # df[df["Instance"] == tsp].plot(
        # title=tsp, kind="bar", x="Timestamp",
        # y=["Used Delta"], color=[(1, 0, 0)])

  df[df["Used Delta"] > 1e8].to_csv("day_stats.csv")
  plt.show()


def download_logs_batch():
  date = datetime.date(2019, 12, 13)
  today = datetime.date.today()
  while date < today:
    file_ptr = f"data/{date.strftime('%d %b')}.csv"
    print(f"Downloading {file_ptr}...")
    download_parse_logs(file_ptr, date.strftime('%m/%d/'))
    date = date + datetime.timedelta(1)


def analyze_stats():
  dfs = [
      _read_csv(f"data/{fp}")
      for fp in os.listdir("data") if fp.endswith(".csv")]
  df = pd.concat(dfs, axis=0, ignore_index=True)

  df["Date"] = [d.date() for d in df.Timestamp]
  df["Time"] = [d.time() for d in df.Timestamp]
  df[df["Used Delta"] > 1e8].to_csv("stats.csv")


def find_high_start(fp, cutoff):
  df = _read_csv(fp)
  df["Date"] = [d.date() for d in df.Timestamp]
  df["Time"] = [d.time() for d in df.Timestamp]
  df[df["Used End"] >= cutoff].to_csv("high_end.csv")


def get_range(fp, st, end):
  df = _read_csv(fp)
  df["Date"] = [d.date() for d in df.Timestamp]
  df["Time"] = [d.time() for d in df.Timestamp]
  df.iloc[st:end].to_csv("range.csv")


date = datetime.date(2019, 12, 12)
file_ptr = f"data/{date.strftime('%d %b')}.csv"
# download_parse_logs(file_ptr, date.strftime('%m/%d/'))
analysis(file_ptr)

# download_logs_batch()
# analyze_stats()
# find_high_start(file_ptr, 350e6)
# get_range(file_ptr, 2100, 2150)
