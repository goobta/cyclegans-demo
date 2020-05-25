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
  img = utils.requestb64_to_image(str(request.data)).convert('RGB')
  img_numpy = np.array(img)[np.newaxis, :]
  img_torch = torch.from_numpy(img_numpy)
  img_final = img_torch.permute([0, 3, 1, 2])
  batch = {'A': img_final, 'A_paths': None}
  return 'test'