import os
import re
import ix.fs as fs

# _line_pttrn = re.compile(os.linesep)
_line_pttrn = re.compile("\n")
_to_constPattern = re.compile(r"([a-z])([A-Z])")

pascal_pttrn = re.compile(r"^[A-Z][a-zA-Z0-9_]+$")
camel_pttrn = re.compile(r"^[a-z][a-zA-Z0-9_]+$")
const_pttrn = re.compile(r"^[A-Z][A-Z0-9_]+$")


def to_pascal(text):
  return text[0].upper() + text[1:]


def to_camel(text):
  return text[0].lower() + text[1:]


def to_const(text):
  text, _ = _to_constPattern.subn(r"\1_\2", text)
  return text.upper()


def to_css(text):
  return _to_constPattern.sub(r"\1-\2", text)


def from_const(text):
  return "".join([s[0].upper() + s[1:].lower() for s in text.split("_")])


def to_template(text):
  return f"~@{{{text}}}"


def to_template_dict(key, value):
  return {
      to_template(to_pascal(key)): to_pascal(value),
      to_template(to_camel(key)): to_camel(value),
      to_template(to_const(key)): to_const(value)
  }


def to_fmt_dict(key, value):
  return {
      to_pascal(key): to_pascal(value),
      to_camel(key): to_camel(value),
      to_const(key): to_const(value)
  }


def get_line_number(position, text):
  return len(_line_pttrn.findall(text, 0, position)) + 1


def findr(directory, file_regex, search_regex=None, **kwargs):
  """Search recursively in a directory for a file that matches file_regex.
  If a search regex is supplied then it will search the file for that pattern

  Parameters:
    directory: str
      Root directory to search in
    file_regex: str
      Regular expression to match file names
    search_regex: str
      Regular expression to match in the file

  Optional Parameters:
    filter: func():bool
      additional filter logic, return True on match
    print: str
      print in a different format {match, line}
  """

  file_pttrn = re.compile(file_regex)

  filterMatch = kwargs['filter'] if 'filter' in kwargs else None
  printType = kwargs['print'] if 'print' in kwargs else 'line'
  fp_matches = []

  if search_regex is not None:
    search_pttrn = re.compile(search_regex)

  fileMatches = 0
  totalMatches = 0
  for root, _, files in os.walk(directory):
    for f in files:
      if file_pttrn.search(f) is None:
        continue

      filepath = os.path.join(root, f)
      if search_regex is None:
        fp_matches.append(filepath)
        fileMatches += 1
        print(f"Matched file({filepath}).")
        continue

      text = fs.read(filepath)
      matches = 0
      for m in search_pttrn.finditer(text):
        lineNo = get_line_number(m.start(), text)

        if filterMatch is not None and not filterMatch(m):
          continue

        matches += 1

        if printType == 'match':
          print(m.group())
        elif printType == 'line':
          print(f"Match at line ({lineNo}) in file({filepath})")

      totalMatches += matches
      if matches > 0:
        fp_matches.append(filepath)
        fileMatches += 1

  print(f"Found {totalMatches} matches in {fileMatches} file(s).")
  return fp_matches


def subr(directory, file_regex, search_regex, replace_regex):
  """Recursively search through a directory and search and replace in each file.

  Params:
    directory: str
      Directory to start the search
    search_regex: str
      pattern to match in the file
    replace_regex: str
      pattern to replace in the file
    file_regex: str
      regex pattern to match files
  """

  # Compile patterns
  search_pttrn = re.compile(search_regex)
  file_pttrn = re.compile(file_regex)

  # Recursively search through directory
  total_subs = 0
  for root, _, files in os.walk(directory):
    for f in files:

      # If a pattern is supplied and it isn't matched, skip the file
      if file_pttrn is not None and file_pttrn.search(f) is None:
        continue

      # Read the file
      filepath = os.path.join(root, f)
      text = fs.read(filepath)

      # Make the appropriate substitutions
      text, n = search_pttrn.subn(replace_regex, text)
      if n > 0:
        print(f"({n}) substitutions in file({filepath})")
        total_subs += n

        fs.write(filepath, text)

  print(f"Total substitutions: {total_subs}")


def subkv(subs, text):
  """Takes a dictionary of substitution map and applies them
  to the text

  Params:
    subs: dict{k:v}
      substitutions to be made
    text: str
      texts to be substituted"""

  for k, v in subs.items():
    text = text.replace(k, v)
  return text


def subf(subs, text):
  """Makes substitutions looking for the ~@{key} and replaces with the
  associated value. Matches on pascal case, camel case and upper case keys.
  For example:
    ~@{keyCamel} -> valueCamel
    ~@{KeyCamel} -> ValueCamel
    ~@{KEY_CAMEL} -> VALUE_CAMEL

  Params:
    text: str
      Text to be replaced
    substitutions: dict{k:v}
      dictionary of keys and values to be replaced. keys should be provided in
      camel case or pascal case and the brackets will be added as part of the
      search."""
  for key, value in subs.items():
    fmt_subs = to_template_dict(key, value)
    text = subkv(fmt_subs, text)

  return text
