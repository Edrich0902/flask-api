from flask import Flask
from flask_restful import Api

#controllers
from resources.controller import Controller

app = Flask(__name__)
api = Api(app)

#routes
api.add_resource(Controller, '/')
#routes end

if __name__ == '__main__':
    # start up api
    app.run(port=5000, debug=True)