import pytest
import practicum.sprint_7.utils.generators as generate


@pytest.fixture()
def new_random_courier_data():  # создаю юзера руками, что бы проверить регистрацию
    new_courier = generate.register_new_courier_and_return_login_password()
    return new_courier


@pytest.fixture()
def generate_courier_without_password():
    return generate.generate_courier_data(include_password=False, include_name=False)


@pytest.fixture()
def new_courier_data():  # надо заменить фиксутру на более красивую
    return generate.generate_courier_data()


@pytest.fixture()
def registered_courier_credentials():
    return generate.user_login()

