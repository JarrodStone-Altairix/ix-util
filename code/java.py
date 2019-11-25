import os
import re

fieldPttrn = re.compile(r"(.*)(\w+)\s+(\w+)\s*(=[\S ]+)?\s*;")
methodPttrn = re.compile(r"(.*)(\w+)\s+(\w+)\s*\((.*)\)\s*([{;}])")

_dftTypeMap = {
    "byte": "0",
    "char": "''",
    "short": "0",
    "int": "0",
    "long": "0",
    "float": "0",
    "double": "0",
    "boolean": "false",
    "void": "null",
    "Integer": "0",
    "Float": "0",
    "Double": "0",
    "String": "\"\""
}


def typeDefault(jtype):
  ret = _dftTypeMap.get(jtype)

  return ret if ret is not None else "null"


class Field:

  def __init__(self, access, fieldType, name, value=None):
    self._access = access
    self._fieldType = fieldType
    self._name = name
    self._value = value

  def setDefaultValue(self, value):
    self._value = value
    return self

  def toString(self):
    str = self._access + " " + self._fieldType + " " + self._name
    if self._value is not None:
      str += " = " + self._value

    return str + ";"


class Method:

  def __init__(self, access, returnValue, name, body=";"):
    self._access = access
    self._returnValue = returnValue
    self._name = name
    self._args = []
    self.body = body

  def addArgument(self, fieldType, fieldName):
    self._args.append((fieldType, fieldName))
    return self

  def toString(self):
    tab = Class.tabChar
    str = tab + self._access + " "
    if self._returnValue is not None:
      str += self._returnValue + " "
    str += self._name + "("

    length = len(self._args) - 1
    for i, (fType, fName) in enumerate(self._args):
      str += fType + " " + fName
      if i < length:
        str += ", "

    str += ") {\n" + tab + tab + self.body
    str += "\n" + tab + "}\n"
    return str


class Enum:
  tabChar = "  "

  def __init__(self, access, name):
    self._access = access
    self._name = name
    self._package = None
    self._interfaces = []
    self._enums = []
    self._fields = []
    self._methods = []

  def addInterface(self, interface):
    self._interfaces.append(interface)

  def addEnum(self, name, *args):
    self._enums.append((name, *args))

  def addField(self, field):
    self._fields.append(field)

  def addMethod(self, method):
    self._methods.append(method)

  def setPackage(self, package):
    self._package = package

  def toString(self):
    tab = Class.tabChar

    str = self._access + " enum " + self._name + " "

    if len(self._interfaces) > 0:
      str += "implements"
      for i, interface in enumerate(self._interfaces):
        str += " " + interface
        if i < len(self._interfaces) - 1:
          str += ","

    str += " {\n\n"

    for enumNdx, enum in enumerate(self._enums):
      name, *args = enum
      str += tab + name + " ("

      for i, arg in enumerate(args):
        str += arg
        if i < len(args) - 1:
          str += ", "

      if enumNdx < len(self._enums) - 1:
        str += "),\n"
      else:
        str += ");\n"

    if len(self._enums) > 0:
      str += "\n"

    for field in self._fields:
      str += tab + field.toString() + "\n"

    str += "\n"

    for method in self._methods:
      str += method.toString() + "\n"

    str += "}"

    return str

  def toFile(self, filepath):
    jFile = open(os.path.join(filepath, self._name + ".java"), "w+")
    if self._package is None:
      jFile.write(self.toString())
    else:
      jFile.write("package " + self._package + "\n\n" + self.toString())
    jFile.close()


class Class:
  tabChar = "  "

  def __init__(self, access, name):
    self._access = access
    self._name = name
    self._baseClass = None
    self._package = None
    self._imports = []
    self._interfaces = []
    self._enums = []
    self._nestedClasses = []
    self._fields = []
    self._methods = []

  def setPackage(self, package):
    self._package = package

  def setBaseClass(self, baseClass):
    self._baseClass = baseClass

  def addImport(self, imprt):
    self._imports.append(imprt)

  def addInterface(self, interface):
    self._interfaces.append(interface)

  def addEnum(self, enum):
    self._enums.append(enum)

  def addNestedClass(self, nestedClass):
    self._nestedClasses.append(nestedClass)

  def addField(self, field):
    self._fields.append(field)

  def addMethod(self, method):
    self._methods.append(method)

  def toString(self):
    tab = Class.tabChar

    str = ""
    if self._package is not None:
      str += "package " + self._package + ";\n\n"

    for imprt in self._imports:
      str += "import " + imprt + ";\n"
    if len(self._imports) > 0:
      str += "\n"

    str += self._access + " class " + self._name + " "
    if self._baseClass:
      str += "extends " + self._baseClass + " "

    if len(self._interfaces) > 0:
      str += "implements"
      for i, interface in enumerate(self._interfaces):
        str += " " + interface
        if i < len(self._interfaces) - 1:
          str += ","

    str += " {\n\n"

    for enum in self._enums:
      str += tab + enum.toString() + "\n"
    if len(self._enums) > 0:
      str += "\n"

    for nestedClass in self._nestedClasses:
      str += nestedClass.toString()
    if len(self._nestedClasses) > 0:
      str += "\n"

    for field in self._fields:
      str += tab + field.toString() + "\n"
    if len(self._fields) > 0:
      str += "\n"

    for method in self._methods:
      str += method.toString()

    str += "}"

    return str

  def toFile(self, filepath):
    jFile = open(os.path.join(filepath, self._name + ".java"), "w+")
    jFile.write(self.toString())
    jFile.close()


def getCorresponding(text, openChar, closeChar):
  i = 0
  for ndx, c in enumerate(text):
    if c == openChar:
      i += 1
    elif c == closeChar:
      i -= 1
      if i <= 0:
        return ndx


def _loadField(text):
  m = fieldPttrn.search(text)

  if m.group(4) == "":
    ret = Field(m.group(1), m.group(2), m.group(3))
  else:
    ret = Field(m.group(1), m.group(2), m.group(3), m.group(4))

  return ret


def _loadMethod(text):
  m = fieldPttrn.search(text)

  if m.group(5) == "{":
    ret = Method(m.group(1), m.group(2), m.group(3), text[m.end():-1])
  else:
    ret = Method(m.group(1), m.group(2), m.group(3))

  argPttrn = re.compile(r"(\w+)\s+(\w+)")
  for arg in m.group(4).split(","):
    m = argPttrn.search(arg)
    ret.addArgument(m.group(1), m.group(2))

  return ret


def _loadEnum(text):
  m = re.search(r"([\w\s]+)\s+enum\s+(\w+)\s+implements\s+([\w<>,\s]+){", text)
  modifier = ""
  for mod in re.finditer(r"\w+", m.group(1)):
    modifier += mod + " "

  ret = Enum(modifier.strip(), m.group(2))
  for intr in re.finditer(r"([\w<>]+),?", m.group(3)):
    ret.addInterface(intr.group(1))

  ndx = text.find(";", m.end())
  for enum in re.finditer(r"(\w+)\s*(?:\((.*)\))?[,;]", text[m.end():ndx + 1]):
    if enum.group(2) == "":
      ret.addEnum(enum.group(1))
    else:
      eArgs = re.sub(r"\s+", "", enum.group(2)).split(",")
      ret.addEnum(enum.group(1), eArgs)

  st = 0
  text = text[ndx + 1:]
  for m in re.finditer(r"[;{]", text):
    if not fieldPttrn.search(text[st:m.end()]) is None:
      ret.addField(_loadField(text[st:m.end()].strip()))
      st = m.end()
    else:
      methodM = methodPttrn.search(text[st:m.end()])
      if methodM is not None:
        if methodM.group(5) == "{":
          end = getCorresponding(text[st:], "{", "}")
        else:
          end = m.end()
        ret.addField(_loadMethod(text[st:end].strip()))
        st = end
      else:
        st = m.end()

  return ret


def load(filepath):
  jFile = open(filepath)
  text = jFile.read()
  jFile.close()

  name = re.findall(r"(\w+)\.java", filepath)[0]
  jClass = Class("", name)
  m = re.search(r"package\s+([\w|.]+)", text)
  jClass.setPackage(m.group(1))
  end = 0

  for m in re.finditer(r"import\s+([\w\.]+)", text):
    jClass.addImport(m.group(1))
    if m.end() > end:
      end = m.end()

  st = text.find("public", end)
  end = text.find("{", st)
  m = re.search(
      r"((?:public\s+|abstract\s+|static\s+|final\s+){1,})class", text[st:end])
  jClass._access = m.group(1).strip()
  m = re.search(r"extends\s+(\w+)", text[st:end])

  if m is not None:
    jClass.setBaseClass(m.group(1))
  m = re.search(r"implements\s+((?:\w+,?\s*){1,})", text[st:end])
  if m is not None:
    for match in re.finditer(r"(\w+),?", m.group(1)):
      jClass.addInterface(match.group(1))

  st = 0
  text = text[text.find("{", end) + 1:]
  enumPttrn = re.compile(r"\s+enum\s+")
  classPttrn = re.compile(r"\s+class\s+")
  for m in re.finditer(r"[{;]", text):
    if st > m.start():
      continue
    print(text[st:m.start()])
    if not enumPttrn.search(text[st:m.start()]) is None:
      end = getCorresponding(text[st:], "{", "}")
      jClass.addEnum(_loadEnum(text[st:end]))
      st = end
    elif not classPttrn.search(text[st:m.start()]) is None:
      end = getCorresponding(text[st:], "{", "}")
      st = end
      print(text[st:end])
    else:
      st = m.end()

  # print(text[st:end])
  # print(text)
  # print(jClass.toString())
  # print(text[:100])

  return jClass

# load(r"C:\Users\Jarrod\Desktop\out\webAssessSession\Server\webAssessSession\WebAssessSessionLocalService.java")
