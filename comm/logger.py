# -*- coding: utf-8 -*-
import logging


class CLog(object):
    def __init__(self, path):
        self.__logger = logging.getLogger()
        self.__logger.setLevel(logging.INFO)
        self.__fh = logging.FileHandler(path, mode = 'w')
        self.__fh.setLevel(logging.INFO)
        self.__formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s") 
        self.__fh.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__fh)

    def debug(self, message):
        self.__logger.debug(message)

    def info(self, message):
        self.__logger.info(message)

    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)

    def critical(self, message):
        self.__logger.critical(message)


