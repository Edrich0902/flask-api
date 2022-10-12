import os
from flask_restful import Resource, request
from flask import jsonify
from common.http import handle_request

class Controller(Resource):
    def get(self):
        url = request.get_json()['url']
        return jsonify(handle_request(url))