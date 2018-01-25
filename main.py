from flask import Flask
from v1 import api_v1

app = Flask(__name__)

# Register v1
api_v1.prefix = '/v1'
api_v1.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
