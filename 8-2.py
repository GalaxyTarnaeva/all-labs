from PIL import Image
przd = {1:"рождество.jpg", 2:"хеллоуин.jpg", 3:"день рождения.jpg"}
print()

a=int(input("Мероприятие: \n"
            "1.Рождество\n"
            "2.Хэллоуин\n"
            "3.День рождения\n"))
name= przd[a]
with Image.open(name) as img:
    img.load()
img.show()
