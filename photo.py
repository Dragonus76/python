from PIL import Image
image = Image.open("voitureyeux1.jpg")
image = image.convert("RGB") 
image = image.resize((200,300))
image = image.rotate(90)
image.show()
