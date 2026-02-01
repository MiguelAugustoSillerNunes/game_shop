from app.extensions import db
from app.models.user import User
from flask import request, Blueprint, jsonify

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or email or password:
        return jsonify({"erro": "Algum dado faltando"}), 400

    email_existe = User.query.filter(email=email).first()

    if email_existe:
        return jsonify({"erro": "Email já cadastrado"}), 400

    novo_user = User(
        name=name,
        email=email,
        password=password
    )

    db.session.add(novo_user)
    db.commit()

    return jsonify({"mensagem": "User criado com sucesso"}), 200
