# -*- coding: utf-8 -*-
from lib.db_manager import *
from lib.logger import *
from lib.config_load import *
import sys, os, datetime
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))  
CONFIG_PATH = ROOT_PATH + "/config"
LOG_PATH = ROOT_PATH + "/statis_log"


date = datetime.date.today().strftime("%Y-%m-%d")
LOG_FILE = LOG_PATH + "/" + date + ".log"
slogger = CLog(LOG_FILE)

DB_CONFIG_FILE = CONFIG_PATH + "/db.json"
try:
    db_config = DBConfig(DB_CONFIG_FILE)
except:
    slogger.error("read db_config error")
    sys.exit(0)

try:
    db_manager = DBManager(db_config)
except:
    slogger.error("connect db error")
    sys.exit(0)

STATISITC_CONFIG_FILE = CONFIG_PATH + "/statistic.json"
statis_config = StatisticConfig(STATISITC_CONFIG_FILE)

DATE_TODAY = datetime.date.today()