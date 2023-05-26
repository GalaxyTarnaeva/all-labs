from PIL import Image
pic = "стикер7.png"
with Image.open(pic) as img_water:
    img_water.load()
img_water =Image.open(pic)
img_water=img_water.resize((img_water.width*3,img_water.height*3))
pic1 = "вода.png"
with Image.open(pic1) as img:
    img.load()
img.paste(img_water,(10,10),img_water)
img.save("водяной.png")
