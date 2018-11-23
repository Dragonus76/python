from PIL import Image 
from PIL  import ImageFilter
image = Image.open("image.jpeg")
image = image.filter(ImageFilter.DETAIL)
image.show()