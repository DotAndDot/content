# -*- encoding: utf-8 -*-

import json



class StatisticConfig(object):

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
        finally:
            self.__file.close()
            return False

        try:
            self.__json = json.loads(content)
        finally:
            return False
            
    