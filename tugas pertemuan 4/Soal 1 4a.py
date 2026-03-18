#tulis program yang meminta pengguna untuk memasukkan nama mereka. Ketika mereka merespons, tulis nama
# mereka ke dalam file bernama guest.txt

name = input("Masukkan nama Anda: ")
with open("guest.txt", "w") as file:
    file.write(name + "\n")