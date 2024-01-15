#!/usr/bin/env python3
from flask import SQLAlchemy
from flask import Flask, make_response,jsonify,request
from flask import Migrate

from models import db,heros,Powers, hero_power_association

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/heros', methods=['GET'])
def heros(heros):
    if request.method == 'GET':
        heros = heros.query.all()

        return make_response(
            jsonify([heros.to_dict() for hero in heros]),
            200,
        )

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    ) 


@app.route('/heros/id', methods = ['GET'])
def get_hero_by_id(id):
    id = int(request.args.get('id'))
    if request.method == 'GET':
        results = heros.query.filter_by(id=id).first()
    
        return make_response(
            jsonify([results.to_dict() for result in results ]), 200
        )


if __name__ == '__main__':
    app.run(port=5555)
