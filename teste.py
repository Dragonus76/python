from PIL import Image
from PIL import ImageFilter
image = Image.open("voitureyeux1.jpg")
image = image.filter(ImageFilter.CONTOUR)


image.show()