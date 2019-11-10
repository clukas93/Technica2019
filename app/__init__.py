from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

#an instance of class Flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

from app import routes