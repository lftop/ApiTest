import re

import xmltodict

from common.common_path import *


#
# print(xml_dir("HP_Copy\\HP_Copy_Payload.xml"))
# path = xml_dir("HP_Copy\\HP_Copy_Payload.xml")


# f = open(file=path, mode='r')
# doc = xmltodict.parse(f.read())
#
# print(doc.get('cpcfgdyn:CopyConfigDyn'))
# copy = doc.get('cpcfgdyn:CopyConfigDyn').get('copy:ColorCopy')
# print(copy)
# doc['cpcfgdyn:CopyConfigDyn']['copy:ColorCopy'] = "enabled"
# print(doc.get('cpcfgdyn:CopyConfigDyn').get('copy:ColorCopy'))
# dicttoxml = xmltodict.unparse(input_dict=doc)
# with open(file=path, mode='w') as f:
#     f.write(dicttoxml)


class XmlControl:
    root_ele = None
    aim_ele = None

    def __init__(self, path=''):
        """
        :param path:  example for HP_Copy\\HP_Copy_Payload.xml
        """
        self.xml_path = xml_dir(path)
        self.doc = self.__create_doc()
        self.root_ele = self.__set_root()

    def getxml(self):
        try:
            f = open(self.xml_path, 'r')
            xmldata = f.read()
        except IOError as e:
            xmldata = None
            print(e)
        f.close()
        return xmldata

    def __create_doc(self):
        try:
            f = open(self.xml_path, 'r', encoding='utf-8')
            doc = xmltodict.parse(xml_input=f.read())
        except Exception as e:
            doc = None
            print("文件打开异常：{0}".format(e))
        f.close()
        return doc

    def __set_root(self):
        return list(self.__create_doc().keys())[0]

    def get_ele_value(self, key):
        try:
            if re.search("^<(\D)+>$", key) is None:
                raise Exception("元素格式不正确")
            if key[1:-1] == self.root_ele:
                raise Exception("传入了根元素")
            return self.doc.get(self.root_ele).get(key[1:-1]) if self.doc.get(self.root_ele).get(
                key[1:-1]) is not None else "元素不存在"
        except Exception as err:
            print(err)
            return err

    def get_root_data(self):
        return self.doc.get(self.root_ele)

    def set_ele_value(self, k, v):
        try:
            if re.search("^<(\D)+>$", k) is None:
                raise Exception("元素格式不正确")
            if k[1:-1] == self.root_ele:
                raise Exception("传入了根元素")
            self.doc[self.root_ele][k[1:-1]] = v
            dict_to_xml = xmltodict.unparse(self.doc, encoding='utf-8')
            if open(self.xml_path, 'w').write(dict_to_xml):
                print("编辑文件：{0}成功".format(self.xml_path))
            else:
                raise Exception("编辑文件失败：{0}".format(self.xml_path))
        except Exception as err:
            print(err)

    def restore_payload(self, path):
        """
        :@path: Orignal template
        :msg: 恢复template初始值
        :return:
        """
        try:
            with open(file=xml_dir(path), mode='r') as f1:
                text = f1.read()
            with open(file=self.xml_path, mode='w') as f:
                f.write(text)
            print("恢复{0}成功".format(self.xml_path))
        except IOError as io:
            print("文件操作异常：{0}".format(io))

    def search_ele(self, data, k):
        # 根元素下的以及子元素
        one_son = list(data.keys())
        if k in one_son:
            print("k:{0},value:{1}".format(k, data.get(k)))
            self.aim_ele = {k: data.get(k)}
        else:
            for k2 in one_son:
                # print("type:{0} value:{1}".format(type(data[k2]),data[k2]))
                if type(data[k2]) is not str:
                    # print(data[k2])
                    self.search_ele(data[k2], k)

    def set_ele_value_super(self,data,key):
        """
        :param data:
        :param key:
        :return:
        """
        keys=key.splice


class XmlToDict:
    def __init__(self, data):
        self.__data = data
        self.ele_root = self.__set_root()

    def to_dict(self):
        return xmltodict.parse(self.__data)

    def __set_root(self):
        return list(self.to_dict().keys())[0]

    def get_ele_value(self, k):
        aim_key = list(self.to_dict().get(self.ele_root).keys())
        # print(aim_key)
        return {"path": k,
                "value": self.to_dict().get(self.ele_root).get(k) if k in aim_key else None
                }


if __name__ == "__main__":
    path = Dir_Project + "\\source\\HP_Scan\\HP_Scan_Usb_Setting_Dyn.xml"
    # xmll=XmlToDict(f.read())
    # print(xmll.to_dict())
    # data=(xmll.to_dict().get(xmll.ele_root))
    # for items in data:
    #     print(data[items])
    obj = XmlControl(path)
    obj.set_ele_value_super()