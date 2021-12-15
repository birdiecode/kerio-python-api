from .base import Kerio, PRODUCT_CONNECT


class KerioConnect(Kerio):
    def __init__(self, host, login, password, port=4040, authorization=True):
        super(KerioConnect, self).__init__(PRODUCT_CONNECT, host, port, '/login/dologin', login, password, authorization)