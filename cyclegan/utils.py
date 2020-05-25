import numpy as np
import base64
import PIL.Image
import io


def requestb64_to_image(req: str):
  prefix, _, b64 = req.partition(',')
  buf = io.BytesIO(base64.b64decode(b64))
  return PIL.Image.open(buf)


def numpy_img2b64(img: np.ndarray):
  pil_img = PIL.Image.fromarray((img * 255).astype(np.uint8))
  buffer = io.BytesIO()
  pil_img.save(buffer, format='PNG')
  return base64.b64encode(buffer.getvalue()).decode('utf-8')