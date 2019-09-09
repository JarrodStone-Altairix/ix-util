import re
import ix.fs as ixfs
from ix.regex import _line_pttrn

find_match_pattern = re.compile(r"Match at line \((\d+)\) in file\((.+)\)")


def append_to_line(fp, line_no, append_text):
  file_text = ixfs.read(fp)

  for ndx, match in enumerate(_line_pttrn.finditer(file_text, 0)):

    if ndx == line_no - 1:
      ixfs.write(fp, "".join([
          file_text[:match.start()],
          append_text,
          file_text[match.start():]]))
      return

  print(f"Unable to find line number {line_no} in ({fp}")
