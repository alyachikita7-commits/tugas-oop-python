class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} we're open")

    def set_number_served(self, jumlah):
        self.number_served = jumlah

    def increment_number_served(self, tambahan):
        self.number_served += tambahan