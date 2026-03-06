#Soal 3: Buatlah kelas bernama User. Buat atribut bernama first_name dan last_name, 
# lalu buat beberapa atribut lain yang biasanya disimpan dalam profil User. 
# Buat metode bernama describe_user() yang mencetak ringkasan informasi pengguna. 
# Buat metode lain bernama greet_user() yang mencetak salam pribadi kepada user. 
# Buatlah beberapa instance yang mewakili user yang berbeda, dan panggil kedua metode tersebut 
# untuk setiap user.

class User:
    def __init__(self, first_name, last_name, nim, university):
        self.first_name = first_name
        self.last_name = last_name
        self.nim = nim
        self.university = university

    def describe_user(self):
        print(f"Nama       : {self.first_name} {self.last_name}")
        print(f"NIM        : {self.nim}")
        print(f"Universitas: {self.university}")

    def greet_user(self):
        print(f"Haloo, {self.first_name} {self.last_name}! Selamat datang")


user1 = User('Rehan', 'Pratama', '1255', 'UIN Suska Riau')
user1.describe_user()
user1.greet_user()
print()

user2 = User('Maya', 'Lestari', '1255', 'UIN Suska Riau')
user2.describe_user()
user2.greet_user()
print()

user3 = User('Giovani', 'Saputra', '1255', 'UIN Suska Riau')
user3.describe_user()
user3.greet_user() 