#Buatlah program kalkulator sederhana di Python beserta unit testing-nya menggunakan unittest.

class Calculator:

    def tambah(self, x, y):
        return x + y

    def kurang(self, x, y):
        return x - y

    def kali(self, x, y):
        return x * y

    def bagi(self, x, y):
        if y == 0:
            raise ValueError("Tidak bisa membagi dengan nol")
        return x / y