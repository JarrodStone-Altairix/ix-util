import os
import shutil
import ix.config as ixcfg
import ix.regex as ixre


def findr(directory, filename):
  for root, _, files in os.walk(directory):
    for f in files:
      if f == filename:
        return os.path.join(root, f)

  return None


def read(filepath):
  """Opens a file at filepath and returns all the text in the file"""
  filePtr = open(filepath, "r")
  text = filePtr.read()
  filePtr.close()

  return text


def read_line(fp, line_no):
  text = read(fp)

  for ndx, m in enumerate(ixre._line_pttrn.finditer(text)):
    if ndx == line_no - 1:
      st_line = text.rfind("\n", 0, m.start() - 1) + 1
      return text[st_line:m.start() - 1]

  return ""


def readInput():
  return read(os.path.join(ixcfg.srcDir, ixcfg.inputTextFile()))


def inputFile():
  return open(os.path.join(ixcfg.srcDir, ixcfg.inputTextFile()), "r")


def write(filepath, text):
  filePtr = open(filepath, "w+")
  text = filePtr.write(text)
  filePtr.close()


def writeOutput(text):
  write(os.path.join(ixcfg.bldDir(), ixcfg.outputTextFile()), text)


def outputFile():
  return open(os.path.join(ixcfg.bldDir(), ixcfg.outputTextFile()), "w+")


def append(filepath, text):
  filePtr = open(filepath, "a+")
  text = filePtr.write(text)
  filePtr.close()


def cleanDir(abs_path):
  for f in os.listdir(abs_path):
    fp = os.path.join(abs_path, f)

    if os.path.isfile(fp):
      os.remove(fp)
    elif os.path.isdir(fp):
      shutil.rmtree(fp)


def cleanBldDir():
  cleanDir(ixcfg.bldDir())
