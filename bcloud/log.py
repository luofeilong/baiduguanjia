# Copyright (C) 2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html

import logging
from logging.handlers import RotatingFileHandler
import os
import sys

# def _init_logger(log_level, maxBytes=5*1024*1024, backupCount=5, logfile='~/.config/bcloud/bcloud.log'):
#     log_file = os.path.expanduser(logfile)
#     dir_name = os.path.dirname(log_file)
#     if not os.path.exists(dir_name):
#         try:
#             os.makedirs(dir_name)
#         except Exception:
#             sys.exit(1)
#     looger = logging.getLogger('bcloud')
#     file_handler = RotatingFileHandler(log_file, maxBytes=maxBytes,
#                                        backupCount=backupCount)
#     formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#     file_handler.setFormatter(formatter)
#     looger.addHandler(file_handler)
#     looger.setLevel(log_level)
#     return looger

#logger = _init_logger(logging.INFO, maxBytes=5*1024*1024, backupCount=5, logfile='d:/bcloud.log')


def configlogger(mylogger, log_level, maxBytes=5*1024*1024, backupCount=5, logfile="baiduguanjia"):
    log_file = os.path.expanduser(logfile)
    dir_name = os.path.dirname(log_file)
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except Exception:
            return False
    
    file_handler = RotatingFileHandler(log_file, maxBytes=maxBytes,
                                       backupCount=backupCount)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)
    mylogger.addHandler(file_handler)
    mylogger.setLevel(log_level)
    return True

logger = logging.getLogger('bcloud')