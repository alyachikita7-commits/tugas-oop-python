# Soal 1: Buat kelas bernama Restaurant. Metode __init__() untuk Restaurant harus
# menyimpan dua atribut: nama restoran (restaurant_name) dan jenis masakan (cuisine_type).
# Buatlah metode bernama describe_restaurant() yang mencetak kedua informasi ini,
# dan metode bernama open_restaurant() yang mencetak pesan yang menunjukkan bahwa
# restoran tersebut buka. Buat instance bernama restaurant dari kelas anda.
# Cetak kedua atribut tersebut secara terpisah, lalu panggil kedua metode tersebut.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} we're open")


restaurant = Restaurant('Bibimbap', 'Korea')

print(f"Selamat datang di restaurant {restaurant.restaurant_name}.")
print(f"kami menyajikan jenis masakan {restaurant.cuisine_type}.")
print()

restaurant.describe_restaurant()
restaurant.open_restaurant()