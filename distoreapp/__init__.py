from flask import Flask


def create_app(config):
    """Create an instance of the Flask application."""
    app = Flask(__name__)

    app.config.from_object(config)

    with app.app_context():
        from . import database
        database.init_app()

    from . import api
    from . import view
    from . import static

    app.register_blueprint(api.bp, url_prefix="/api")
    app.register_blueprint(view.bp)
    app.register_blueprint(static.bp)

    return app