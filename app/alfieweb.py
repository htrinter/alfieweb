import os
import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

from routes import index
