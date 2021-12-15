import time

import requests

PRODUCT_CONNECT = 1
PRODUCT = {
    1: "CONNECT"
}


class Kerio:
    def __init__(self, product: int, host: str, port: int, prefix_url_login: str, login: str, password: str, automatic_authorization: bool):
        self.product = product
        self.domain = host + ':' + str(port)
        self.prefix_url_login = prefix_url_login
        self.login = login
        self.password = password
        self.account = None

        if automatic_authorization: self.authorization()

    def authorization(self):
        result = requests.post(
            "https://" + self.domain + "/admin" + self.prefix_url_login,
            data="kerio_username=" + self.login + "&kerio_password=" + self.password,
            headers={"Content-Type": "application/x-www-form-urlencoded"}, verify=False,
            allow_redirects=False)

        self.account = {
            'session': result.cookies["SESSION_" + PRODUCT[self.product] + "_WEBADMIN"],
            'token': result.cookies["TOKEN_" + PRODUCT[self.product] + "_WEBADMIN"],
            'creation': int(time.time())
        }