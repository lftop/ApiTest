import xml.etree.ElementTree as ET

from common.common_path import *
import xmltodict

class xmlControl:

    def __init__(self, path):
        self.file_path = xml_dir(path)
        self.tree = self.__set_tree()
        self.root = self.__set_root()

    def __set_tree(self):
        return ET.parse(self.file_path)

    def __set_root(self):
        return self.tree.getroot()

    def set_ele_value(self, data):
        try:
            if data is None:
                raise Exception("data can't be null")
            path, value, namespace = data.get('path'), data.get('value'), data.get('namespace')
            self.root.find(path=path, namespaces=namespace).text = value
            self.register_all_namespaces()
            self.tree.write(file_or_filename=self.file_path,encoding='utf-8')
        except Exception as e:
            print("Error:", e)

    def register_all_namespaces(self):
        namespaces = dict([node for _, node in ET.iterparse(self.file_path, events=['start-ns'])])
        for ns in namespaces:
            ET.register_namespace(ns, namespaces[ns])

    def restore_payload(self, path):
        """
        :@path: Orignal template
        :msg: 恢复template初始值
        :return:
        """
        try:
            with open(file=xml_dir(path), mode='r') as f1:
                text = f1.read()
            f1.close()
            with open(file=self.file_path, mode='w') as f:
                f.write(text)
            f.close()
            print("恢复{0}成功".format(self.file_path))
        except IOError as io:
            print("文件操作异常：{0}".format(io))

    def get_payload(self):
        """
        :return: 返回修改后的payload
        """
        payload=None
        try:
            with open(file=self.file_path,mode='r') as f:
                payload=f.read()
        except IOError as e:
            payload=None
        return payload

    # def get_ele_value(self,data):
    #     try:
    #         if self.file_path is None:
    #             raise Exception("请求返回数据为空")
    #         ele=self.root.find(path=data.get('path'),namespaces=data.get('namespace'))
    #         result={data.get('path'):ele.text}
    #     except Exception as e:
    #         result=None
    #         print(e)
    #     return result


if __name__ == "__main__":
    # xmlobj=xmlControl("HP_Scan\\HP_Scan_Usb_Setting_Payload.xml")
    str1 = """<cpcfgdyn:CopyConfigDyn xmlns:cpcfgdyn="http://www.hp.com/schemas/imaging/con/ledm/cpcfgdyn/2008/05/05" xmlns:copy="http://www.hp.com/schemas/imaging/con/copy/2008/07/07" xmlns:dd="http://www.hp.com/schemas/imaging/con/dictionaries/1.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.hp.com/schemas/imaging/con/ledm/cpcfgdyn/2008/05/05 ../schemas/CopyConfigDyn.xsd">
        <dd:Version>
        <dd:Revision>SVN-IPG-LEDM.122</dd:Revision>
        <dd:Date>2011-10-18</dd:Date>
        </dd:Version>
        <copy:Copy>enabled</copy:Copy>
        <copy:ColorCopy>enabled</copy:ColorCopy>
        <copy:DefaultLighterDarker>4</copy:DefaultLighterDarker>
        <copy:DefaultNumberOfCopies>1</copy:DefaultNumberOfCopies>
        <copy:DefaultOptimize>Mixed</copy:DefaultOptimize>
        <copy:DefaultReduceEnlarge>original</copy:DefaultReduceEnlarge>
        <copy:DefaultReduceEnlargeCustom>100</copy:DefaultReduceEnlargeCustom>
        <copy:DefaultTraySelect>Tray1</copy:DefaultTraySelect>
        <copy:DefaultCollation>disabled</copy:DefaultCollation>
        <copy:DefaultCopyQuality>normal</copy:DefaultCopyQuality>
        <copy:DefaultMarginOff>enabled</copy:DefaultMarginOff>
        <dd:CopySides>simplexToSimplex</dd:CopySides>
        <cpcfgdyn:DefaultOutputType>color</cpcfgdyn:DefaultOutputType>
        <cpcfgdyn:DefaultInputSource>Flatbed</cpcfgdyn:DefaultInputSource>
        <cpcfgdyn:DefaultDuplexBindingOption>longEdge</cpcfgdyn:DefaultDuplexBindingOption>
        </cpcfgdyn:CopyConfigDyn>"""
    xmlobj=xmlControl(path=str1,type="str")

    # file = xml_dir("HP_Scan\\HP_Scan_Usb_Setting_Payload.xml")
    # xml_obj = ET.parse(source=file)
    # root = xml_obj.getroot()
    # print(root)
    # print("root 的子元素")
    # for ele in root:
    #     print(ele)
    #
    # ele1 = root.find(path=".//dd:Exposure",
    #                  namespaces={'dd': 'http://www.hp.com/schemas/imaging/con/dictionaries/1.0/'})
    # ele1.text = str(20)
    # print(ele1.text)
    # # register_all_namespaces(filename=file)
    # xml_obj.write(file_or_filename=file)

    data={
            'path': './/copy:DefaultLighterDarker',
            'value': '3',
            'namespace':{'copy': 'http://www.hp.com/schemas/imaging/con/copy/2008/07/07'}
        }
    xmlobj.get_ele_value(type="str",data=data)

    # print(xmlobj.get_payload())