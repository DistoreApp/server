from flask import Flask


def create_app(config: str = "Production"):
    """Create an instance of the Flask application."""
    app = Flask(__name__)

    app.config.from_object("config.{}".format(config))

    with app.app_context():
        from . import database
        database.init_app()

    from . import store
    from . import view

    app.register_blueprint(store.bp)
    app.register_blueprint(view.bp)

    return app