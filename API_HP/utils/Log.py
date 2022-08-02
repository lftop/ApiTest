# -*-coding:utf-8-*-
import logging
import time

# 设置日志颜色的包
import colorlog

from common.common_path import *


class Logs:
    '''日志颜色配置'''
    log_colors_config = {
        # 颜色支持 blue蓝，green绿色，red红色，yellow黄色，cyan青色
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
    # 保存文件的日志格式
    file_formatter = logging.Formatter(
        fmt='[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
        datefmt='%Y-%m-%d  %H:%M:%S'
    )
    # 控制台的日志格式
    console_formatter = colorlog.ColoredFormatter(
        # 输出那些信息，时间，文件名，函数名等等
        fmt='%(log_color)s[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
        # 时间格式
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors=log_colors_config
    )

    def __init__(self,types):
        # self.msg = kwargs
        self.types = types if types is not "" else "debug"
        self.logger = logging.getLogger('test')
        # 输出到控制台
        self.console_handler = logging.StreamHandler()
        # '''获取当前年月日作为日志文件名'''
        self.times = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        self.fileName = os.path.join(log_path + self.times + ".log")
        self.file_handler = logging.FileHandler(filename=self.fileName, mode='a', encoding='utf8')

        # 日志级别设置logger控制最低输出什么级别日志(优先级最高)
        self.logger.setLevel(logging.DEBUG)
        # console_handler设置控制台最低输出级别日志
        self.console_handler.setLevel(logging.DEBUG)
        # console_handler设置保存到文件最低输出级别日志
        self.file_handler.setLevel(logging.INFO)
        # 日志输出格式
        self.console_handler.setFormatter(self.console_formatter)
        self.file_handler.setFormatter(self.file_formatter)
        # self.resolve_reset_log()
        self.resolve_reset_log()

    # 重复日志问题：
    # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，解决重复打印的问题

    def resolve_reset_log(self):
        if not self.logger.handlers:
            self.logger.addHandler(self.console_handler)
            self.logger.addHandler(self.file_handler)

    def console_save(self, **msg):

        if self.types == "debug":
            self.logger.debug(msg=key_value(msg))
        elif self.types == "info":
            self.logger.info(msg=key_value(msg))
        elif self.types == "warning":
            self.logger.info(msg=key_value(msg))
        elif self.types == "error":
            self.logger.info(msg=key_value(msg))
        else:
            self.logger.critical(msg=msg)
        self.close_hander()

    def close_hander(self):
        self.console_handler.close()
        self.file_handler.close()


# if __name__ == "__main__":
#     logs = Logs(types="info")
#     logs.console_save(msg="asdas")
