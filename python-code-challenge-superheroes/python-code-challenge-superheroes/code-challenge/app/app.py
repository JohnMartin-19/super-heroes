#!/usr/bin/env python3
from flask import SQLAlchemy
from flask import Flask, make_response,jsonify,Response
from flask import Migrate

from models import db,heros,Powers, hero_power_association

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/heros', methods=['GET'])
def heros():
    heros = heros.query.all()
    return ''


if __name__ == '__main__':
    app.run(port=5555)
