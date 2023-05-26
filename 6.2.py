"стикер4.png"
from PIL import Image
pic = "стикер4.png"
with Image.open(pic) as img:
    img.load()
new_img = img.resize((img.width//3,img.height//3))
new_img.save("stik.png")
c_img = img.transpose(Image.FLIP_TOP_BOTTOM)
c_img.save("fliptop.png")
c_img = img.transpose(Image.FLIP_LEFT_RIGHT)
c_img.save("flipleft.png")
pic1 = "stik.png"
with Image.open(pic1) as img1:
    img1.load()

