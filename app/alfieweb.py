import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'key-replaced-on-docker-build'

from routes import index
