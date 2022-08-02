import pytest
from common.common_path import *
import subprocess
from utils.Log import Logs
import os
if __name__=="__main__":
    logs = Logs(types='info')
    logs.console_save(msg="开始执行测试用力")
    # pytest.main(["-s", "-v", "./testcase/test_01.py", "--alluredir", "./result/report/"])
    # subprocess.call('allure generate result/report/ -o result/report/html --clean', shell=True)
    # subprocess.cal1('allure open -h 127.0.0.1 -p  8088 ./result/report/html', shell=True)

    pytest.main(["-s", "-v", "./testcase/test_01.py", "--alluredir=./result/report/"])

    os.system("allure generate ./result/report/ -o ./result/report/html --clean")
    # os.system("allure serve ./result/report/")
    os.system("allure open -h localhost -p 8306 ./result/report/html")
    logs.console_save(msg="测试用例执行结束")

# from utils.Log import Logs
# if __name__ == "__main__":
#
#     logs.console_save(msg="dasd")
#     conf = Configer()
#     print(conf.get('HTTPS', 'IP'))
