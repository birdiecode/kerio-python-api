from .base import Kerio, PRODUCT_OPERATOR


class KerioOperator(Kerio):
    def __init__(self, host, login, password, port=4021, authorization=True):
        super(KerioOperator, self).__init__(PRODUCT_OPERATOR, host, port, '/dologin.php', login, password, authorization)

    def getUsers(self, start=0, limit=-1):
        return self.request("Users.get", {"query": {"start": start, "limit": limit, "orderBy": [{"columnName": "EXTENSIONS", "direction": "Asc"}]}})['result']
