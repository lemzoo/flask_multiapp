from flask import Flask


def create_app(config=None):
    """
    Build the app build don't initilize it, useful to get back the default
    app config, correct it, then call ``bootstrap_app`` with the now config
    """

    app = Flask(__name__)
    if config:
        app.config.update(config)
    app.config.from_pyfile('settings.cfg')
    return app


def bootstrap_app(app=None, config=None):
    """
    Create and initilize the sief app
    """

    if not app:
        app = create_app(config)
    elif config:
        app.config.update(config)

    # Register app v1
    from v1 import blueprint as blueprint_v1
    app.register_blueprint(blueprint_v1, url_prefix='/v1')

    # Register app v2
    from v2 import blueprint as blueprint_v2
    app.register_blueprint(blueprint_v2, url_prefix='/v2')

    return app
