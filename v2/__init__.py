from flask import Blueprint
from flask.ext.restplus import Api

from v2.endpoints import HelloWorldAPI

blueprint = Blueprint('version 2', __name__)

api = Api(blueprint)
api.add_resource(HelloWorldAPI, '/hello')
