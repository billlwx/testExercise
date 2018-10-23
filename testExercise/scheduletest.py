#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/9/14
import os

import datetime
import schedule
import time


def job1():
    print("I'm working for job1")
    time.sleep(2)
    # n = os.system('/app/sh/consumer.sh')
    print("job1:", datetime.datetime.now())

def job2():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())

schedule.every(2).seconds.do(job1)
schedule.every(2).seconds.do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)