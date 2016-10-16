#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해


def plot_models(x, cs, gr, models, fname=None, mx=None, ymax=None, xmin=None):
    colors = ['g', 'k', 'b', 'm', 'r']
    linestyles = ['-', '-.', '--', ':', '-']
    plt.clf()
    plt.scatter(x, cs, s=10)
    plt.title("graph")
    plt.xlabel("Time")
    plt.ylabel("Rate")
    plt.scatter(x, gr, s=10, marker='*')
    
    # if models:
    #     if mx is None:
    #         mx = sp.linspace(0, x[-1], 100)
    #     for model, style, color in zip(models, linestyles, colors):
    #         plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

    #     plt.legend(["d=%i" % m.order for m in models], loc="upper left")

    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    if ymax:
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.ylim(ymax=30)        
    plt.grid(True, linestyle='-', color='0.75')
    plt.show()

date = '2016-09-21'
setcode = b'100090'

filePath = os.path.join("C:\\", "Dropbox\\Data\\" + date + "\\" + date + ".txt");
data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')

# code to analysis
codes = sp.unique(data[data[:,7] == setcode][:,7])
times = sp.unique(data[data[:,0] == setcode][:,0])

plusCnt = 0
minusCnt = 0
mesuCost = dict()
upCost = dict()
downCost = dict()

str_standardTime = datetime.timedelta(hours=9,minutes=2,seconds=00).total_seconds()
str_medoTime = datetime.timedelta(hours=15,minutes=20,seconds=00).total_seconds()

second_standardTime = 0
for i, t in enumerate(times):
    x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
    nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    second_standardTime = nt    
    if(nt > str_standardTime):
        str_standardTime = t.decode('utf-8')
        break;

second_medoTime = 0
for i, t in enumerate(times):
    x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
    nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    second_medoTime = nt
    if(nt > str_medoTime):
        str_medoTime = t.decode('utf-8')
        break;

fa = []
seecode = ''
sd = 0
for ci, code in enumerate(codes):
    # print(code.decode('utf-8'))
    # if(code.decode('utf-8') != "073240"):
    #     continue

    exportData = data[data[:,7] == code]
    # firstTime for time conver to index
    x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
    firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

    maxlist = sp.array([])
    ti = sp.array([])
    c = exportData[:, 3].astype(float)
    maxIndex = sp.argmax(c)
    maxTime = time.strptime(exportData[maxIndex,0].decode('utf-8'), '%H:%M:%S')
    maxSecond = datetime.timedelta(hours=maxTime.tm_hour,minutes=maxTime.tm_min,seconds=maxTime.tm_sec).total_seconds()
    minIndex = sp.argmin(c)
    minTime = time.strptime(exportData[minIndex,0].decode('utf-8'), '%H:%M:%S')
    minSecond = datetime.timedelta(hours=minTime.tm_hour,minutes=minTime.tm_min,seconds=minTime.tm_sec).total_seconds()
    for i, b_currentTime in enumerate(exportData[:,0]):
        t_currentTime = time.strptime(b_currentTime.decode('utf-8'), '%H:%M:%S')
        second = datetime.timedelta(hours=t_currentTime.tm_hour,minutes=t_currentTime.tm_min,seconds=t_currentTime.tm_sec).total_seconds()
        v_time = second - firstSecond

        ti = sp.append(ti, sp.sqrt(v_time)/2)
        maxr = (max(exportData[:,4].astype(float)))/30
        ry = (exportData[:i+1,4].astype(float))/maxr        
        rate = exportData[i, 3].decode('UTF-8')
        grade = int(exportData[i, 1].decode('UTF-8'))
    
    plot_models(ti, c, ry, fa)