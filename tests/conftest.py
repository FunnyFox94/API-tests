import pytest

import sprint_7.utils.generators as generate


@pytest.fixture()
def courier_generating():
    courier_data = generate.register_new_courier_and_return_login_password()
    return courier_data


@pytest.fixture()
def new_random_courier_data():  # создаю юзера руками, что бы проверить регистрацию
    new_courier = generate.register_new_courier_and_return_login_password()
    return new_courier


@pytest.fixture()
def generate_courier_without_required_parameter():
    return {
        "login": f"{generate.generate_random_string()}",
        "firstName": f"{generate.generate_random_string()}"
    }
