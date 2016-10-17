#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해


def plot_models(x, cs, msy, mdy, models, fname=None, mx=None, ymax=None, xmin=None):
    colors = ['g', 'k', 'b', 'm', 'r']
    linestyles = ['-', '-.', '--', ':', '-']
    plt.clf()
    plt.scatter(x, cs, s=15)
    plt.title("graph")
    plt.xlabel("Time")
    plt.ylabel("Rate")
    plt.scatter(x, msy, s=15, marker='*')
    plt.scatter(x, mdy, s=15, marker='_')
    
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
    plt.savefig(fname)
    # plt.show()

dates = [
 "2016-09-21", "2016-09-21", "2016-09-22", "2016-09-23", "2016-09-23", "2016-09-23", "2016-09-23", "2016-09-27", "2016-09-27", "2016-09-27", "2016-09-27", "2016-09-29", "2016-09-30", "2016-09-30", "2016-10-04", "2016-10-05", "2016-10-05", "2016-10-06", "2016-10-06", "2016-10-06", "2016-10-06", "2016-10-07", "2016-10-07", "2016-10-10", "2016-10-11", "2016-10-12", "2016-10-12", "2016-10-13", "2016-10-14", "2016-10-14", "2016-10-17"
]

bcodes = [
 b'038950', b'049120', b'102710', b'007610', b'100660', b'078860', b'134060', b'100660', b'049120', b'089600', b'095570', b'036620', b'015710', b'075970', b'044450', b'011500', b'021650', b'042370', b'017650', b'049480', b'047400', b'065650', b'049120', b'003960', b'201490', b'010420', b'067730', b'035620', b'030270', b'005620', b'090360'
]

rates = [
 "0.9", "18.9", "4.1", "2.3", "5.2", "3.2", "5.2", "20.2", "5.8", "8.6", "1.0", "0.7", "3.7", "10.7", "1.69", "18.82", "2.62", "1.22", "24.03", "0.24", "3.30", "1.85", "15.88", "9.62", "16.31", "2.41", "2.21", "4.83", "7.03", "15.98", "1.66"
]

for datei, da in enumerate(dates):
    
    date = da
    setcode = bcodes[datei] #b'038950'
    
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
            msy = (exportData[:i+1,5].astype(float))/maxr        
            mdy = (exportData[:i+1,6].astype(float))/maxr        
            rate = exportData[i, 3].decode('UTF-8')
            grade = int(exportData[i, 1].decode('UTF-8'))
        
        img_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        plot_models(ti, c, msy, mdy, fa, fname = os.path.join(img_dir, rates[datei] +".png")) 