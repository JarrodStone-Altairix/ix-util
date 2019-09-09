import os
import re
import ix.fs as fs
import ix.config as config
import ix.code.service.method as srvcMethod
import ix.code.java as javaClass

# Examples:
# createAdfService("Resource", "loadAudio", "AudioSet")
# createBxService("Resource", "loadAudio", "AudioSet")

_srvcMthdPrefix = "SRVCMTHDNM_"
_doMethodRE = re.compile(r"public\s+ServiceResponseManifest\s+doMethod\s*\(ServiceRequestManifest\s+\w+\)\s*{([\w\s\(\)\{\}\.\;]*)(?=return\s*super\.doMethod\(\s*\w+\s*\)\;)")

def _modifyLocalService(serviceName, methodName, constMethodName, dataObj, fileDir):
  filepath = fs.findr(fileDir, f"{serviceName}LocalService.java")
  if filepath == None:
    print(f"Unable to find: {serviceName}LocalService.java")
    return False
  fileTxt = fs.read(filepath)

  match = _doMethodRE.search(fileTxt)
  doMethodBody = fileTxt[match.start(1):match.end(1)]
  lastIf = doMethodBody.rfind("if")
  endElseBlock = match.start(1) + javaClass.getCorresponding(doMethodBody[lastIf:], "{", "}") + lastIf + 1
 
  classClose = fileTxt.rfind("}")
  doMethod = javaClass.Method("private", "ServiceResponseManifest", "doMethod_" + methodName)
  doMethod.addArgument("ServiceRequestManifest", "srvcReqMan")
  doMethod.body = "// " + config.TODO_Tag +  " to be implemented.\n"

  newFile = open(filepath, "w+")
  newFile.write(fileTxt[:endElseBlock] + 
  f"""
    if (srvcReqMan.getMethodName().equals({serviceName}Const.{_srvcMthdPrefix}{constMethodName})) {{ 
      return doMethod_{methodName}(srvcReqMan);
    }}"""
    + fileTxt[endElseBlock:classClose] + "\n"
    + srvcMethod.createDoMethod(serviceName, methodName, dataObj) + "\n"
    + srvcMethod.createIsValidMethod(serviceName, methodName, dataObj) + "\n"
    + srvcMethod.createImplMethod(serviceName, methodName, dataObj) + "\n"
    + fileTxt[classClose:])
  newFile.close()

  return True

def _modifyConstFile(serviceName, methodName, constMethodName, fileDir):
  filepath = fs.findr(fileDir, f"{serviceName}Const.java")
  if filepath == None:
    print(f"Unable to find: {serviceName}Const.java")
    return False
  fileTxt = fs.read(filepath)

  lastConstEndLine = fileTxt.rfind(_srvcMthdPrefix) 
  lastConstEndLine = fileTxt[lastConstEndLine:].find(";") + lastConstEndLine + 1

  newFile = open(filepath, "w+")
  newFile.write(fileTxt[:lastConstEndLine] + f"""
  public static final String {_srvcMthdPrefix}{constMethodName} = "{methodName}";"""
    + fileTxt[lastConstEndLine:])
  newFile.close()

  return True

def _modifyProviderFile(serviceName, methodName, constMethodName, isSync, dataObj, fileDir):
  filepath = fs.findr(fileDir, f"{serviceName}Provider.java")
  if filepath == None:
    print(f"Unable to find: {serviceName}Provider.java")
    return False
  fileTxt = fs.read(filepath)

  classClose = fileTxt.rfind("}") 

  newFile = open(filepath, "w+")
  newFile.write(fileTxt[:classClose] + "\n"
    + srvcMethod.createProviderMethod(serviceName, methodName, constMethodName, isSync, dataObj) 
    + fileTxt[classClose:])
  newFile.close()

  return True

def _createService(serviceName, methodName, dataObj, serverDir, syncDir, commDir, asyncDir):
  constMethodName = re.sub("(.)([A-Z])", r"\1_\2", methodName).upper()

  if not _modifyLocalService(serviceName, methodName, constMethodName, dataObj, serverDir):
    return
  if not _modifyConstFile(serviceName, methodName, constMethodName, commDir): 
    return
  if not _modifyProviderFile(serviceName, methodName, constMethodName, True, dataObj, syncDir): 
    return
  if not _modifyProviderFile(serviceName, methodName, constMethodName, False, dataObj, asyncDir):
    return

  print("Success!")

def createAdfService(serviceName, methodName, dataObj):
  _createService(serviceName, methodName, dataObj, config.AdfServer, config.AdfSync, config.AdfCommon, config.AdfAsync)

def createBxService(serviceName, methodName, dataObj):
  _createService(serviceName, methodName, dataObj, config.BxServer, config.BxSync, config.BxCommon, config.BxAsync)
