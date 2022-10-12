from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#controllers
from resources.controller import Controller

app = Flask(__name__)
api = Api(app)
CORS(app)

#routes
api.add_resource(Controller, '/')
#routes end

if __name__ == '__main__':
    # start up api
    app.run(port=5000, debug=True)