# Soal 2: Dari soal nomor 1, buatlah 3 instance berbeda dari kelas tersebut,
# dan panggil describe_restaurant() untuk setiap instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} we're open")


resto1 = Restaurant('Bibimbap', 'Korea')
print(f"Selamat datang di restaurant {resto1.restaurant_name}.")
print(f"Kami menyajikan jenis masakan {resto1.cuisine_type}.")
print()
resto1.describe_restaurant()
resto1.open_restaurant()
print()

resto2 = Restaurant('Dimsum', 'China')
print(f"Selamat datang di restaurant {resto2.restaurant_name}.")
print(f"Kami menyajikan jenis masakan {resto2.cuisine_type}.")
print()
resto2.describe_restaurant()
resto2.open_restaurant()
print()

resto3 = Restaurant('Tempura', 'Jepang')
print(f"Selamat datang di restaurant {resto3.restaurant_name}.")
print(f"Kami menyajikan jenis masakan {resto3.cuisine_type}.")
print()
resto3.describe_restaurant()
resto3.open_restaurant()
