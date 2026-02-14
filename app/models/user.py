from app.extensions import db
import bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

    create_date = db.Column(db.DateTime, server_default=db.func.now())

    def hash_password(self, password_digitada):
        hash_pass = bcrypt.hashpw(
            password_digitada.encode('utf-8'),
            bcrypt.gensalt()
        )
        self.password = hash_pass.decode('utf-8')

    def check_pass(self, password_digitada):
        return bcrypt.checkpw(
            password_digitada.encode('utf-8'),
            self.password.encode('utf-8')
        )

    def to_dict(self):
        resultado = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "create_date": self.create_date
        }
        return resultado