# -*- encoding: utf-8 -*-
import sys
import config
import pymongo

dbconfig_path = "../config/db.json"

def judge_interval(before):
    pass

class DBManager(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(DBManager, cls).__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.__db_config = config.DBConfig(dbconfig_path)
        if not (self.__db_config.open()):
            sys.exit(0)
        self.__host = self.__db_config.get('host')
        self.__username = self.__db_config.get('username')
        self.__pwd = self.__db_config.get('pwd')
        try:
            self.__client = pymongo.MongoClient(self.__host)
        except Exception, e:
            sys.exit(0)
        self.__db = self.__client[self.__db_config.get('db')]

    def handle_count(self, collection, field, destcollection):
        pass

    def handle_add(self, collection, field, destcolleciont):
        pass

    def get_last_record(self, item):
        pass


interval = {"day": 1, 
            "week" : 7, 
            "month" : 30}


class StatisticManager(object):
    def __init__(self, path):
        self.__statistic_config = config.StatisticConfig(path)
        if not (self.__statistic_config.open()):
            sys.exit(0)
        self.__db_manager = DBManager()
        
    def run(self):
        for i in range(self.__statistic_config.len()):
            item = self.__statistic_config[i]
            fre = item["frequence"]
            last = self.__db_manager.get_last_record(item["name"])
            if (judge_interval(last) < item["frequence"]):
                continue
            if(item["type"] == "count"):
                self.__db_manager.handle_count(item["collection"], item["field"], item["destcollection"])
            elif (item["type"] == "add"):
                self.__db_manager.handle_add(item["collection"], item["field"], item["destcollection"])
