from PIL import Image
from PIL import ImageFilter
image = Image.open("tigre.jpg")
image = image.filter(ImageFilter.SHARPEN)
image.show()
