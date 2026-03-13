from restaurant import Restaurant

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


#Penambahan atribut
from restaurant import Restaurant

resto1 = Restaurant("Bibimbap", "Korea")
resto2 = Restaurant("Dimsum", "China")
resto3 = Restaurant("Tempura", "Jepang")

# Resto1
print(f"Selamat datang di restaurant {resto1.restaurant_name}.")
print(f"Kami menyajikan jenis masakan {resto1.cuisine_type}.")
print()

resto1.describe_restaurant()
resto1.open_restaurant()

print("Jumlah pelanggan awal :", resto1.number_served)

resto1.set_number_served(36)
print("Setelah set           :", resto1.number_served)

resto1.increment_number_served(4)
print("Setelah increment     :", resto1.number_served)
print("\n")

#Resto2
print(f"Selamat datang di restaurant {resto2.restaurant_name}.")
print(f"Kami menyajikan jenis masakan {resto2.cuisine_type}.")
print()

resto2.describe_restaurant()
resto2.open_restaurant()

print("Jumlah pelanggan awal :", resto2.number_served)

resto2.set_number_served(40)
print("Setelah set           :", resto2.number_served)

resto2.increment_number_served(5)
print("Setelah increment     :", resto2.number_served)
print("\n")

#resto 3
print(f"Selamat datang di restaurant {resto3.restaurant_name}.")
print(f"Kami menyajikan jenis masakan {resto3.cuisine_type}.")
print()

resto3.describe_restaurant()
resto3.open_restaurant()

print("Jumlah pelanggan awal :", resto3.number_served)

resto3.set_number_served(46)
print("Setelah set           :", resto3.number_served)

resto3.increment_number_served(4)
print("Setelah increment     :", resto3.number_served)
print("\n")


