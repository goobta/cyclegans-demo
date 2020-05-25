import numpy as np
import base64
import PIL.Image
import io


def requestb64_to_image(req: str) -> PIL.Image:
  """Convert a flask request into a PIL image 

  Args:
    req (str): flask request body

  Returns:
    PIL.Image: image decoded from the base64 request
  """
  prefix, _, b64 = req.partition(',')
  buf = io.BytesIO(base64.b64decode(b64))
  return PIL.Image.open(buf)


def numpy_img2b64req(img: np.ndarray) -> str:
  """Convert numpy image into base64 encoded image request body

  Args:
    img (np.ndarray): image array. should be of shape (width, height, channels)

  Returns:
    str: base64 encoded image body
  """
  amin = np.amin(img)
  amax = np.amax(img)
  norm = (255 * (img - amin) / (amax - amin)).astype(np.uint8)

  pil_img = PIL.Image.fromarray(norm)
  buffer = io.BytesIO()
  pil_img.save(buffer, format='PNG')
  return 'data:image/png;base64,' + \
         base64.b64encode(buffer.getvalue()).decode('utf-8')