import re
from flask import request
from flask_restful import Resource
from ix.parse.util import format_table, format_pivot


class Format_Table(Resource):
  def post(self):
    args = request.get_json()
    return {"text": format_table(args["text"])}


class Format_Pivot(Resource):
  def post(self):
    args = request.get_json()
    # Remove any excess whitespace
    text = re.sub(r"(\S) +", r"\1 ", args["text"])
    return {"text": format_pivot(text, args["pivot"])}
