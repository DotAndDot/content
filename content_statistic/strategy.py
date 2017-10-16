# -*- coding: utf-8 -*-
from comm.statis_comm import *
from comm.statis_global import *
import os


class StatisStrategy(object):
    def __init__(self, stra):
        self.__strategy = stra

    def execute(self, par):
        self.__strategy.execute(par)


class CountStrategy(object):
    def handle_count_array(self, source, common_fields, field):
        cf = {}
        for it in common_fields:
            cf[it] = "$" + it
        array_field = "$" + field[:-2]
        pipeline = {
            "$group": {
                "_id" : cf,
                "total" : {
                    "$sum":{ "$size" : array_field}
                }
            }
        }
        res = db_manager.aggregate(source, pipeline)
        statis_res = []
        for cursor in res:
            temp = []
            temp.append(cursor['_id'])
            temp.append(cursor['total'])
            statis_res.append(temp)
        return statis_res
        pass
    
    def handle_count(self, source, common_fields):
        cf = {}
        for it in common_fields:
            cf[it] = "$" + it
        pipeline = {
            "$group": {
                "_id" : cf,
                "total" : {
                    "$sum":1
                }
            }
        }
        res = db_manager.aggregate(source, pipeline)
        statis_res = []
        for cursor in res:
            temp = []
            temp.append(cursor['_id'])
            temp.append(cursor['total'])
            statis_res.append(temp)
        return statis_res
        pass

    def execute(self, par):
        source = par.get_source()
        common_fields = par.get_common_fields()
        field = par.get_field()
        is_array = False
        if field:
            is_array = True
        name = par.get_name()

        if is_array:
            res = self.handle_count_array(source, common_fields, field)
        else:
            res = self.handle_count(source, common_fields)
        statis_res = {par.get_name(): res}
        return statis_res
        pass

class AddStrategy(object):
    def is_array(self, field):
        fs = field.split('.')
        if len(fs) == 1:
            return False
        if fs[0].end_with('[]'):
            return True
        return False

    def handle_add_array(self, source, common_fields, field):
        cf = {}
        for it in common_fields:
            cf[it] = "$" + it
        fs = field.split('.')
        fs[0] = fs[0][:-2]
        array_field = "$"
        for it in fs:
            array_field += it
        pipeline = {
            "$group": {
                "_id" : cf,
                "list" : {
                    "$push": array_field
                }
            }
        }
        res = db_manager.aggregate(source, pipeline)
        statis_res = []
        for cursor in res:
            temp = []
            temp.append(cursor['_id'])
            total = 0
            for i in cursor['list']:
                for ii in i:
                    total += ii
            temp.append(total)
            statis_res.append(temp)
        return statis_res
        pass
    
    def handle_add(self, source, common_fields, field):
        cf = {}
        for it in common_fields:
            cf[it] = "$" + it
        field += "$"
        pipeline = {
            "$group": {
                "_id" : cf,
                "total" : {
                    "$sum": field
                }
            }
        }
        res = db_manager.aggregate(source, pipeline)
        statis_res = []
        for cursor in res:
            temp = []
            temp.append(cursor['_id'])
            temp.append(cursor['total'])
            statis_res.append(temp)
        return statis_res
        pass

    def execute(self, par):
        source = par.get_source()
        common_fields = par.get_common_fields()
        field = par.get_field()
        is_array = self.is_array(field)
        name = par.get_name()

        if is_array:
            res = self.handle_add_array(source, common_fields, field)
        else:
            res = self.handle_add(source, common_fields, field)
        statis_res = {par.get_name(): res}
        return statis_res
        pass

class StorageStrategy(object):
    def get_file_size(self, filePath, size=0):
        for root, dirs, files in os.walk(filePath):
            for f in files:
                size += os.path.getsize(os.path.join(root, f))
                print(f)
        return size

    def execute(self, par):
        source = par.get_source()
        name = par.get_name()
        res = []
        for k,v in source.items():
            sto = self.get_file_size(v)
            res.append({
                k : sto
            })
        return res
        pass

def strategy_create(method):
    strategys = dict(
        count = StatisStrategy(CountStrategy()),
        plus = StatisStrategy(AddStrategy()),
        storage = StatisStrategy(StorageStrategy())
    )
    return strategys[method]