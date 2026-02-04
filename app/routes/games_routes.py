from app.extensions import db
from app.models.games import Games
from flask import request, Blueprint, jsonify


games_bp = Blueprint("games", __name__)


@games_bp.route("/games-register", methods=["POST"])
def games_register():

    data = request.get_json()

    id_api = data.get("id_api")
    name = data.get("name")
    version = data.get("version")
    price = data.get("price", 0)
    description = data.get("description")
    console = data.get("console")
    activated = data.get("activated", "Y")

    if not id_api or not name or not version or not description or not console:
        return jsonify({"erro": "Algum dado faltante."}), 400

    game = Games.query.filter_by(id_api=id_api).first()

    if game:
        return jsonify({"erro": f"Jogo ja existe {game.name}"})

    novo_game = Games(
            id_api=id_api,
            name=name,
            version=version,
            price=price,
            description=description,
            console=console,
            activated=activated
    )

    db.session.add(novo_game)   
    db.session.commit()

    return jsonify({"mensagem": f"Game cadastrado com sucesso {novo_game.name}"}), 200


@games_bp.route("/game_update_status", methods=["POST"])
def game_delete():
    data = request.get_json()

    id = data.get("id")
    activated = data.get("activated")

    if not id or not activated:
        return jsonify({"erro": "Necessaio id e estado Y/N"}), 400

    game_id = Games.query.filter_by(id=id).first()

    if not game_id:
        return jsonify({"erro": "Jogo não existe"}), 400

    Games.query.filter_by(id=id).update({
        "activated": activated.upper()
    })

    db.session.commit()
    if activated.upper() == "Y":
        return jsonify({"mensagem": f"Jogo ativado com sucesso {game_id.name}"}), 200
    else:
        return jsonify({"mensagem": f"Jogo desativado com sucesso {game_id.name}"}), 200
