from flask.ext.restplus import Resource


class RouteAPI(Resource):
    def get(self):
        return 'hello world from V2.0'
