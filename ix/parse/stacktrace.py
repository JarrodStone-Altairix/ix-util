def getCommon(stacktraces):

  # Create a flattend map of all the stack traces
  flatmap = {}
  for stack in stacktraces:
    for n, method in enumerate(stack):
      if method in flatmap:
        flatmap[method].append(n)
      else:
        flatmap[method] = [n]

  return flatmap
  # stackCnt = len(stacktraces)
  # for k, v in flatmap.items():
    # if len(v) == stackCnt:

      

