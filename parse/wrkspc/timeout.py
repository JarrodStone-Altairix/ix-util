import os
import re
import json
import csv
import ix.parse.gae as ixgae
import ix.config as ixcfg
import ix.parse.ixjson as ixjson
import ix.fs as ixfs
import ix.parse.stacktrace as ixstacktrace

pathmap = [
  ("protoPayload.versionId", "versionId"),
  ("protoPayload.latency", "latency"),
  ("protoPayload.resource", "resource"),
  ("protoPayload.taskName", "taskName"),
  ("protoPayload.megaCycles", "megaCycles"),
  ("protoPayload.startTime", "time_start"),
  ("protoPayload.endTime", "time_end"),
  ("severity", "severity"),
  ("traceSampled", "traceSampled"),
]
msgmap = [
  ("time", "time"),
  ("sourceLocation.file", "file"),
  ("sourceLocation.line", "line"),
  ("sourceLocation.functionName", "method")
]
patternmap = [
  ("stack", re.compile(r"doPost: Error\(This request \(\w+\) started at .+? UTC and was still executing at .+? UTC\.\) encountered processing Servlet PUT Request\n(.+)")),
  ('srvcReq', re.compile(r"Service Request\(((?:\w+\.?)+)\)")),
  ('exception', re.compile(r"(java\..+): ===> (.+)")),
  # ('deadline', re.compile(r"(Process terminated because the request deadline was exceeded\. \(Error code 123\))")),
]
ignorelist = [
  re.compile(r"<continued from previous message>"),
  re.compile(r"Process terminated because the request deadline was exceeded\. \(Error code 123\)"),
]
# Load files
errs, outstanding = ixgae.read_log(os.path.join(ixcfg.dlDir, 'gae_log.json'), pathmap, msgmap, patternmap, ignorelist)
_ = ixgae.read_log(os.path.join(ixcfg.dlDir, 'gae_log_acts.json'), pathmap, msgmap, patternmap, ignorelist)
errs.extend(_[0])
outstanding.extend(_[1])

# filtering
num_p = re.compile(r"\d+\.\d+")
errs = [e for e in errs if float(num_p.search(e['latency']).group(0)) > 60]
# errs = [e for e in errs if len(e['unmatched']) > 0]

# Load files
# errs = ixjson.load(os.path.join(ixcfg.dlDir, 'gae_log.json'))
# errs.extend(ixjson.load(os.path.join(ixcfg.dlDir, 'gae_log_acts.json')))

# Dump the error files
# json.dump(outstanding, ixfs.outputFile(), indent=2, sort_keys=True)
json.dump(errs, ixfs.outputFile(), indent=2)
# ixjson.flatten_list_to_csv(ixfs.outputFile(), *errs)

# Dump the stacktraces
# stacktraces = ixstacktrace.getCommon(list(map(lambda y : y[0].splitlines(), filter(lambda x: not x is None, [ixjson.resolvePath(e, "msg.stacktrace") for e in errs]))))
# csvwriter = csv.writer(ixfs.outputFile())
# for k, v in stacktraces.items():
#   csvwriter.writerow([len(v), k, *v])

# data = ixjson.load(os.path.join(ixcfg.dlDir, 'gae_log.json'))
# data.extend(ixjson.load(os.path.join(ixcfg.dlDir, 'gae_log_acts.json')))
# results = []
# for d in data:
#   keymap = ixjson.flatten(d)

#   for k, v in keymap.items():
#     if not k in results:
#       results.append(k)

# ixfs.writeOutput("\n".join(r for r in results))