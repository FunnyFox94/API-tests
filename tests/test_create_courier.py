import sprint_7.utils.test_literals as json
import sprint_7.src.api_client as api


class TestCreateCourier:
    def test_create_courier(self, new_random_courier_data):
        response = api.create_user(new_random_courier_data)
        assert response.json() == json.SUCCESS_CREATING_COURIER
        assert response.status_code == 201

    def test_duplicate_courier(self, new_random_courier_data):
        response = api.create_user(new_random_courier_data)
        response_duplicate = api.create_user(new_random_courier_data)
        assert response_duplicate.status_code == 409
        assert response_duplicate.json() == json.ALREADY_EXIST_COURIER

    def test_create_courier_fails_without_required_parameter(self, generate_courier_without_required_parameter):
        response = api.create_user(generate_courier_without_required_parameter)
        assert response.status_code == 400
        assert response.json() == json.MISSING_LOGIN_OR_PASSWORD

