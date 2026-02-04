from flask import Flask
from .config import Config
from .extensions import db
from .routes.user_routes import user_bp
from .routes.games_routes import games_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_bp)
    app.register_blueprint(games_bp)
    db.init_app(app)

    @app.route("/")
    def home():
        return {"mensagem": "Agora vai"}
    return app
