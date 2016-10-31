#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

today = datetime.datetime.now().strftime('%Y-%m-%d')
startTime = datetime.timedelta(hours=9,minutes=00,seconds=10).total_seconds()
endTime = datetime.timedelta(hours=15,minutes=19,seconds=30).total_seconds()
temp_sec = 0
while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    second_now = datetime.timedelta(hours=hour,minutes=minute,seconds=second).total_seconds()
    
    if((second_now - temp_sec) < 3):
        time.sleep(3 - (second_now - temp_sec))
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        second_now = datetime.timedelta(hours=hour,minutes=minute,seconds=second).total_seconds()

    temp_sec = second_now
    time.sleep(4)
    print(temp_sec)
    
