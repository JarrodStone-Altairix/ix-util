import os
import csv
import ix.config as ixcfg
import ix.parse.ixjson as ixjson
import ix.fs as ixfs

csvfile = csv.reader(open(os.path.join(ixcfg.dlDir, 'stacktraces.txt'), "r"))
csvOut = csv.writer(ixfs.outputFile())

for i, line in enumerate(csvfile):

  stackmap = {}
  for val in line:
    if val in stackmap:
      stackmap[val] += 1
    else:
      stackmap[val] = 1
  
  stacklist = []
  for k, v in stackmap.items():
    stacklist.append(k)
    stacklist.append(v)
  
  csvOut.writerow(stacklist)

  # stacklist.append(stackmap)


