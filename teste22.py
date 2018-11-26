from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
imageImage = Image.open("image.jpeg")
imageTigre = Image.open("tigre.jpg")
imageTigre = imageTigre.resize((190,178))
imageImage = imageImage.convert("RGBA")
imageTigre = imageTigre.convert("RGBA")
imageImage.alpha_composite(imageTigre, dest=(70,15))
imageImage.save("result.png")
imageImage.show()