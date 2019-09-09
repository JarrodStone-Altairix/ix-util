import os
import re
import json
import csv
import ix.config as ixcfg
import ix.parse.ixjson as ixjson
import ix.fs as ixfs

data = ixjson.load(os.path.join(ixcfg.dlDir, 'gae_log.json'))

number = re.compile(r"[\d]+")
high_latency = [x for x in data if float(number.search(x['protoPayload']['latency']).group()) > 60]
data_filtered = [x['protoPayload']['line'] for x in high_latency]

text = []
for payload in data_filtered:
  text.append(''.join(t['logMessage'] for t in payload))

largestStack = 0
stacktraces = []
stackPattern = re.compile(r"doPost: Error\(This request \(\w+\) started at .+? UTC and was still executing at .+? UTC\.\) encountered processing Servlet PUT Request\n((:?.+\n)+)")

for t in text:
  m = stackPattern.search(t)
  if not m is None:
    stack = m.group(1).splitlines()
    stacktraces.append(stack)
    if len(stack) > largestStack:
      largestStack = len(stack)
  else:
    stacktraces.append(None)

csvfile = csv.writer(ixfs.outputFile())
csvfile.writerow([n for n, _ in enumerate(text)])

for i in range(largestStack):
  line = []
  for stack in stacktraces:
    if stack is None or i >= len(stack):
      line.append("")
    else:
      line.append(stack[i])
  
  csvfile.writerow(line)
