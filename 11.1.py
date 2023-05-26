class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):  #
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):  # метод выводит название ресторана и тип кухни
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):  # метод показывает открыт ли ресторан
        print("Ресторан открыт")


newRestaurant = Restaurant(input(),input())  # новый ресторан
print(newRestaurant.restaurant_name)  # выводим название
print(newRestaurant.cuisine_type)  # выводим тип кухни
newRestaurant.describe_restaurant()  # вызов метода
newRestaurant.open_restaurant()  # вызов метода