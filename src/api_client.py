import requests
import sprint_7.utils.urls as url
import sprint_7.utils.generators as generate


def create_user(data):
    return requests.post(url.REGISTER_URL, json=data)


def login_user(data):
    creds = generate.generate_credentials_for_login(create_user)
    return requests.post(url.LOGIN_URL, json=data)


def delete_user(login_pass):
    pass
