from flask import Flask
from v1 import blueprint as blueprint_v1
from v2 import blueprint as blueprint_v2

app = Flask(__name__)

# Register app v1
app.register_blueprint(blueprint_v1, url_prefix='/v1')

# Register app v2
app.register_blueprint(blueprint_v2, url_prefix='/v2')


if __name__ == '__main__':
    app.run(debug=True)
