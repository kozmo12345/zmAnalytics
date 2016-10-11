#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        date = subdirname

        filePath = os.path.join("C:\\", "Dropbox\\Data\\" + date + "\\" + date + ".txt");
        data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')
        
        # code to analysis
        codes = sp.unique(data[data[:,7] != b''][:,7])
        times = sp.unique(data[data[:,0] != b''][:,0])
        maxFile = open(os.path.join("C:\\", "Data\\maxlist.txt"), 'w')
        # timeFile = open(os.path.join("C:\\", "Data\\timeConver.txt"), 'w')
        upFile = open(os.path.join("C:\\", "Data\\upList" + date + ".txt"), 'w')
        downFile = open(os.path.join("C:\\", "Data\\downList" + date + ".txt"), 'w')
        
        plusCnt = 0
        minusCnt = 0
        mesuCost = dict()
        upCost = dict()
        downCost = dict()
        
        str_standardTime = datetime.timedelta(hours=9,minutes=2,seconds=00).total_seconds()
        str_medoTime = datetime.timedelta(hours=9,minutes=10,seconds=00).total_seconds()
        
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
        
        for i, code in enumerate(codes):
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
                ti = sp.append(ti, v_time)
                # timeFile.write(time.strftime("%H:%M:%S", t_currentTime) + '\t' + str(v_time) + '\n')
                rate = exportData[i, 3].decode('UTF-8')
                grade = int(exportData[i, 1].decode('UTF-8'))
        
                if(b_currentTime.decode('utf-8') == str_standardTime and grade < 15 ):
                    mesuCost[code.decode('utf-8')] = float(rate)
                    upCost[code.decode('utf-8')] = float(rate)
                    downCost[code.decode('utf-8')] = float(rate)
                    # maxFile.write(b_currentTime.decode('utf-8') + '\t' + '\t' + rate + '\t' + exportData[maxIndex,0].decode('utf-8') + '\t' + str(c[maxIndex]) + '\t' + code.decode('UTF-8') + '\n')
                    if(maxSecond > second):
                        # if(exportData[i, 3].astype(float) > 5.0):
                        #     print(exportData[i, 3].astype(float), c[maxIndex], c[maxIndex] - exportData[i, 3].astype(float))
                        plusCnt = plusCnt + 1
                    elif(maxSecond <= second):
                        # if(exportData[i, 3].astype(float) > 5.0):
                        #     print(exportData[i, 3].astype(float), c[maxIndex], c[maxIndex] - exportData[i, 3].astype(float))
                        minusCnt = minusCnt + 1
        
                if(second_standardTime < second and second <= second_medoTime and code.decode('utf-8') in upCost and upCost[code.decode('utf-8')] < float(rate)):
                    upCost[code.decode('utf-8')] = float(rate)
                elif(second_standardTime < second and second <= second_medoTime and code.decode('utf-8') in downCost and downCost[code.decode('utf-8')] >= float(rate)):
                    downCost[code.decode('utf-8')] = float(rate)
        
        for k, v in upCost.items():
            upFile.write( str(k) + ' ' + str(mesuCost[k]) + ' ' + str(v) + ' ' + str(v - mesuCost[k]) + '\n')
        
        for k, v in downCost.items():
            downFile.write( str(k) + ' ' + str(mesuCost[k]) + ' ' + str(v) + ' ' + str(v - mesuCost[k]) + '\n')      
        # print(plusCnt, minusCnt)
            # plt.clf()
            # plt.plot(ti, c)
            # plt.title("Rate/Time")
            # plt.xlabel("Time")
            # plt.ylabel("Rate")
            # plt.autoscale(tight=True)
            # plt.ylim(ymin=0)
            # plt.grid(True, linestyle='-', color='0.75')
            # plt.show()