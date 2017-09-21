# -*- encoding: utf-8 -*-
import sys
import config_load
import pymongo

dbconfig_path = "../config/db.json"

def judge_interval(before):
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
