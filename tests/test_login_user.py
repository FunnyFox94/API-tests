import practicum.sprint_7.src.api_client as api
import practicum.sprint_7.utils.test_literals as json


class TestLoginUser:
    def test_login_courier_positive_check(self, registered_courier_credentials):
        response = api.login_user(registered_courier_credentials)
        id_in_response = response.json().get('id')
        assert response.status_code == 200
        assert isinstance(id_in_response, int) == True

    def test_login_courier_missing_password(self, generate_courier_without_password):
        response = api.login_user(generate_courier_without_password)
        assert response.status_code == 400
        assert response.json() == json.MISSING_PASSWORD_ON_LOGIN

    def test_login_courier_wrong_password(self, registered_courier_credentials):
        registered_courier_credentials['password'] = 123456
        response = api.login_user(registered_courier_credentials)
        assert response.status_code == 404
        assert response.json() == json.WRONG_PASSWORD
