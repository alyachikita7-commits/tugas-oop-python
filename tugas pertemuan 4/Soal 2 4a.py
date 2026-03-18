#Tulis perulangan while yang meminta pengguna untuk memasukkan nama mereka. 
#kumpulkan semua nama yang dimasukkan, lalu tulis nama-nama ini ke dalam file bernama guest_book.txt.
#Pastikan setiap entri muncul di baris baru dalam file.
daftar_nama = []

while True:
    nama = input("Masukkan nama tamu: ")

    if nama == 'selesai':
        break

    daftar_nama.append(nama)

with open("guest_book.txt", "a") as file:
    for nama in daftar_nama:
        file.write(nama + "\n")

print("Semua nama tamu berhasil disimpan ke guest_book.txt!")