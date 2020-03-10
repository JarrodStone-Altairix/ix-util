import os
import ix.config as config
import ix.code.template as ixtemplate
import ix.regex as ixre
import ix.fs as ixfs


def _createPackage(templateDir, packageName):

  # Create new package output directory
  pkgRoot = os.path.join(config.bldDir(), packageName)
  os.mkdir(pkgRoot)
  formatSubs = {ixtemplate.tag: packageName}

  # Copy files over
  templateDirLen = len(templateDir) + 1
  for root, dirs, files in os.walk(templateDir):
    # determine the new root name and make the appropriate name substitution
    newRoot, _ = ixre.subf(os.path.join(pkgRoot, root[templateDirLen:]),
                           formatSubs)
    # Rename new directories that are created
    for d in dirs:
      newDir, _ = ixre.subf(d, formatSubs)
      os.mkdir(os.path.join(newRoot, newDir))

    # Any files that are copied over have a format substitution
    for f in files:
      # Read the old file
      text = ixfs.read(os.path.join(root, f))

      # Make the substitutions in new text
      text, _ = ixre.subf(text, formatSubs)

      # Get the new filename
      filename, _ = ixre.subf(f, formatSubs)

      # Save in a new file
      ixfs.write(os.path.join(newRoot, filename), text)

  return pkgRoot

def createBxPackage(packageName):
  _createPackage(config.bxTemplateDir(), packageName)

def createAdfPackage(packageName):
  _createPackage(config.adfTemplateDir(), packageName)

def createPackageData(loaderName):
  return ixtemplate.applyTemplate(loaderName, "CreatePackageData.java", f"Create{loaderName}Data.java")

def createLoadCommand(loaderName):
  return ixtemplate.applyTemplate(loaderName, "LoadCommand.java", f"Load{loaderName}.java")

def createArrayList(arrName, objName):
  fmtSub = {"Object" : objName}
  return ixtemplate.applyTemplate(arrName, "ArrayList.java", f"{arrName}ArrayList.java", fmtSub)

def createTcd(tcdName):
  return ixtemplate.applyTemplate(tcdName, "Tcd.java", f"{tcdName}Tcd.java")

def createTcdField(tcdName):
  return ixtemplate.applyTemplate(tcdName, "TcdField.java", f"{tcdName}TcdField.java")
