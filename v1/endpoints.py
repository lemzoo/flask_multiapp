from flask.ext.restplus import Resource


class RouteAPI(Resource):
    def get(self):
        "Get the resource by the given id"
        return 'hello world from V1.0'
