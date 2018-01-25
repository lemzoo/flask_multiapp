from flask import Blueprint
from flask.ext.restplus import Api

from v2.endpoints import RouteAPI

v2_blueprint = Blueprint('v2', __name__)

api_v2 = Api(v2_blueprint)
api_v2.add_resource(RouteAPI, '/routes')
