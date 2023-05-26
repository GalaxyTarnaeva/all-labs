class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):  # вызов метода, если открыт
        print("The restaurant", self.restaurant_name, "is now open.")


italian_restaurant = Restaurant("Пиццерия", "Итальянская")
chinese_restaurant = Restaurant("Евразия", "Европейская")
mexican_restaurant = Restaurant("СушиШоп", "Азиатская")

italian_restaurant.describe_restaurant()
chinese_restaurant.describe_restaurant()
mexican_restaurant.describe_restaurant()