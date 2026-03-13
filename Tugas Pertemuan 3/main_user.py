from user import User

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
print()

from user import User

user1 = User('Rehan', 'Pratama', '1255', 'UIN Suska Riau')

user1.describe_user()
user1.greet_user()
print()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login attempts :", user1.login_attempts)

user1.reset_login_attempts()

print("Setelah reset  :", user1.login_attempts)