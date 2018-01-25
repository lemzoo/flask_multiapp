from flask.ext.restplus import Resource


class HelloWorldAPI(Resource):
    def get(self):
        return 'hello world from V1.0'
