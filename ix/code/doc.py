import os
import re
import ix.fs as ixfs
import ix.regex as ixregex


def python(directory):

  file_pttrn = re.compile(r"\.py")
  method_pttrn = re.compile(r"(\s*)def(\s+)(.+)\((.+)\):\n")
  # class_pttrn = re.compile(r"(\s*)class(\s+)(.+)\((.+)\):\n")
  whitespace = re.compile(r"\s*")

  for root, _, files in os.walk(directory):

    for f in files:

      # Skip all non python files
      if file_pttrn.search(f) is None:
        continue

      filepath = os.path.join(root, f)
      text = ixfs.read(filepath)

      for m in method_pttrn.finditer(text):
        docNdxSt = text.find('"""', m.endpos)

        # Skip if it found a docstring
        if whitespace.match(text[m.endpos:docNdxSt]) is not None:
          continue

        print(f"Unable to find docstring for method({m.group()})"
              f"at line ({ixregex.get_line_number(text, m.start())}")

        # TODO replace with docstring
