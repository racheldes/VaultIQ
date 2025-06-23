from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from config import Config
from db import db
import auth

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

#app.register_blueprint(auth.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
