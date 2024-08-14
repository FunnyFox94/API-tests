import requests
import practicum.sprint_7.utils.urls as url
import allure


@allure.step('Выполнение запроса создания курьера POST api/v1/courier')
def create_user(data):
    return requests.post(url.REGISTER_URL, json=data)


@allure.step('Выполнение запроса логина курьера POST /api/v1/courier/login')
def login_user(data):
    return requests.post(url.LOGIN_URL, json=data)


@allure.step('Выполнение запроса создания заказа POST /api/v1/orders')
def create_order(data):
    return requests.post(url.ORDERS, json=data)


@allure.step('Выполнение запроса заказов курьера GET /api/v1/orders')
def get_order():
    return requests.get(url.ORDERS)
