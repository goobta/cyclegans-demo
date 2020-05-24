import base64
import PIL
import io


def requestb64_to_image(req: str):
  prefix, _, b64 = req.partition(',')
  buf = io.BytesIO(base64.b64decode(b64))
  return PIL.Image.open(buf)