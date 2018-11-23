from PIL import Image
from PIL import ImageFilter
image = Image.open("image.jpeg")
image = image.filter(ImageFilter.GaussianBlur(20))
image.show()