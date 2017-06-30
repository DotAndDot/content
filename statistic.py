# -*- coding: utf-8 -*-
from content_manage import *


if __name__ == "__main__":
    path = "./config/statistic.json"
    print manager.dbconfig_path
    sta = manager.StatisticManager(path)
    print sta