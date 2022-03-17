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

    def getLeasesDhcp(self, scopeIds, start=0, limit=-1):
        return self.request("Dhcp.getLeases", {
            "query": {
                "conditions":[],
                "combining":"Or",
                "orderBy":[{"columnName":"ipAddress","direction":"Asc"}],
                "start": start,
                "limit": limit,
            },
            "scopeIds": scopeIds
        })['result']

    def getVpnClients(self, start=0, limit=-1):
        return self.request("VpnClients.get", {
            "query": {
                "start": start,
                "limit": limit,
            },
            "refresh": True
        })['result']

