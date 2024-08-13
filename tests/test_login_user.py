import requests
import sprint_7.utils.urls as url
import sprint_7.utils.test_literals as json
import sprint_7.src.api_client as api


class TestLoginUser:
    def test_login_courier_positive_check(self, courier_generating):
        response = api.login_user()
