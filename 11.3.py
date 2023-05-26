class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):  # + рейтинг
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)
        print("Rating:", self.rating)

    def update_rating(self, new_rating):  # метод нового рейтинга
        self.rating = new_rating
restaurant = Restaurant("СушиШоп", "Азиатская", 3.7)
restaurant.describe_restaurant()
restaurant.update_rating(4.2)
restaurant.describe_restaurant()