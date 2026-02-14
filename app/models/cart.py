from app.extensions import db


class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))

    quantity = db.Column(db.Integer, nullable=False, server_default=db.text("0"), default=0)

    price_at_time = db.Column(db.Numeric(5, 2), nullable=False)

    user = db.relationship("User")

    game = db.relationship("Games")