from PIL import Image, ImageDraw, ImageFont
a = input()
image = Image.open("день рождения.jpg")
tx = a + ", Поздравляю!"
font = ImageFont.truetype("arial.ttf", 150)
drawer = ImageDraw.Draw(image)
drawer.text((1, 1), tx , font=font, fill="purple")
image.save('new_img.jpg')
image.show()