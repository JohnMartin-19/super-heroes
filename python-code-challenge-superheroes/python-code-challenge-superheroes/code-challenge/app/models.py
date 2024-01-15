from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


hero_power_association = db.Table('hero_power_association',
    db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
    db.Column('power_id', db.Integer, db.ForeignKey('power.id')),
    db.Column('Strength', db.String, ('Strong'),('Weak'),('Average'))
)


class Heros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    powers = db.relationship('Power', secondary=hero_power_association, back_populates='heroes')

class Powers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    heroes = db.relationship('Hero', secondary=hero_power_association, back_populates='powers')
    description = db.Column(db.String,('description >= 20'),nullable = False)

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)