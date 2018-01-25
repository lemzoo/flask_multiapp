from flask import Blueprint
from flask.ext.restplus import Api

from v1.endpoints import HelloWorldAPI

blueprint = Blueprint('version 1', __name__)

api = Api(blueprint)
api.add_resource(HelloWorldAPI, '/hello')
