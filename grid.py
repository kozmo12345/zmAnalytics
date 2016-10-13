#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

date = '2016-09-26'

filePath = os.path.join("C:\\", "Dropbox\\Data\\" + date + "\\" + date + ".txt");
data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')

# code to analysis
codes = sp.unique(data[data[:,7] != b''][:,7])
times = sp.unique(data[data[:,0] != b''][:,0])

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

for ci, code in enumerate(codes):
    exportData = data[data[:,7] == code]

    # firstTime for time conver to index
    x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
    firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

    maxlist = sp.array([])
    ti = sp.array([])
    f_rate = exportData[:, 3].astype(float)
    f_mean_rate = sp.mean(f_rate)
    f_volume = exportData[:, 4].astype(int)
    f_mean_volume = sp.mean(f_volume)
    f_mesur = exportData[:, 5].astype(int)
    f_mean_mesur = sp.mean(f_mesur)
    f_medor = exportData[:, 6].astype(int)
    f_mean_medor = sp.mean(f_medor)
    maxIndex = sp.argmax(f_rate)
    maxTime = time.strptime(exportData[maxIndex,0].decode('utf-8'), '%H:%M:%S')
    maxSecond = datetime.timedelta(hours=maxTime.tm_hour,minutes=maxTime.tm_min,seconds=maxTime.tm_sec).total_seconds()
    minIndex = sp.argmin(f_rate)
    minTime = time.strptime(exportData[minIndex,0].decode('utf-8'), '%H:%M:%S')
    minSecond = datetime.timedelta(hours=minTime.tm_hour,minutes=minTime.tm_min,seconds=minTime.tm_sec).total_seconds()

    for i, b_currentTime in enumerate(exportData[:,0]):
        t_currentTime = time.strptime(b_currentTime.decode('utf-8'), '%H:%M:%S')
        second = datetime.timedelta(hours=t_currentTime.tm_hour,minutes=t_currentTime.tm_min,seconds=t_currentTime.tm_sec).total_seconds()
        v_time = second - firstSecond
        ti = sp.append(ti, v_time)
        str_currentRate = exportData[i, 3].decode('UTF-8')
        grade = int(exportData[i, 1].decode('UTF-8'))

        if(b_currentTime.decode('utf-8') == str_standardTime and grade < 15 ):
            mesuCost[code.decode('utf-8')] = float(str_currentRate)
            upCost[code.decode('utf-8')] = float(str_currentRate)
            downCost[code.decode('utf-8')] = float(str_currentRate)

        if(second_standardTime < second and second <= second_medoTime and code.decode('utf-8') in upCost and upCost[code.decode('utf-8')] < float(str_currentRate)):
            upCost[code.decode('utf-8')] = float(str_currentRate)
        elif(second_standardTime < second and second <= second_medoTime and code.decode('utf-8') in downCost and downCost[code.decode('utf-8')] >= float(str_currentRate)):
            downCost[code.decode('utf-8')] = float(str_currentRate)

    if(ci == 124):
        plt.clf()
        plt.plot(ti, (f_rate/f_mean_rate)*10, 'r-', ti, (f_volume/f_mean_volume)*10, 'b-', ti, (f_mesur/f_mean_mesur)*10, 'g-', ti, (f_medor/f_mean_medor)*10, 'y-')
        # plt.plot(ti, f_rate)
        plt.title("ZM")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.autoscale(tight=True)
        plt.ylim(ymin=0)
        plt.grid(True, linestyle='-', color='0.75')
        plt.show()