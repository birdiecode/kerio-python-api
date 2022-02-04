from .base import Kerio, PRODUCT_CONTROL


class KerioControl(Kerio):
    def __init__(self, host, login, password, port=4081, authorization=True):
        super(KerioControl, self).__init__(PRODUCT_CONTROL, host, port, '/internal/dologin.php', login, password, authorization)

    def getDhcp(self, start=0, limit=-1):
        return self.request("Dhcp.get", {
            "query": {
                "start": start,
                "limit": limit,
            }
        })['result']
