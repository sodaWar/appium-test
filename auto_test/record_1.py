#coding=utf-8
import xlrd, hashlib, json
import os
import sys
import logging
# from email.mime.text import MIMEText
from email.header import Header
# from smtplib import SMTP_SSL
from flask import Flask

import requests
import threading
import multiprocessing


def match_reptile():
    try:
        for i in range(1000):
            values = {"userId": "d1209bbfbd104b31ba15141f1bc23b66", "tanentNo" : "100000"}
            re_url = "http://47.96.156.154:9030/execute?"
            # values = {"bid": 11230, "pid" : "9573477-1478443907"}
            # re_url = "http://buluo.qq.com/p/detail.html?"
            r = requests.get(url = re_url,params = values)
            print(r.status_code)
    except requests.exceptions.ConnectionError:
        match_reptile()

# 多线程
# 创建数组存放线程
# threads = []
# # 创建100个线程
# for i in range(100):
#     # 针对函数创建线程
#     t = threading.Thread(target=match_reptile, args=())
#     # 把创建的线程加入线程组
#     threads.append(t)
#
# if __name__ == '__main__':
#     # 启动线程
#     for i in threads:
#         i.start()
#         # keep thread
#     for i in threads:
#         i.join()


process = []
# 创建100个进程
for i in range(30):
    # 针对函数创建进程
    t = multiprocessing.Process(target=match_reptile, args=())
    # 把创建的进程加入进程组
    process.append(t)

if __name__ == '__main__':
    # 启动进程
    for i in process:
        i.start()
        # keep thread
    for i in process:
        i.join()


# # set up logging to file - see previous section for more details
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt='%m-%d %H:%M',
#                     filename='D:\\MyProgram\\AppiumProject\\appium-test\\auto_test\\interfaceLog.txt',
#                     filemode='w')
# # define a Handler which writes INFO messages or higher to the sys.stderr
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# # set a format which is simpler for console use
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# # tell the handler to use this format
# console.setFormatter(formatter)
# # add the handler to the root logger
# logging.getLogger('').addHandler(console)
#
# # Now, we can log to the root logger, or any other logger. First the root...
# logging.info('Jackdaws love my big sphinx of quartz.')
#
# # Now, define a couple of other loggers which might represent areas in your
# # application:
#
# logger1 = logging.getLogger('myapp.area1')
# logger2 = logging.getLogger('myapp.area2')
#
# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
# logger1.info('How quickly daft jumping zebras vex.')
# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
# logger2.error('The five boxing wizards jump quickly.')

