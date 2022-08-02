import requests
from requests.auth import HTTPBasicAuth
from utils.Log import Logs

"""

"""


class Requests:
    logs = Logs(types="info")
    auth_account = {"name": "admin", "psw": "12345678"}
    payload_key: {'json': 'json', 'data': 'data', 'params': 'params'}

    def __init__(self, url, method, **kwargs):
        self.__url = url
        self.__method = method
        self.__params = self.__deal_param(kwargs)

    def __deal_param(self, params):
        header = params.get('headers')
        print("headers:", header)
        payload = params.get("payloads")
        print("payload:", payload)
        key = list(payload.keys())[0]
        if key == 'data':
            param = {'headers': header, 'data': payload.get(key)}

        if key == "json":
            param = {'headers': header, 'json': payload.get(key)}

        if key == "param":
            param = {'headers': header, 'params': payload.get(key)}
        print("param:",param)
        return param

    def transfer_station(self):

        if self.__method == "GET":
            result = self.get()
        elif self.__method == "PUT":
            result = self.put()
        elif self.__method == "POST":
            result = self.post()
        elif self.__method == "DELETE":
            result = self.delete()
        else:
            result = "操作方式错去"
        return result

    def get(self):
        try:
            re = requests.request(self.__method, self.__url, **self.__params, verify=False,
                                  auth=HTTPBasicAuth(self.auth_account.get('name'), self.auth_account.get('psw')))
            return {"body": re.text, "status": re.status_code}
        except requests.exceptions.ConnectTimeout as e:
            self.logs.console_save(msg=e)
            return {"msg": "{0}|{1}请求超时".format(self.__method, self.__url)}

    def post(self):
        try:
            re = requests.request(self.__method, self.__url, **self.__params, verify=False,
                                  auth=HTTPBasicAuth(self.auth_account.get("name"), self.auth_account.get("psw")))
            return {"body": re.text if re.text is None else "No response body", "status": re.status_code}
        except requests.exceptions.ConnectTimeout as e:
            self.logs.console_save(msg=e)
            return {"msg": "{0}|{1}请求超时".format(self.__method, self.__url)}

    def put(self):
        result = None
        try:
            re = requests.request(self.__method, self.__url, **self.__params, verify=False,
                                  auth=HTTPBasicAuth(self.auth_account.get("name"), self.auth_account.get("psw")))
            result = {"body": re.text if re.text is None else "No response body", "status": re.status_code}
        except requests.exceptions.ConnectTimeout as e:
            self.logs.console_save(msg=e)
            result = {"msg": "{0}|{1}请求超时".format(self.__method, self.__url)}
        return result

    def delete(self):
        try:
            re = requests.request(self.__method, self.__url, **self.__params, verify=False,
                                  auth=HTTPBasicAuth(self.auth_account.get("name"), self.auth_account.get("psw")))
            return {"body": re.text if re.text is None else "No response body", "status": re.status_code}
        except requests.exceptions.ConnectTimeout as e:
            self.logs.console_save(msg=e)
            return {"msg": "{0}|{1}请求超时".format(self.__method, self.__url)}


