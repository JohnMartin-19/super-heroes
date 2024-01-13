#!/usr/bin/env python3
from flask import SQLAlchemy
from flask import Flask, make_response
from flask import Migrate

from models import db,Hero

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''


if __name__ == '__main__':
    app.run(port=5555)
