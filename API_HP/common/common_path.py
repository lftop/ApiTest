import os

# 项目目录
Dir_Project = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 配置文件目录
config_path = os.path.join(Dir_Project, "config\\config.ini")
# 测试用例目录
test_case_dir = os.path.join(Dir_Project, "testcase")
# 测试用例数据目录
test_case_data_dir = os.path.join(Dir_Project, "testdata\\")
# log文件生成地址
log_path = os.path.join(Dir_Project, "result/Logs/")
# 测试报告地址
report_path = os.path.join(Dir_Project, "")

# utils路径
utils_path = os.path.join(Dir_Project, "utils")

# xml_payload路径
xml_dir = lambda dir: os.path.join(os.path.join(Dir_Project, "source"), dir)


def key_value(kwargs):
    fmt = ""
    for k, v in kwargs.items():
        fmt += "{0}->{1}\t|\t".format(k, v)
    return fmt
