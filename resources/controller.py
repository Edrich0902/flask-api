import os
from flask_restful import Resource, request

class Controller(Resource):
    def get(self):
        print(os.getenv('API_KEY'))
        return 'Testing message'