import os
import re

propPattern = re.compile(r"(\\w+)\\h*=\\h*(.*)")

def loadPropFile(filepath):
  file = open(filepath, "r")
  if file is None:
    return None

  ret = {}
  r = file.read()
  m = re.findall(r"(\w+)[^\S\n]*=[^\S\n]*(.*)", r)
  for (prop, value) in m:
    ret[prop] = value

  return ret
