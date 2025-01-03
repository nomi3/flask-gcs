import logging

from flask import Flask

from src.actions import bucket_actions_bp
from src.config import Config


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(bucket_actions_bp)

    @app.route("/")
    def hello():
        return "hello"

    if __name__ != "__main__":
        gunicorn_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    return app