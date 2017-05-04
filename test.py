#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)

now = datetime.datetime.now()
print(str(datetime.datetime.now()))

startTime = datetime.timedelta(hours=9,minutes=00,seconds=00).total_seconds()
endTime = datetime.timedelta(hours=9,minutes=12,seconds=30).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=20,seconds=00).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=25,seconds=20).total_seconds()
wanna = 1
mesuLimit = [2]
rateLimit = 0.31
rateMLimit = 3.1
stdLimit = 2
sumEd = 0
gradient = 0
today = now.strftime('%Y-%m-%d')
oTimeindex = 0
completedCodes = []

print(today)


ti = sp.asarray([0, 1, 2, 3, 4, 5])
cg = sp.asarray([169, 168, 165, 164, 162, 160])
cg2 = sp.asarray([149, 148, 145, 144, 142, 140])
cg3 = sp.asarray([129, 128, 125, 124, 122, 120])


cgfit = sp.polyfit(ti, cg.astype(float), 1)
cggrad = sp.around(cgfit[0], decimals=2)
print(cggrad)


cgfit = sp.polyfit(ti, cg2.astype(float), 1)
cggrad = sp.around(cgfit[0], decimals=2)
print(cggrad)


cgfit = sp.polyfit(ti, cg3.astype(float), 1)
cggrad = sp.around(cgfit[0], decimals=2)
print(cggrad)

