from flask_restful import Resource


class HelloWorldAPI(Resource):
    def get(self):
        return 'hello world from V2.0'
