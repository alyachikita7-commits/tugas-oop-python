#Bungkus kode program dari Latihan dan Tugas (4-a) nomor 2 dalam perulangan while agar pengguna dapat 
#terus memasukkan angka,meskipun mereka membuat kesalahan dan memasukkan teks sebagai pengganti angka.

while True:
    angka1 = input("Masukkan angka pertama: ")
    if angka1 == 'selesai':
        break

    angka2 = input("Masukkan angka kedua: ")
    if angka2 == 'selesai':
        break

    try:
        hasil = float(angka1) + float(angka2)
        print("Hasil penjumlahan:", hasil)
    except ValueError:
        print("Input harus berupa angka!")