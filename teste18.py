from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
image = Image.open("image.jpeg")
image = ImageOps.expand(image,border=50)
image.show()