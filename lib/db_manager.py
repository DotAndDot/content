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
            self.__host = self.__db_config['host']
            self.__username = self.__db_config['username']
            self.__pwd = self.__db_config['pwd']
            try:
                self.__client = pymongo.MongoClient(self.__host)
            except:
                sys.exit(0)
            self.__db = self.__client[self.__db_config['db']]

    def select_col(self, collection):
        try:
            col = self.__db[collection]
            return col
        except:
            return False

    def find(self, collection, query):
        col = self.select_col(collection)
        if not col:
            return False
        return col.find(query)
    
    def find_one(self, collection, query):
        col = self.select_col(collection)
        if not col:
            return False
        return col.find_one(query)

    def insert(self, collection, query):
        col = self.select_col(collection)
        if not col:
            return False
        return col.insert_many(query)

    def insert_one(self, collection, query):
        col = self.select_col(collection)
        if not col:
            return False
        return col.insert_one(query)

    def update(self, collection, where, value):
        col = self.select_col(collection)
        if not col:
            return False
        return col.update(where, value)

    def delete(self, collection, where):
        col = self.select_col(collection)
        if not col:
            return False
        return col.delete(where)

    def aggregate(self, collection, pipeline):
        col = self.select_col(collection)
        if not col:
            return False
        return col.aggregate(pipeline)