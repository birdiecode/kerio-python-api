from .base import Kerio, PRODUCT_CONNECT


class KerioConnectToolMakeUser():
    skeleton = {
        "loginName": None,
        "description": None,
        "hasDefaultSpamRule": True,
        "allowPasswordChange": True,
        "publishInGal": True,
        "authType": "UInternalAuth",
        "isPasswordReversible": True,
        "isEnabled": True,
        "domainId": None,
        "hasDomainRestriction": False,
        "accessPolicy": None,
        "password": None,
        "role": {
            "userRole": "UserRole",
            "publicFolderRight": False,
            "archiveFolderRight": False
        },
        "itemLimit": {
            "isActive": False,
            "limit": 0
        },
        "diskSizeLimit": {
            "isActive": False,
            "limit": {
                "value": 0,
                "units": "MegaBytes"    
            }
        },
        "outMessageLimit": {
            "isActive": False,
            "limit": {
                "value": 0,
                "units": "MegaBytes"
            }
        },
        "cleanOutItems": {
             "isUsedDomain": True,
             "deletedItems": {
                "isEnabled": False,
                "days": 30
            },
            "junkEmail": {
                "isEnabled": False,
                "days": 30
            },
            "sentItems": {
                "isEnabled": False,
                "days": 30
            },
            "autoDelete": {
                "isEnabled": False,
                "days": 1095
            }
        },
        "fullName": None,
        "emailForwarding": {
            "mode": "UForwardNone",
            "emailAddresses": []
        },
        "emailAddresses": [],
        "userGroups": [],
        "companyContactId": ""
    }

    def __init__(self, fullName=None, loginName=None, description=None, domainId=None, accessPolicy=None, password=None):
        self.skeleton['fullName']=fullName
        self.skeleton['loginName']=loginName
        self.skeleton['description']=description
        self.skeleton['domainId']=domainId
        self.skeleton['accessPolicy']=accessPolicy
        self.skeleton['password']=password


class KerioConnectToolAccessPolicy:
    def __init__(self, ww):
        self.ww = ww

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        ee = self.ww[self.indx]
        self.indx += 1
        return ee

    def getDefault(self):
        for ee in self.ww:
            if ee['isDefault']:
                return ee
        raise Exception("not found access policy")


class KerioConnectToolDomains:
    def __init__(self, ww):
        self.ww = ww

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        ee = self.ww[self.indx]
        self.indx+=1
        return ee

    def get(self, domain):
        for ee in self.ww:
            if ee["name"] == domain:
                return ee['id']
        raise Exception("not found domain")


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

    def createUsers(self, users):
        return self.request("Users.create", {
            "users": users
            })

    def getMailboxCountUsers(self):
        return self.request("Users.getMailboxCount", {})

    def getRoleDistributedDomain(self):
        return self.request("DistributedDomain.getRole", {})
