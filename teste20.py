from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
image = Image.open("image.jpeg")
image = ImageOps.solarize(image, threshold=128)
image.show()