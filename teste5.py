from PIL import Image
from PIL import ImageFilter
image = Image.open("image.jpeg")
image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

image.show()
