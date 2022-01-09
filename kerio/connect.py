from .base import Kerio, PRODUCT_CONNECT


class KerioConnect(Kerio):
    def __init__(self, host, login, password, port=4040, authorization=True):
        super(KerioConnect, self).__init__(PRODUCT_CONNECT, host, port, '/login/dologin', login, password, authorization)

    def getDomains(self):
        return self.request("Domains.get", {
            "query": {
                "fields": [
                    "id",
                    "name",
                    "service",
                    "keepForRecovery",
                    "isDistributed",
                    "deletedItems",
                    "junkEmail",
                    "sentItems",
                    "autoDelete",
                    "isPrimary",
                    "passwordExpirationEnabled",
                    "passwordComplexityEnabled",
                    "passwordMinimumLength",
                    "passwordHistoryCount",
                    "isLdapManagementAllowed"
                ],
                "orderBy": [
                    {
                        "columnName": "name",
                        "direction": "Asc"
                    }
                ],
                "start": 0,
                "limit": -1
            }
        })['result']

    def getGroupListAccessPolicy(self, start=0, limit=-1):
        return self.request("AccessPolicy.getGroupList", {
            "query": {
                "start": start,
                "limit": limit
            }
        })['result']

    def createUsers():
        return self.request("Users.create", {
            "users": users
            })
