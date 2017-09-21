# -*- encoding: utf-8 -*-
import sys
import pymongo

class DBManager(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(DBManager, cls).__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self, dbconfig):
        try:
            self.__db_config
        except:
            self.__db_config = dbconfig
            if not (self.__db_config.open()):
                sys.exit(0)
            self.__host = self.__db_config.get('host')
            self.__username = self.__db_config.get('username')
            self.__pwd = self.__db_config.get('pwd')
            try:
                self.__client = pymongo.MongoClient(self.__host)
            except:
                sys.exit(0)
            self.__db = self.__client[self.__db_config.get('db')]

    def handle_count(self, collection, field, destcollection):
        pass

    def handle_add(self, collection, field, destcolleciont):
        pass

    def get_last_record(self, item):
        pass