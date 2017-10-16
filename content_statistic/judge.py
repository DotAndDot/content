# -*- coding: utf-8 -*-
from comm.statis_comm import *
from comm.statis_global import *
import pymongo, datetime

class Judgement(object):
    @staticmethod
    def frequency_judge(config):
        name = config.get_name()
        target = config.get_target()
        query = {
            'name': name 
        }
        res = db_manager.find(target, query).sort(
                'create_time', pymongo.DESCENDING
            )
        try :
            last_time = res[0]['create_time']
        except:
            return True
        
        lt = datetime.datetime.strptime(last_time, "%Y-%m-%d")
        fre = TIME_MAP[config.get_frequency()]
        date = DATE_TODAY - datetime.timedelta.days(fre)
        if(lt > date):
            return False
        return True

    @staticmethod
    def mode_judge(config):
        smode = config.get_mode()
        if smode == INCREMENT:
            return True
        return False