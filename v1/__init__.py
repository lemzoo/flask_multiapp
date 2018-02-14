from flask import Blueprint
from flask.ext.restplus import Api

from v1.endpoints import HelloWorldApiAuthResource
from v1.endpoints import HelloWorldApiNoAuthResource

blueprint = Blueprint('version 1', __name__)

api = Api(blueprint)

api.add_resource(HelloWorldApiAuthResource, '/hello-auth')
api.add_resource(HelloWorldApiNoAuthResource, '/hello-no-auth')
