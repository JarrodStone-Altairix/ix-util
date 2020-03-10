from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED
from flask import request, send_file
from flask_restful import Resource
import ix.regex as ixre
import ix.code.template as ixtemplate


class CreateTemplate_Basic(Resource):
  def post(self):
    args = request.get_json()

    subs = {
        k: ixre.to_template(v) for (k, v) in
        ixre.to_fmt_dict(args["template"], ixtemplate.Tag).items()}
    text = ixre.subkv(subs, args["text"])

    return {"text": text}


class ApplyTemplate_Basic(Resource):
  def post(self):
    args = request.get_json()

    fp = BytesIO()
    if len(args["templates"]) > 1:
      filename = "templates.zip"
      zf = ZipFile(fp, mode="w", compresslevel=ZIP_DEFLATED)
      for template in args["templates"]:
        zf.writestr(
            ixre.subf({ixtemplate.Tag: template}, args["filename"]),
            ixre.subf({ixtemplate.Tag: template}, args["text"]))
      zf.close()
    else:
      template = args["templates"][0]
      filename = ixre.subf({ixtemplate.Tag: template}, args["filename"])
      fp.write(ixre.subf({ixtemplate.Tag: template}, args["text"])
               .encode("utf-8"))

    fp.seek(0)
    return send_file(
        fp, as_attachment=True,
        attachment_filename=filename)
