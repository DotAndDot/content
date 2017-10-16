# -*- encoding: utf-8 -*-
from comm.statis_comm import *
from comm.statis_global import *
from content_statistic.judge import *
from content_statistic.strategy import *
import sys, pymongo

dbconfig_path = "../config/db.json"


class StatisticManager(object):
    def __init__(self, config):
        self.__statistic_config = config 
    
    def is_same(self, item1, item2):
        for k, v in item1.items():
            if not item2.has_key(k) or v != item2[k]:
                return False
        for k, v in item2.items():
            if not item1.has_key(k) or v != item1[k]:
                return False
        return True

    def run(self):
        if(  not Judgement.frequency_judge(self.__statistic_config) ):
            slogger.info("statis %s is in frequency" % self.__statistic_config.get_name())
            return False
        
        name = self.__statistic_config.get_name()
        target_col = self.__statistic_config.get_target()
        statis_res = {}
        for item in self.__statistic_config.get_options():
            stra = strategy_create(item.get_operate())
            res = stra.execute(item)
            if not res:
                slogger.info("statis error on %s" % item.get_name())
                continue
            for k,v in res.items():
                statis_res[k] = v

        statis_res['create_time'] = DATE_TODAY
        statis_res['mode'] = FULL
        db_manager.insert_one(target_col, statis_res)

        if Judgement.mode_judge(self.__statistic_config):
            query = {
                'name' : name
            }
            res = db_manager.find(target_col, query).sort(
                'create_time', pymongo.DESCENDING
            )
            try :
                options_names = self.__statistic_config.get_options_names()
                last_res = res[1]
                for name in options_names:
                    if not last_res.has_key(name) :
                        continue
                    for si in range(len(statis_res[name])):
                        for li in range(len(last_res[name])):
                            if self.is_same(statis_res[name][si][0], last_res[name][li][0]):
                                statis_res[name][si][1] -= last_res[name][li][1]
                statis_res['create_time'] = DATE_TODAY
                statis_res['mode'] = INCREMENT
                db_manager.insert_one(target_col, statis_res)

            except:
                pass