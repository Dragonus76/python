from PIL import Image 
from PIL import ImageFilter
image = Image.open("computer.png")
image = image.filter(ImageFilter.EDGE_ENHANCE)

image.show()