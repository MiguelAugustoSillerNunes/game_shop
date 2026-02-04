from app.extensions import db
'''
Model Games - cria tabela games no banco - armazena preço, versão, console, ativo (Y/N)
Valor Padrão e ativo = Y e de preço = 0
'''


class Games(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)

    id_api = db.Column(db.Integer, nullable=False, unique=True)

    name = db.Column(db.String(100), nullable=False)

    version = db.Column(db.String(20), nullable=False)

    price = db.Column(db.Numeric(5, 2), nullable=False, server_default=db.text("0"), default=0)

    description = db.Column(db.String(300), nullable=False)

    console = db.Column(db.String(15), nullable=False)

    activated = db.Column(db.String(1), nullable=False, server_default=db.text("'Y'"))