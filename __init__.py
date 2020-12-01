from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'hu7hb8uy8o6vdoidw9ng'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app