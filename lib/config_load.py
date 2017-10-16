# -*- encoding: utf-8 -*-

import json

class DBConfig(object):
    def __init__(self, path):
        self.__path = path
        self.__file = None
        self.__file = open(self.__path, 'r')
        content = self.__file.read()
        self.__json = json.loads(content)

    def get(self, field):
        if not (isinstance(field, str)):
            return False
        return self.__json.get(field, False)

    def __getitem__(self, index):
        return self.__json[index]


class Option(object):
    def __init__(self, item):
        self.__item = item
    
    def get_name(self):
        return self.__item['name']

    def get_source(self):
        return self.__item['source']

    def get_field(self):
        if self.__item.has_key('field'):
            return self.__item['field']
        return False

    def get_common_fields(self):
        return self.__item['common_fields']

class ConfigItem(object):
    def __init__(self, item):
        self.__item = item
        self.__options = []
        for it in self.__item['options']:
            self.__options.append(Option(it))
    
    def get_target(self):
        return self.__item['target']

    def get_name(self):
        return self.__item['name']

    def get_options(self):
        return self.__item['options']

    def get_options_names(self):
        names = []
        for it in self.get_options():
            names.append(it.get_name())
        return names

class StatisticConfig(object):
    def __init__(self, path):
        self.__path = path
        self.__file = None
        self.__len = 0
        self.__file = open(self.__path, 'r')
        content = self.__file.read()
        self.__file.close()
        cjson = json.loads(content)
        self.__config = []
        self.__len = len(cjson)
        for it in cjson:
            self.__config.append(ConfigItem(it))

    
    def len(self):
        return self.__len
