from flask import request
from flask_restful import Resource
import ix.regex as ixre


class Substitute(Resource):
  def post(self):
    args = request.get_json()

    text = args["text"].replace(ixre.to_camel(args["find"]),
                                ixre.to_camel(args["replace"]))
    text = text.replace(ixre.to_pascal(args["find"]),
                        ixre.to_pascal(args["replace"]))
    text = text.replace(ixre.to_css(args["find"]),
                        ixre.to_css(args["replace"]))

    return {
        "text": text.replace(ixre.to_const(args["find"]),
                             ixre.to_const(args["replace"]))}


class Case(Resource):

  case_switch = {
      "pascal": ixre.to_pascal,
      "camel": ixre.to_camel,
      "const": ixre.to_const,
  }

  def post(self):
    args = request.get_json()

    text = ixre.to_const(args["text"]) \
        if ixre.const_pttrn.match(args["text"]) \
        else args["text"]

    return {"text": Case.case_switch[args["case"]](text)}
