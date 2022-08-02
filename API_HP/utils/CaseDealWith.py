from utils.Log import Logs
from utils.ReadConfig import Configer
from utils.ReadYaml import YamlData
# from utils.controlXml import XmlControl
from utils.xmlControl import xmlControl

class CaseDealWith:
    logs = Logs(types='info')
    test_module = None
    test_case = None
    test_url = None
    test_headers = None
    test_data = None
    yamldata = None
    method=None
    configer = Configer()
    content_type = "json"
    support_type = ['json', 'xml']
    isRun = True
    method_support = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, filename=""):
        # self.__filename=filename
        self.yamldata = self.__set_yaml_data(filename)
        self.__set_module_name()
        self.__set_url()
        self.__set_case()
        self.__set_content_type()

    def __set_yaml_data(self, filename):
        return YamlData(filename).load_yaml()

    def __set_url(self):
        self.test_url = "https://" + self.configer.get('HTTPS', 'IP') + self.yamldata[0].get('module').get('url')

    def __set_module_name(self):
        """
        :return: return module name
        """
        try:
            data = self.yamldata
            # print(data[0].get("module").get('des'))
            if data == None:
                raise Exception("因为文件不存在获取它原因暂无数据")
            self.test_module = data[0].get('module').get("des")
        except Exception as e:
            print(e)
            self.logs.console_save(msg=e)

    def __set_case(self):
        try:
            data = self.yamldata
            # print(data[0].get("module").get('des'))
            if data == None:
                raise Exception("因为文件不存在获取它原因暂无数据")
            self.test_case = data[0].get('module').get("case")
        except Exception as e:
            print(e)
            self.logs.console_save(msg=e)

    def __isRun(self):
        self.isRun = self.yamldata[0].get('isRun')

    def __set_content_type(self):
        try:
            types = self.yamldata[0].get('module').get('content_type')
            if types not in self.support_type:
                raise Exception("{0}非法的编码格式，仅支持{1}".format(types, self.support_type))
            self.content_type = types
        except Exception as e:
            self.content_type = None
            self.logs.console_save(msg=e)

    def set_headers(self, cookie):
        """
        :param cookie:
        :return: 返回完整的请求头
        """
        try:
            head = self.yamldata[0].get('module')['headers']
            if head is None:
                raise Exception("没有请求头，请检查数据源是否编写了请求头")
            if head['Cookie'] is None:
                raise Exception("没有编写cookie来源，请检查是否正确设置了cookie的捕获")
            head['Cookie'] = cookie
            self.test_headers = head
            self.logs.console_save(msg="Cookie已重新替换为[{0}],实际请求头更新为：{1}".format(cookie, head))
        except Exception as e:
            self.logs.console_save(msg=e)

    def get_method(self, data):
        try:

            if data is None:
                raise Exception("请求体不能为空")
            if data['method'] not in self.method_support:
                raise Exception("{0}非法的请求方法,仅支持{1}".format(data['method'], self.method_support))
            method = data.get('method')
            self.method=method
        except Exception as e:
            method = None
            self.logs.console_save(msg=e)
        return method

    def get_test_payload(self, data):
        """
        :param data: input payload
        :return: None
        """
        try:
            payload = None
            if data is None:
                raise Exception("请求体不能为空")
            if self.content_type == "xml":
                if self.method=='GET':
                    payload={'param':data.get('payload').get('param')}
                else:
                    xmlobj = xmlControl(path=self.yamldata[0].get("module").get('template'))
                    xmlobj.set_ele_value(data=data.get('payload').get('data'))
                    payload = {'data':xmlobj.get_payload()}
                    # 恢复template为默认设置
                    xmlobj.restore_payload(self.yamldata[0].get('module').get('orignal_template'))
            if self.content_type == "json":
                    payload=data.get('payload')

        except Exception as e:
            payload = None
            self.logs.console_save(msg=e)
        return payload

    def get_data(self,data):
        return data.get('data')

    def get_step(self, case):
        return case.get('step')

    def get_expected(self, case):
        return case.get("check_items")

# if __name__ == "__main__":
#     case = CaseDealWith("hp_api_lan.yaml")
#     print(case.yamldata)
#     print(case.test_module)
#     print("url:", case.test_url)
#     print("case:", case.test_case)
#     print("isrun:", case.isRun, type(case.isRun))
#     print("type:", case.content_type)
#     print('method',case.get_method(case.test_case[0].get('step')[0]))
#     print("payload:",case.get_test_payload(case.test_case[0].get('step')[0]))
