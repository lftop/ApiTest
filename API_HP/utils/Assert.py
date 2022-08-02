from utils.Log import Logs
import json
log = Logs(types='info')


class Assert:
    def __init__(self, type="json", actual=None, expected=None):
        self.__type = type
        self.__actual = actual
        self.__expected = expected

    def route_assert(self):
        if self.__type == "json":
            result = self.__json_assert()
        if self.__type == "xml":
            result = self.__xml_assert()
        return result

    def __xml_assert(self, ):
        """
        :param response_body: 返回的请求体
        :param aim_data: 寻找的目标参数
        :param expected: 期望参数和值
        :return:
        """
        # print("Actual:{0}".format(self.__actual))
        # print("Expected result:{0}",self.__expected)
        flag = True
        if list(self.__actual.keys())[0] == "msg":
            flag = False
        elif self.__actual.get('body') == "No response body":
            flag = self.__actual.get("status") == self.__expected.get("status")
        else:
            flag = "<{0}>{1}".format(self.__expected.get("path"), self.__expected.get("value")) in self.__actual.get(
                'body')
            "判断状态码与目标参数与预期结果一致"
        return flag

    def __json_assert(self):
        flag = True
        if list(self.__actual.keys())[0] == "msg":
            flag = False
        elif self.__actual.get('body') == "No response body":
            flag = self.__actual.get("status") == self.__expected.get("status")
        else:
            flag = self.search_ele().get('value') == self.__expected.get('ele_txt').get('value')
        return flag

    def search_ele(self, data=None, k=''):
        # 根元素下的以及子元素
        result = None
        try:
            if k == '':k = self.__expected.get('ele_txt').get('key')
            else:k = k
            if data is None:data =self.__actual
            data = json.loads(data.get('body'),encoding='utf-8')
            print("data:",data)
            for key, val in data.items():
                if result != None:break
                if k == key:
                    result = {'key':k,'value':val}
                    break
                else:
                    # print("type:{0} value:{1}".format(type(val), val))
                    if type(val) is dict:
                        result = self.search_ele(val, k)
                    else:
                        continue
        except AttributeError as e:
            result = {'key': k, 'value': None}
            print(e)
        # print(result)
        return result


# if __name__ == "__main__":
#     actual = {
#         'data': {
#             'deviceLanguage': 'en',
#             'displayContrast': '100',
#             'keyPressVolume': 'soft',
#             'version': '1.0.0'
#         },
#         'msg': "asdsa"
#     }
#     expected = {
#         'status': 200,
#         'ele_txt':{'key':'deviceLanguage','value':'en'}
#     }
#     ass = Assert(actual=actual, expected=expected)
#     print(ass.search_ele())
