from PIL import Image
image = Image.open("voitureyeux1.jpg")
image2 = Image.open("computer.png")
image2 = image2.resize((200,200))
image.paste(image2,box=(200,200))
image.show()


