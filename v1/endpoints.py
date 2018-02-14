from core import CoreResource, NoAuthCoreResource


class HelloWorldApiAuthResource(CoreResource):
    def get(self):
        return 'hello world from V1.0 with authentication'


class HelloWorldApiNoAuthResource(NoAuthCoreResource):
    def get(self):
        return 'hello world from V1.0 without authentication'
