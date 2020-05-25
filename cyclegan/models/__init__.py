from .test_model import TestModel
from . import data

import matplotlib.pyplot as plt

import PIL.Image
import argparse
import math

default_opts = {
  'dataroot': '',
  'name': '',
  'gpu_ids': [],
  'checkpoints_dir': '',
  'model': 'test',
  'input_nc': 3,
  'output_nc': 3,
  'ngf': 64,
  'ndf': 64,
  'netD': 'basic',
  'netG': 'resnet_9blocks',
  'n_layers_D': 3,
  'norm': 'instance',
  'init_type': 'normal',
  'init_gain': 0.02,
  'no_dropout': True,
  'dataset_mode': 'single',
  'direction': 'AtoB',
  'serial_batches': True,
  'num_threads': 0,
  'batch_size': 1,
  'load_size': 128,
  'crop_size': 128,
  'max_dataset_size': math.inf,
  'preprocess': 'resize_and_crop',
  'no_flip': True,
  'display_winsize': 128,
  'epoch': 'latest',
  'load_iter': 0,
  'verbose': False,
  'suffix': '',
  'results_dir': './results/',
  'aspect_ratio': 1.0,
  'phase': 'test',
  'eval': False,
  'num_test': 50,
  'model_suffix': '',
  'isTrain': False,
  'display_id': -1
}


def vangogh_model():
  opts = default_opts.copy()
  opts['checkpoints_dir'] = 'bin/'
  opt = argparse.Namespace(**opts)
  model = TestModel(opt)
  model.setup(opt)
  return model

def _get_transforms():
  opt = argparse.Namespace(**default_opts)
  return data.get_transform(opt, grayscale=False)


VANGOGH=vangogh_model()
_TRANFORM = _get_transforms()


def predict(img: PIL.Image, model):
  clean_img = _TRANFORM(img.convert('RGB'))
  batched = clean_img.unsqueeze(0)
  inpt = {'A': batched, 'A_paths': None}

  model.set_input(inpt)
  model.test()
  vis = model.get_current_visuals()

  fake = vis['fake'].squeeze().permute(1, 2, 0)
  return fake.numpy()