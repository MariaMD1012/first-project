from faker import Faker
import random


fake = Faker("en_US")

# generation login, email, password
fake_login = fake.first_name()
a = random.randint(100, 300)
fake_email = f'{fake_login}{a}@exmaple.ru'
fake_password = fake_login + '_123456'

# Incorrect password
incorrect_password = 'a1234'

# Static login details
login = 'Maria'
email = 'maria.rthefam@yandex.ru'
password = '123456'
