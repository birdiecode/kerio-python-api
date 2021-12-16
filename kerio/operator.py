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

    def createExtensions(self, tel_num: str, sip_username: str, description: str, sip_password: str):
        return self.request("RingingGroups.get", {
            'detail': {
                'telNum': tel_num,
                'sipUsername': sip_username,
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
                'sipPassword': sip_password
            }
        })['result']

    def toolsExtensionForUser(self, guid_group, tel_num: str, description):
        return {"GUID": guid_group,
                "TEL_NUM": tel_num,
                "DESCRIPTION": description,
                "IS_PRIMARY":True,
                "RING_EXTENSION":True,
                "RING_EXTENSION_TIMEOUT":120,
                "BUSY_ACTION":1,
                "VOICEMAIL_FALLBACK":False,
                "VOICEMAIL_FALLBACK_TIMEOUT":120,
                "FIND_ME_LIST":[],
                "OCCUPIED_REJECT":"",
                "OBEY_RING_RULES":"",
                "WEBRTC_RING_GROUP":""}

    def createUsers(self, username: str, user_password: str, ami_password: str, extensions, full_name="", email=""):
        return self.request("RingingGroups.get", {
            "detail": {
                "LDAP_ENABLED": 0,
                "FULL_NAME": full_name,
                "EMAIL": email,
                "DISABLED": 0,
                "ADMINISTRATION_ROLE_ID": 2,
                "EXTENSIONS": extensions,
                "LANGUAGE_PBX": 1,
                "AMI_ENABLED": False,
                "WEBRTC_ENABLED": True,
                "VOICEMAIL_DISABLED": False,
                "VOICEMAIL_PRESS0_ENABLED": False,
                "VOICEMAIL_PRESS0_TELNUM": "",
                "USERNAME": username,
                "USER_PASSWORD": user_password,
                "PIN": "1191",
                "AMI_PASSWORD": ami_password
            }
        })['result']

    def getCallHistory(self, start=0, limit=-1):
        return self.request("CallHistory.get", {
            "query": {
                "limit": limit,
                "start": start,
                "orderBy": [
                    {"columnName": "TIMESTAMP", "direction": "Desc"}
                ]
            }
        })['result']