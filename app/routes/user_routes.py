from app.extensions import db
from app.models.user import User
from flask import request, Blueprint, jsonify

user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email").lower()
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"erro": "Algum dado faltando"}), 400

    email_existe = User.query.filter_by(email=email).first()

    if email_existe:
        return jsonify({"erro": "Email já cadastrado"}), 400

    novo_user = User(
        name=name,
        email=email
    )
    novo_user.hash_password(password)

    db.session.add(novo_user)
    db.session.commit()

    return jsonify({"mensagem": "User criado com sucesso"}), 200


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"erro": "Email ou senha não fornecidos"})

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"erro": "Email não cadastrado"}), 401

    if not user.check_pass(password):
        return jsonify({"erro": "Senha incorreta"}), 401

    return jsonify({"mensagem": f"User autenticado - Ola {user.name}"}), 200



@user_bp.route("/user_delete", methods=["PUT"])
def user_delete():
    data = request.get_json()

    email = data.get("email")

    email_existe = User.query.filter_by(email=email).first()

    if not email_existe:
        return jsonify({"erro": "User não existe"}), 400

    db.session.delete(email_existe)
    db.session.commit()

    return jsonify({"mensagem": "Deletado com sucesso"}), 200



@user_bp.route("/user_get", methods=["GET"])
def user_get():

    email_parametro = request.args.get("email")

    id_parametro = request.args.get("id")

    if email_parametro:
        user_busca = User.query.filter_by(email=email_parametro).first()
    elif id_parametro:
        user_busca = User.query.filter_by(id=id_parametro).first()
    else:
        return jsonify({"erro": "Erro de parametro, faltou id ou email"}), 404

    if not user_busca:
        return jsonify({"erro": "User não existe"}), 400

    if user_busca:
        return jsonify(user_busca.to_dict())
