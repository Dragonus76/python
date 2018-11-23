from PIL import Image
from PIL import ImageFilter
image = Image.open("tigre.jpg")
image = image.filter(ImageFilter.SMOOTH_MORE)

image.show()
