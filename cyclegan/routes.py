import flask

from cyclegan import app

@app.route('/')
@app.route('/index')
def index():
  return flask.render_template('index.html')