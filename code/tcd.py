import os
import ix.config as config
import ix.regex as ixre
import ix.code.java as java
import ix.code.template as ixtemplate

def createTcd(name, *newFields):

  # Create class
  tcd = java.Enum("public", f"{name}Tcd")

  # Enum Field Template
  tcd.addInterface(f"HasEnumField<{name}Tcd>")

  # Add Enum basic fields
  tcd.addField(java.Field("private static final", "String", "CLASSNM", f"{name}Tcd.class.getName()"))
  tcd.addField(java.Field("private static final", "String", "CLASSNM_SIMPLE", f"{name}Tcd.class.getSimpleName()"))
  tcd.addField(java.Field("private static final", "Logger", "logger", "LoggerFactory.getLogger(CLASSNM)"))

  # build full field list
  fields = [("String", "value"), ("String", "desc")]
  fields.extend(newFields)
  # create default values
  dftValues = list(map(lambda f : java.typeDefault(f[0]), newFields))

  # Default Enums
  tcd.addEnum("All", "\"*\"", "\"ALL\"", *dftValues)
  tcd.addEnum("NULL", "\"@\"", "\"NULL\"", *dftValues)

  constructor = java.Method("", None, f"{name}Tcd", "\n")
  # Add Enum values
  for fType, fName in fields:
    constructor.addArgument(fType, fName)
    constructor.body += f"    this.{fName} = {fName};\n"
    tcd.addField(java.Field("private", fType, fName))
    tcd.addMethod(java.Method("public", fType, f"get{ixre.toPascal(fName)}", f"return {fName};"))
  tcd.addMethod(constructor)

  # add methods
  tcd.addMethod(java.Method("public", "boolean", "isInstanceof", f"return testValue instanceof {name}Tcd;").addArgument("Object", "testValue"))
  tcd.addMethod(java.Method("public", "boolean", "isSelectionValue", f"return tstEnum == ALL;").addArgument(name, "tstEnum"))
  tcd.addMethod(java.Method("public", f"{name}Tcd", "toEnum", f"""
    if (enumString != null) {{
      for ({name}Tcd enumVal: values()) {{
        if (enumVal.value.equals(enumString)) {{
          return enumVal;
        }}
      }}
    }}

    logger.error("Invalid value({{}}) for {{}}.toEnum()", enumString, CLASSNM);

    return null;""").addArgument("String", "enumString"))
  tcd.addMethod(java.Method("public", "String", "toString", """return CLASSNM_SIMPLE + "(" + value + ")";"""))

  # write out the create file
  tcd.toFile(config.bldDir())

  # Create the TcdField java file
  ixtemplate.applyTemplate(name, "TcdField.java", f"{name}TcdField.java")


