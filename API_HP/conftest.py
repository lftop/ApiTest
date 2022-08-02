import pytest
from utils.Log import Logs
from utils.ReadConfig import Configer
import requests
from requests.auth import HTTPBasicAuth
import random
@pytest.fixture(scope="session",autouse=True)
def get_cookie():
    logs = Logs(types='info')
    config = Configer()
    AUTHS = {"name":"admin","psw":"12345678"}
    url="https://{0}/AuthChk?_=165761665778{1}".format(config.get("HTTPS","IP"),random.randint(1,10))
    try:
        re = requests.request(url=url, method='GET', verify=False,auth=HTTPBasicAuth(AUTHS.get('name'),AUTHS.get('psw')))
        logs.console_save(des="获取cookies",url=url,status="Successfull {0} OK".format(re.status_code))
        for k, v in requests.utils.dict_from_cookiejar(re.cookies).items():
            str1 = k + "=" + v
        return str1
    except Exception as e:
        logs.console_save(des="获取Cookies请求失败",details=e)
#
# @pytest.fixture(scope="session", autouse=True)
# def get_cookie():
#     print("开始测试")
#     yield "hello"
#     print("结束测试")


def pytest_collection_modifyitems(items):
    """
    修改用例名称中文乱码
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')
