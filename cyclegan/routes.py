from flask import request, render_template
import flask

import matplotlib.pyplot as plt

from cyclegan import app
from cyclegan import utils

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/vangoghconvert', methods=['POST'])
def vangoghconvert():
  plt.imshow(utils.requestb64_to_image(str(request.data)))
  plt.show()
  return 'test'