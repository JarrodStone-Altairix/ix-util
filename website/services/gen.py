from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED
from flask import request, send_file
from flask_restful import Resource
import os
import ix.fs as ixfs
import ix.regex as ixre
from ix.code.template import tag

packageData = ixfs.read("generate/src/CreatePackageData.java")
loadCommandStr = ixfs.read("generate/src/LoadCommand.java")
tcd = ixfs.read("generate/src/Tcd.java")
tcdField = ixfs.read("generate/src/TcdField.java")


class AdfPackage(Resource):
  def get(self):
    return create_package("generate/src/@AdfTemplate")


class BxPackage(Resource):
  def get(self):
    return create_package("generate/src/@BxTemplate")


class CreatePackageData(Resource):
  def get(self):
    return apply_template(packageData, "Create%sData.java")


class LoadCommand(Resource):
  def get(self):
    return apply_template(loadCommandStr, "Load%s.java")


class Tcd(Resource):
  def get(self):
    return apply_template(tcd, "%sTcd.java")


class TcdField(Resource):
  def get(self):
    return apply_template(tcdField, "%sTcdField.java")


def apply_template(source_str, dst_filename_fmt):
  name = ixre.to_pascal(request.args["name"])
  text, _ = ixre.subf({tag: name}, source_str)
  mem_file = BytesIO(text.encode("utf-8"))
  mem_file.seek(0)
  return send_file(
      mem_file, as_attachment=True,
      attachment_filename=dst_filename_fmt % name)


def create_package(template_dir):
  Name = ixre.to_pascal(request.args["name"])
  name = ixre.to_camel(request.args["name"])

  fmt_subs = ixre.to_template_dict(tag, name)
  fp = BytesIO()
  zf = ZipFile(fp, mode="w", compresslevel=ZIP_DEFLATED)

  template_dir_len = len(template_dir) + 1
  for root, _, files in os.walk(template_dir):
    new_root = ixre.subkv(fmt_subs, root[template_dir_len:])

    for f in files:
      text = ixre.subkv(fmt_subs, ixfs.read(os.path.join(root, f)))
      new_filename = ixre.subkv(fmt_subs, f)
      zf.writestr(os.path.join(new_root, new_filename), text)

  zf.close()
  fp.seek(0)
  return send_file(
      fp, as_attachment=True,
      attachment_filename=f"{Name}.zip")
