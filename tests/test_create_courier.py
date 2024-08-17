import allure

import practicum.sprint_7.utils.test_literals as json
import practicum.sprint_7.src.api_client as api


@allure.suite('Тесты на создание курьера')
class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Генерим курьера, передаем его креды в запрос и проверяем ответ')
    def test_create_courier(self, new_courier_data):
        response = api.create_user(new_courier_data)
        assert response.json() == json.SUCCESS_CREATING_COURIER
        assert response.status_code == 201

    @allure.title('Создание дубликата курьера')
    @allure.description('Генерим курьера и два раза отправляем запрос на его создание')
    def test_duplicate_courier(self, new_random_courier_data):
        response = api.create_user(new_random_courier_data)
        response_duplicate = api.create_user(new_random_courier_data)
        assert response_duplicate.status_code == 409
        assert response_duplicate.json() == json.ALREADY_EXIST_COURIER

    @allure.title('Создание курьера с пустым паролем')
    @allure.title('Генерируем курьера и НЕ подставляем в запрос его создания пароль, после отправки проверяем ошибку')
    def test_create_courier_fails_without_required_parameter(self, generate_courier_without_password):
        response = api.create_user(generate_courier_without_password)
        assert response.status_code == 400
        assert response.json() == json.MISSING_LOGIN_OR_PASSWORD_ON_REGISTRATION
