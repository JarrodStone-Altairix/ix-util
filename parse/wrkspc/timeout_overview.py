import os
import re
import json
import csv
import ix.config as ixcfg
import ix.parse.ixjson as ixjson
import ix.fs as ixfs

data = ixjson.load(os.path.join(ixcfg.dlDir, 'gae_log_acts.json'))

number = re.compile(r"[\d]+")
high_latency = [x for x in data if float(number.search(x['protoPayload']['latency']).group()) > 60]
data_filtered = [x['protoPayload']['line'] for x in high_latency]

text = []
for payload in data_filtered:
  text.append(''.join(t['logMessage'] for t in payload))

out = []
stackPattern = re.compile(r"doPost: Error\(This request \(\w+\) started at .+? UTC and was still executing at .+? UTC\.\) encountered processing Servlet PUT Request\n(.+)")
i = 0
for n, t in enumerate(text):
  m = stackPattern.search(t)
  if not m is None:
    out.append(f"{n}\t{m.group(1)}")
  else:
    out.append(f"{n}\t")

for n, d in enumerate(high_latency):
  out[n] += f"\t{d['protoPayload']['ip']}\t{d['httpRequest']['status']}\t"

  if 'instanceId' in (d['protoPayload']):
    out[n] += f"{d['protoPayload']['instanceId']}"

  out[n] += '\t'
  if 'responseSize' in (d['protoPayload']):
    out[n] += f"{d['protoPayload']['responseSize']}"

ixfs.writeOutput('\n'.join(x for x in out))
