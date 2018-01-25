from flask import Blueprint
from flask.ext.restplus import Api

from v1.endpoints import RouteAPI

v1_blueprint = Blueprint('v1', __name__)

api_v1 = Api(v1_blueprint)
api_v1.add_resource(RouteAPI, '/routes')
