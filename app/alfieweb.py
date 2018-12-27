#from app import app
import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-key'

from routes import index
