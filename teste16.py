from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
image = Image.open("image.jpeg")
image = ImageOps.flip(image)
image.show()