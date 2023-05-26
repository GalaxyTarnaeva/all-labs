from PIL import Image
ca = "стикер4.png"
with Image.open(ca) as img:
    img.load()
img.show()
width, hight = img.size
format = img.format
mode = img.mode
print("Ширина изображения", width)
print("Высота изображения", hight)
print("Формат изображения", format)
print("Цветовая модель", mode)