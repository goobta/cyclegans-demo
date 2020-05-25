from flask import request, render_template
import flask

import numpy as np
import torch

from cyclegan import app
from cyclegan import utils
from cyclegan import models

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/vangoghconvert', methods=['POST'])
def vangoghconvert():
  img = utils.requestb64_to_image(str(request.data))
  return models.predict(img, models.VANGOGH)