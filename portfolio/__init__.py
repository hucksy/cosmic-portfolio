from flask import Flask


def init_app():
    """do the thing Julee!"""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    with app.app_context():
        from .routes import main_bp

        app.register_blueprint(main_bp)

        return app
