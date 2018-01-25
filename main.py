from flask import Flask
from v1 import v1_blueprint
from v2 import v2_blueprint

app = Flask(__name__)

# Register app v1
app.register_blueprint(v1_blueprint, url_prefix='/v1')

# Register app v2
app.register_blueprint(v2_blueprint, url_prefix='/v2')


if __name__ == '__main__':
    app.run(debug=True)
