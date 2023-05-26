from PIL import Image
n = "123.jpg"
with Image.open(n) as img:
    img.load()
img_crop=img.crop((200, 200, 1600, 1600))
img_crop.save('112233.png', quality=95)