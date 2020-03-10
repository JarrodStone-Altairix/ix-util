from flask import request
from flask_restful import Resource
from ix.code.builder import generate


class Generate(Resource):
  def post(self):
    args = request.get_json()
    return {"text": generate(
        args["class"], args.get("base"),
        args["required"], args["optional"]).toString()}
