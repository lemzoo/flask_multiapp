from flask.ext.restplus import Api
from v1.endpoints import RouteAPI


api_v1 = Api()
api_v1.add_resource(RouteAPI, '/routes')
