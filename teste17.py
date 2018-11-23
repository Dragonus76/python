from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
image = Image.open("image.jpeg")
image = ImageOps.flip(image)
image = image.rotate(180)
image.show()
image.save("image.jpeg")