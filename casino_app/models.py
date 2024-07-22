# File: casino_app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Exclusion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    street = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zip = db.Column(db.String(10), nullable=False)
    reason = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)
    exclusion_authority = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    id_type = db.Column(db.String(20), nullable=False)
    id_number = db.Column(db.String(20), nullable=False, unique=True)

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exclusions.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()

def add_exclusion(data):
    new_exclusion = Exclusion(**data)
    db.session.add(new_exclusion)
    db.session.commit()

def get_exclusion_by_id_number(id_number):
    return Exclusion.query.filter_by(id_number=id_number).first()

def view_exclusions():
    return Exclusion.query.all()
