from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageChops
image1 = Image.open("image.jpeg")
image2 = Image.open("tigre.jpg")
# Attention : les images doivent avoir la meme taille et le meme mode
image1 = image1.convert("RGB")
image1 = image1.resize((300,300))
image2 = image2.convert("RGB")
image2 = image2.resize((300,300))
image3 = Image.blend(image1,image2,0.5)
image3 = ImageChops.darker(image1,image2)
image3.show()