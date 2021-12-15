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
