from .base import Kerio, PRODUCT_CONTROL


class KerioControl(Kerio):
    def __init__(self, host, login, password, port=4081, authorization=True):
        super(KerioControl, self).__init__(PRODUCT_CONTROL, host, port, '/internal/dologin.php', login, password, authorization)
