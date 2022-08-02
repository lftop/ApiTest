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

# if __name__ == "__main__":
#     url = "https://10.50.29.64//Copy/CopyConfigDyn.xml"
#     headers={'Content-Type': 'text/xml',
#              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
#              'Cookie': 'sid=s1952d94a-99f87ac563217a5a3994f59298973f1f'
#              }
#
#     data=""" <cpcfgdyn:CopyConfigDyn xmlns:copy="http://www.hp.com/schemas/imaging/con/copy/2008/07/07" xmlns:cpcfgdyn="http://www.hp.com/schemas/imaging/con/ledm/cpcfgdyn/2008/05/05" xmlns:
# dd="http://www.hp.com/schemas/imaging/con/dictionaries/1.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.hp.com/schemas/imaging/con/ledm/cpcfgdyn
# /2008/05/05 ../schemas/CopyConfigDyn.xsd">
#     <copy:DefaultLighterDarker>5</copy:DefaultLighterDarker>
#     <copy:DefaultNumberOfCopies>1</copy:DefaultNumberOfCopies>
#     <copy:DefaultOptimize>Mixed</copy:DefaultOptimize>
#     <copy:DefaultReduceEnlarge>original</copy:DefaultReduceEnlarge>
#     <copy:DefaultTraySelect>Tray1</copy:DefaultTraySelect>
#     <copy:DefaultCollation>disabled</copy:DefaultCollation>
#     <copy:DefaultCopyQuality>normal</copy:DefaultCopyQuality>
#     <copy:DefaultMarginOff>enabled</copy:DefaultMarginOff>
#     <dd:CopySides>simplexToSimplex</dd:CopySides>
#     <cpcfgdyn:DefaultOutputType>color</cpcfgdyn:DefaultOutputType>
# </cpcfgdyn:CopyConfigDyn>"""
#     r = Requests(url=url, method="PUT",headers=headers,data=data)
#     print(r.transfer_station())
