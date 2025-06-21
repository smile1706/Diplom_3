from faker import Faker

faker = Faker()

def generate_registration_data():
    email = faker.email(domain='yndex.ru')
    password = faker.password(length=6)
    name = faker.name()
    return email, password, name  # Возвращаем кортеж

def register_body(email, password, name):
    return {
        "email": email,
        "password": password,
        "name": name
    }

def generate_auth_header(access_token):
    return {
        "Authorization": access_token
    }

class Data:
    path_index = 2
    ingredient_index = 3

