import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__.split('.')[0], instance_relative_config=True)

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from lazaga import blog, projects

    app.register_blueprint(blog.bp)
    app.register_blueprint(projects.bp)

    app.add_url_rule('/', endpoint='index')

    return app
