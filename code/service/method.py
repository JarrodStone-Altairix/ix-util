import ix.config as config
import ix.regex as ixre
import ix.config as config
import ix.code.java as javaClass

def _getProvider(serviceName):
  providerNm = f"{serviceName}Provider"
  providerVar = f"{ixre.toCamel(serviceName)}Prdr"

  return providerNm, providerVar

# Create the do_method in the local service
def createDoMethod(serviceName, methodName, dataObj):
  providerNm, providerVar = _getProvider(serviceName)
  if not dataObj is None:
    dataObjVar = ixre.toCamel(dataObj)

  # Create the method class
  doMethod = javaClass.Method("private", "ServiceResponseManifest", "doMethod_" + methodName)
  doMethod.addArgument("ServiceRequestManifest", "srvcReqMan")

  doMethod.body = """
    // Get generic objects
    ServiceStub srvcStub  = srvcReqMan.getServiceObject();"""
  if not dataObj is None:
    doMethod.body += """
    BaseObject dataObj  = srvcReqMan.getParm(SrvcConst.PARMNM_DATA_OBJECT);"""
  
  doMethod.body += f"""
    // Validate Service Object class
    if (! (srvcStub instanceof {providerNm})) {{
      return malformedRequest("Missing {providerNm}", srvcReqMan);
    }}"""
  
  if not dataObj is None:
    doMethod.body += f"""
    // Validate Object Class
    if (dataObj == null) {{
      return malformedRequest("Missing {dataObj} + ", srvcReqMan);
    }}
    else if (!(dataObj instanceof {dataObj})) {{
      return malformedRequest("Cannot cast to {dataObj}", srvcReqMan);
    }}
    """

  doMethod.body += f"""
    {providerNm} {providerVar} = ({providerNm}) srvcStub;"""  
  if not dataObj is None:
    doMethod.body += f"""
    {dataObj} {dataObjVar} = ({dataObj}) dataObj;"""

  doMethod.body += f"""
    if (!isValid{methodName[:1].upper() + methodName[1:]}({providerVar})) {{ return invalidRequest(srvcReqMan); }}"""
  
  doMethod.body += f"""
    boolean rtFg = {methodName}({providerVar}"""
  if not dataObj is None:
    doMethod.body += f", {dataObjVar}"

  doMethod.body += ");\n"

  doMethod.body += """
    // Compose and return response
    ServiceResponseManifest srvcRspMan =
      new ServiceResponseManifest(srvcReqMan.getMethodName(), srvcReqMan.getServiceObject(),
      ServiceDataFlag.INCLUDE, rtFg);\n"""
  if not dataObj is None:
    doMethod.body += f"""
    srvcRspMan.addParm(SrvcConst.PARMNM_DATA_OBJECT, {dataObjVar});"""

  doMethod.body += """
    return srvcRspMan;"""

  return doMethod.toString()

def createIsValidMethod(serviceName, methodName, dataObj):
  providerNm, providerVar = _getProvider(serviceName)

  newMethod = javaClass.Method("private", "boolean", "isValid" + methodName[:1].upper() + methodName[1:])
  newMethod.addArgument(providerNm, providerVar)

  newMethod.body = f"""// {config.TODO_Tag} implement this method.

    return true;"""

  return newMethod.toString()


def createImplMethod(serviceName, methodName, dataObj):
  providerNm, providerVar = _getProvider(serviceName)

  newMethod = javaClass.Method("private", "boolean", methodName)
  newMethod._args.append((providerNm, providerVar))
  if not dataObj is None:
    newMethod.addArgument(dataObj, ixre.toCamel(dataObj))

  newMethod.body = f"""// {config.TODO_Tag} implement this method.

    return true;"""

  return newMethod.toString()

def createProviderMethod(serviceName, methodName, constMethodNm, isSync, dataObj):
  newMethod = javaClass.Method("public", "void", methodName)

  if not dataObj is None:
    dataObjVar = ixre.toCamel(dataObj)
    newMethod.addArgument(dataObj, dataObjVar)

  if not isSync:
    newMethod.addArgument("AsyncCallback<ServiceResponseManifest>", "callback")

  newMethod.body = f"""
    // {config.TODO_Tag} complete this method.

    ServiceRequestManifest srvcReqMan = new ServiceRequestManifest(
      {serviceName}Const.SRVCMTHDNM_{constMethodNm}, this, ServiceDataFlag.INCLUDE);
    """
  if not dataObj is None:
    newMethod.body += f"srvcReqMan.addParm(SrvcConst.PARMNM_DATA_OBJECT, {dataObjVar});"

  if isSync:
    newMethod.body += "\n\n    doMethod(srvcReqMan);"
  else:
    newMethod.body += "\n\n    doMethod(srvcReqMan, callback);"


  return newMethod.toString()
