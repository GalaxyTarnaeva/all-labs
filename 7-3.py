from PIL import Image,ImageFilter
pic = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg"]
for i in pic:
    with Image.open(i) as img:
        img.load()
        new_img = img.filter(ImageFilter.CONTOUR )
        new_img.save("new_" + i)
