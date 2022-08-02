from configparser import ConfigParser

from common.common_path import *


class Configer(ConfigParser):
    def __init__(self):
        super(Configer, self).__init__()
        self.read(config_path, encoding='utf-8')
