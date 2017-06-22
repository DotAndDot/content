# -*- encoding: utf-8 -*-

import json



class StatisticConfig(object):
    def __init__(self, path):
        self.__path = path
        self.__file = None
        self.__len = 0
    
    def open(self):
        try:
            self.__file = open(self.__path, 'r')
        except Exception, e:
            return False
        
        try:
            content = self.__file.read()
        except Exception, e:
            self.__file.close()
            return False

        try:
            self.__json = json.loads(content)
        except Exception, e:
            return False
        if not (isinstance(self.__json, dict)):
            return False
        self.__len = len(self.__json)
        return True
    
    def len(self):
        return self.__len

    def __getitem__(self, index):
        return self.__json[index]


class DBConfig(object):
    def __init__(self, path):
        self.__path = path
        self.__file = None
        
    def open(self):
        try:
            self.__file = open(self.__path, 'r')
        except Exception, e:
            return False
        
        try:
            content = self.__file.read()
        except Exception, e:
            self.__file.close()
            return False

        try:
            self.__json = json.loads(content)
        except Exception, e:
            return False

        if not (isinstance(self.__json, dict)):
            return False
        return True

    def get(self, field):
        if not (isinstance(field, str)):
            return False
        return self.__json.get(field, False)