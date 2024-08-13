import requests
import random
import string
import sprint_7.utils.urls as url


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(url.REGISTER_URL, json=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в словарь логин и пароль курьера
    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "first_name": first_name
        }


def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_credentials_for_login(credentials):
    return credentials['login'], credentials['password']


def user_login(credentials):
    login, password = generate_credentials_for_login(credentials)
    payload = {
        "login": login,
        "password": password
    }

    response = requests.post(url.LOGIN_URL, json=payload)
    if response.status_code == 200:
        return {
            "login": login,
            "password": password
        }
