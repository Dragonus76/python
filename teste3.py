from PIL import Image
image = Image.open("voitureyeux1.jpg")
w,h = image.size
image = image.crop((100,100,w,h))
image.show()