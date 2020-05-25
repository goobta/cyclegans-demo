from .test_model import TestModel

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
  'load_size': 256,
  'crop_size': 256,
  'max_dataset_size': math.inf,
  'preprocess': 'resize_and_crop',
  'no_flip': True,
  'display_winsize': 256,
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

VANGOGH=vangogh_model()