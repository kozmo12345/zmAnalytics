#-*- coding: utf-8 -*-

import os
import datetime
from utils import DATA_DIR, CHART_DIR
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

date = "2016-09-23"
filePath = os.path.join("C:\\", "Data\\test.txt");
data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')

# code to analysis
code = b'5360'
data = data[data[:,7] == code]

# firstTime for time conver to index
x = time.strptime(data[0,0].decode('utf-8'), '%H:%M:%S')
firstTime = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

# t = list()
ti = sp.array([])
c = data[:, 3].astype(float)

timeFile = open(os.path.join("C:\\", "Data\\timeConver.txt"), 'w')
for i, v in enumerate(data[:,0]):
    x = time.strptime(v.decode('utf-8'), '%H:%M:%S')
    nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds() - firstTime
    ti = sp.append(ti, nt)
    timeFile.write(time.strftime("%H:%M:%S", x) + '\t' + str(nt) + '\n')
    # t = sp.append(t, [x, nt])

# print(t.size)
# print(c.size)
colors = ['g', 'k', 'b', 'm', 'r']
linestyles = ['-', '-.', '--', ':', '-']

# plt.figure(num=None, figsize=(8, 6))
plt.clf()
plt.plot(ti, c)
plt.title("Rate/Time")
plt.xlabel("Time")
plt.ylabel("Rate")
# plt.xticks(
#     [w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])

plt.autoscale(tight=True)
plt.ylim(ymin=0)
plt.grid(True, linestyle='-', color='0.75')
plt.show()

