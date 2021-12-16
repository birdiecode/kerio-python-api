from .base import Kerio, PRODUCT_OPERATOR


class KerioOperator(Kerio):
    def __init__(self, host, login, password, port=4021, authorization=True):
        super(KerioOperator, self).__init__(PRODUCT_OPERATOR, host, port, '/dologin.php', login, password, authorization)

    def getUsers(self, start=0, limit=-1):
        return self.request("Users.get", {
            "query": {
                "start": start,
                "limit": limit,
                "orderBy": [
                    {"columnName": "EXTENSIONS", "direction": "Asc"}
                ]
            }
        })['result']

    def getExtensions(self, start=0, limit=-1):
        return self.request("Extensions.get", {
            "query": {
                "start": start,
                "limit": limit,
                "orderBy": [
                    {"columnName": "telNum", "direction": "Asc"}
                ]
            }
        })['result']

    def getConferences(self, start=0, limit=-1):
        return self.request("Conferences.get", {
            "query": {
                "start": start,
                "limit": limit,
                "orderBy": [
                    {"columnName": "EXTENSION_NUMBER", "direction": "Asc"}
                ]
            }
        })['result']

    def getCallQueues(self, start=0, limit=-1):
        return self.request("CallQueues.get", {
            "query": {
                "start": start,
                "limit": limit,
                "orderBy": [
                    {"columnName": "queueNumber", "direction": "Asc"}
                ]
            }
        })['result']

    def getAutoAttendantScripts(self, start=0, limit=-1):
        return self.request("AutoAttendantScripts.get", {
            "query": {
                "start": start,
                "limit": limit,
                "orderBy": [
                    {"columnName": "IVR_NUMBER", "direction": "Asc"}
                ]
            }
        })['result']

    def getRingingGroups(self, start=0, limit=-1):
        return self.request("RingingGroups.get", {
            "query": {
                "start": start,
                "limit": limit,
                "orderBy": [
                    {"columnName": "EXTENSION_NUMBER", "direction": "Asc"}
                ]
            }
        })['result']

    def getPbxServices(self):
        return self.request("PbxServices.get", {})['result']

    def createExtensions(self, telNum: str, sipUsername, description, sipPassword):
        return self.request("RingingGroups.get", {
            'detail': {
                'telNum': telNum,
                'sipUsername': sipUsername,
                'description': description,
                'callPermission': 1,
                'userGuid': None,
                'selectedCodecs': [
                    {'ID': 'G.711 A-law', 'SEQUENCE': 1, 'DESCRIPTION': 'G.711 A-law'},
                    {'ID': 'G.711 U-law', 'SEQUENCE': 2, 'DESCRIPTION': 'G.711 U-law'},
                    {'ID': 'GSM Full Rate', 'SEQUENCE': 3, 'DESCRIPTION': 'GSM Full Rate'},
                    {'ID': 'speex', 'SEQUENCE': 4, 'DESCRIPTION': 'SpeeX'},
                    {'ID': 'ilbc', 'SEQUENCE': 5, 'DESCRIPTION': 'iLBC'},
                    {'ID': 'g722', 'SEQUENCE': 6, 'DESCRIPTION': 'G.722 (wideband)'},
                    {'ID': 'g726', 'SEQUENCE': 7, 'DESCRIPTION': 'G.726'}
                ],
                'natSupport': False,
                'secured': False,
                'recordInbound': True,
                'recordOutbound': True,
                'faxDetect': False,
                'faxDetectType': 0,
                'dtmfMode': 0,
                'sipPassword': sipPassword
            }
        })['result']