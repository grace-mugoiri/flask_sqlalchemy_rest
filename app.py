from distutils.log import debug
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

@app.route('/', methods=["Get"])
def hello():
    return jsonify({'msg': "Hello dunia"})
    
if __name__ == "__main__":
    app.run(debug=True)