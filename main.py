from flask import Flask,jsonify,request
# from flask_sqlalchemy import SQLAlchemy
import datetime
# from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

\

@app.route('/',methods=['GET'])
def home():
    return jsonify({'message':'Hello World'})


