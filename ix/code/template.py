import os
import ix.config as config
import ix.regex as ixre
import ix.fs as ixfs

tag = "template"
Tag = "Template"
TAG = "TEMPLATE"


def generateTemplate(src_fp, dst_dir, key, value=None):

  # read the file
  text = ixfs.read(src_fp)

  # check if there is a different substitution value
  if value is None:
    value_camel = tag
    value_pascal = Tag
    value_const = TAG
  else:
    value_camel = ixre.toCamel(value)
    value_pascal = ixre.toPascal(value)
    value_const = ixre.toConst(value)

  # Make the substitutions
  text = ixre.to_template(ixre.toCamel(key), value_camel, text)
  text = ixre.to_template(ixre.toPascal(key), value_pascal, text)
  text = ixre.to_template(ixre.toConst(key), value_const, text)

  filename = ixre.to_template(key, Tag, os.path.basename(src_fp))

  # write out the file
  ixfs.write(os.path.join(dst_dir, filename), text)


def generate_multi_templates(dst_dir, key, *src_fps):

  for src_fp in src_fps:
    generateTemplate(src_fp, dst_dir, key)


def substitute_multi_template(dst_dir, key, value, *src_fps):
  subs = ixre.to_fmt_dict(key, value)
  for src_fp in src_fps:
    ixfs.write(
        os.path.join(dst_dir, ixre.subkv(subs, os.path.basename(src_fp))),
        ixre.subkv(subs, ixfs.read(src_fp)))


def apply_template(template, src_fp, dst_dir, fmt_subs=None):

  # Substitution map
  if fmt_subs is None:
    fmt_subs = {tag: template}
  else:
    fmt_subs[tag] = template

  # read the file
  text = ixfs.read(src_fp)

  # make the substitutions
  text, _ = ixre.subf(text, fmt_subs)

  # Get the templated name
  dst_fp = os.path.join(
      dst_dir, ixre.subf(os.path.basename(src_fp), fmt_subs)[0])

  # write out the destination file
  ixfs.write(dst_fp, text)

  return dst_fp


def apply_template_dir(template, src_dir, dst_dir, fmt_subs=None):

  for fp in os.listdir(src_dir):
    if os.path.isfile(os.path.join(src_dir, fp)):
      apply_template(template, os.path.join(src_dir, fp), dst_dir, fmt_subs)


def multiTemplate(srcFilename, dstFilename, *templates):
  """Create multiple files from one template"""

  # Creat substitution map
  fmt_subs = {tag: ""}

  # Get outfile name
  filepath = os.path.join(config.bldDir(), dstFilename)
  ixfs.write(filepath, "")  # clear the file

  for template in templates:
    # Build sub map
    fmt_subs[tag] = template

    # read the file
    text = ixfs.read(ixfs.findr(config.srcDir(), srcFilename))

    # make the substitutions
    text, _ = ixre.subf(text, fmt_subs)

    # append to file
    ixfs.append(filepath, text)

  return filepath
