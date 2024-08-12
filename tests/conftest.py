import pytest

import sprint_7.utils.generators as generate


@pytest.fixture()
def courier_generating():
    courier_data = generate.register_new_courier_and_return_login_password()
    return courier_data


@pytest.fixture()
def new_courier_data():  # создаю юзера руками, что бы проверить регистрацию
    return {
        "login": f"{generate.generate_random_string()}",
        "password": f"{generate.generate_random_string()}",
        "firstName": f"{generate.generate_random_string()}"
    }
