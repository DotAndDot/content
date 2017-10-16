# -*- coding: utf-8 -*-
from comm.statis_comm import *
from content_statistic.manager import *
import sys, datetime

if __name__ == "__main__":
    parament = {}
    for i in range(1, len(sys.argv)):
        if sys.argv[i].startswith('-'):
            parament[sys.argv[i]] = sys.argv[i + 1]
            i += 1
    if parament.has_key('-d'):
        try:
            DATE_TODAY = datetime.datetime.strftime("%Y-%m-%d", parament['-d'])
        except:
            pass
    for con in statis_config:
        m = StatisticManager(con)
        m.run()