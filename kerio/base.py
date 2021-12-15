import time

import requests

PRODUCT_CONNECT = 1
PRODUCT_OPERATOR = 2
PRODUCT = {
    1: "CONNECT",
    2: "OPERATOR"
}


class Kerio:
    def __init__(self, product: int, host: str, port: int, prefix_url_login: str, login: str, password: str, automatic_authorization: bool):
        self.product = product
        self.domain = host + ':' + str(port)
        self.prefix_url_login = prefix_url_login
        self.login = login
        self.password = password
        self.account = None
        self.request_id = 1

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
            'last_use': int(time.time())
        }

    def request(self, method, params):
        if int(time.time()) - self.account['last_use'] > 120:
            raise Exception("Просроченные авторизационные данные.")
        result = requests.post("https://" + self.domain + "/admin/api/jsonrpc/",
            verify=False,
            cookies={"SESSION_" + PRODUCT[self.product] + "_WEBADMIN": self.account['session'],
                   "TOKEN_" + PRODUCT[self.product] + "_WEBADMIN": self.account['token']},
            headers={"X-Token": self.account['token'], "Accept": "application/json-rpc"},
            json={
                'jsonrpc': '2.0',
                'id': self.request_id,
                'method': method,
                'params': params})
        self.request_id += 1
        self.account['last_use'] = int(time.time())
        return result.json()
