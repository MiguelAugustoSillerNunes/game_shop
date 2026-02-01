from app import create_app
from app.extensions import db
# from app.models.user import User

app = create_app()

with app.app_context():
    db.create_all()
