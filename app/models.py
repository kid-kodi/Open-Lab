from time import time
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from app import app
import jwt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    equipments = db.relationship('Equipment', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    equipments = db.relationship('Equipment', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category: {}>'.format(self.name)


class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    equipments = db.relationship('Equipment', backref='label', lazy='dynamic')

    def __repr__(self):
        return '<Category: {}>'.format(self.name)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    equipments = db.relationship('Equipment', backref='service', lazy='dynamic')

    def __repr__(self):
        return '<Category: {}>'.format(self.name)


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    label_id = db.Column(db.Integer, db.ForeignKey('label.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    model = db.Column(db.String(120), index=True)
    serial = db.Column(db.String(255))
    name = db.Column(db.String(120), index=True)
    arrived_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    interviews = db.relationship('Interview', backref='equipment', lazy='dynamic')

    def __repr__(self):
        return '<Equipment {}>'.format(self.name)


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester = db.Column(db.String(120), index=True)
    service_id = db.Column(db.String(255))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    reasons = db.Column(db.String(255))
    interviewer = db.Column(db.String(255))
    request_date = db.Column(db.String(120))
    request_time = db.Column(db.String(120))
    status = db.Column(db.Integer)
    actions = db.Column(db.String(255))
    start_date = db.Column(db.String(120))
    end_date = db.Column(db.String(120))

    def __repr__(self):
        return '<Interview {}>'.format(self.name)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester = db.Column(db.String(120), index=True)
    description = db.Column(db.String(255))
    date = db.Column(db.String(120), index=True)
    service = db.Column(db.String(255))
    orderer = db.Column(db.String(255))
    actions = db.Column(db.String(255))

    def __repr__(self):
        return '<Order {}>'.format(self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
