import os
import re
import json
import csv
import ix.config as ixcfg
import ix.parse.ixjson as ixjson
import ix.fs as ixfs
import ix.parse.stacktrace as ixstacktrace

data = ixjson.load(os.path.join(ixcfg.dlDir, 'gae_log_acts.json'))

srvcReqPattern = re.compile(r"Service Request\(((:?\w+\.?)+)\)")
number = re.compile(r"[\d]+")
high_latency = [x for x in data if float(number.search(x['protoPayload']['latency']).group()) > 60]

errors = []

for d in high_latency:
  err = {
    'latency' : d['protoPayload']['latency'],
    'opId' : d['operation']['id'],
    'versionId' : d['protoPayload']['versionId'],
  }

  msgs = [x for x in d['protoPayload']['line'] if x['severity'] == "ERROR" and 'sourceLocation' in x]
  for msg in msgs:
    msg.pop('Severity', None)
    log = msg.pop('logMessage', None)

    rNdx = log.find('\n')
    if rNdx > 0:
      msg['firstLine'] = log[log.find(":") + 1:rNdx].strip()
      err['faultingMethod'] = log[rNdx + 1 : log.find('\n', rNdx + 1)]
      err['stacktrace'] = log.splitlines()[1:]
    else:
      msg['firstLine'] = log[log.find(":") + 1:].strip()

    m = srvcReqPattern.search(msg['firstLine'])
    if m is not None:
      err['srvcReq'] = m.group(1)

  err['msgs'] = msgs
  errors.append(err)

complete = [e for e in errors if 'srvcReq' in e if 'stacktrace' in e]

srvcReqMap = {}
for e in complete:
  if e['srvcReq'] in srvcReqMap:
    srvcReqMap[e['srvcReq']] += 1
  else:
    srvcReqMap[e['srvcReq']] = 1

# for e in errors:
#   print("".join(f"{m['sourceLocation']['file']}:{m['sourceLocation']['line']}" for m in e['msgs']))

# json.dump(srvcReqMap, ixfs.outputFile(), indent=2, sort_keys=True)
# json.dump(errors, ixfs.outputFile(), indent=2, sort_keys=True)
# json.dump([e for e in errors if 'srvcReq' not in e and 'stacktrace' in e], ixfs.outputFile(), indent=2, sort_keys=True)

# traces = ixstacktrace.getCommon([e['stacktrace'] for e in errors if 'stacktrace' in e])
# csvfile = csv.writer(ixfs.outputFile())
# for k, v in traces.items():
#   csvfile.writerow([len(v), k, *v])

# for err in errors:
  # if 'srvcReq' in err and 'stacktrace' in err:
    # print(err['opId'])

csvfile = csv.writer(ixfs.outputFile())
for err in errors:
  out = [err['opId'], err['latency']]
  if 'srvcReq' in err:
    out.append(err['srvcReq'])
  if 'faultingMethod' in err:
    out.append(err['faultingMethod'])
  csvfile.writerow(out)
