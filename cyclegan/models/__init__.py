# A HUGE hack to get the cyclegan model working
from .test_model import TestModel
from . import data

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
  'load_size': 256,                     # Modify this value to change resolution
  'crop_size': 256,                     # Modify this value to change resolution
  'max_dataset_size': math.inf,
  'preprocess': 'resize_and_crop',
  'no_flip': True,
  'display_winsize': 256,               # Modify this value to change resolution
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


def _get_transforms():
  """Get a function to preprocess the images

  Returns:
    torch.Compose: preprocessing pipeline based on default_args
  """
  opt = argparse.Namespace(**default_opts)
  return data.get_transform(opt, grayscale=False)


def vangogh_model():
  """Create the vangogh generator

  Returns:
    base_model.BaseModel: vangogh model
  """
  opts = default_opts.copy()
  opts['checkpoints_dir'] = 'bin/models/vangogh/'
  opt = argparse.Namespace(**opts)

  model = TestModel(opt)
  model.setup(opt)
  return model


VANGOGH=vangogh_model()
_TRANFORM = _get_transforms()


def predict(img: PIL.Image, model):
  """Perform style transfer on image with the desired model.

  Args:
    img (PIL.Image): real image
    model (base_model.BaseModel): model to use

  Returns:
    np.ndarray: fake image in the shape of (width, height, channels)
  """
  # Preprocess image
  clean_img = _TRANFORM(img.convert('RGB'))

  # Put into the (batch_count, width, height, channels)
  batched = clean_img.unsqueeze(0)

  # Put into the batch format that the default model uses. Put in dummy 
  # placeholders for actual file paths as everything is done in cache.
  inpt = {'A': batched, 'A_paths': None}

  # Generate predictions
  model.set_input(inpt)
  model.test()
  vis = model.get_current_visuals()

  # Get the results and reshape to (width, height, channels)
  fake = vis['fake'].squeeze().permute(1, 2, 0)
  return fake.numpy()