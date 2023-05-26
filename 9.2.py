import os
from PIL import Image, ImageFilter
print("Мероприятие: \n"
        "1.Детализировать\n"
        "2.Улучшить резкость\n"
        "3.Найти контуры\n"
        "4.Тисневое изоб")
a = int(input())
directory = os.listdir(os.getcwd() + "\Изображения для обработки")
print(directory)
eff = [ImageFilter.DETAIL, ImageFilter.SHARPEN, ImageFilter.CONTOUR, ImageFilter.EMBOSS]
for file in directory:
    os.chdir(r"C:\Users\79143\PycharmProjects\pythonProject\Изображения для обработки")
    with Image.open(file) as img:
        os.chdir(r"C:\Users\79143\PycharmProjects\pythonProject\Обработанные картинки")
        img.load()
        new_img = img.filter(eff[a - 1])
        new_img.save(file)