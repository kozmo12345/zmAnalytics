#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

def plot_models(x, cs, msy, mdy, gry, models, mstime, fname=None, mx=None, ymax=None, xmin=None):
    colors = ['g', 'k', 'b', 'm', 'r']
    linestyles = ['-', '-.', '--', ':', '-']
    plt.clf()
    plt.scatter(x, cs, s=15)
    plt.title("graph")
    plt.xlabel("Time")
    plt.ylabel("Rate")
    plt.scatter(x, gry, s=5, marker='*', c=colors[0])
    # plt.scatter(x, msy, s=5, marker='_', c=colors[1])
    # plt.scatter(x, mdy, s=5, marker='.', c=colors[3])
    mx = sp.linspace(0, x[-1], 1000)
    plt.plot([mstime]*len(mx), mx, linestyle=':', linewidth=2, c='m')
    # if models:
    #     if mx is None:
      #      mx = sp.linspace(0, x[-1], 1000)
      #  for model, style, color in zip(models, linestyles, colors):
       #     plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

    plt.legend(["d=%i" % m.order for m in models], loc="upper right")
    
    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    if ymax: 
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.xlim(xmax=1000)
    plt.ylim(ymax=40)
    plt.grid(True, linestyle='-', color='0.75')
    plt.savefig(fname)

def toSecond(s):
    x = time.strptime(s.split(',')[0],'%H:%M:%S')
    return datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

dates = ['2016-09-21', '2016-09-21', '2016-09-22', '2016-09-22', '2016-09-23', '2016-09-23', '2016-09-26', '2016-09-26', '2016-09-28', '2016-09-28', '2016-09-28', '2016-09-30', '2016-10-04', '2016-11-23', '2016-11-24', '2016-11-28', '2016-11-28', '2016-11-28', '2016-11-28', '2016-11-28', '2016-11-29', '2016-11-29', '2016-11-30', '2016-12-01', '2016-12-05', '2016-12-06', '2016-12-07', '2016-12-08', '2016-12-09', '2016-12-09', '2016-12-09', '2016-12-13', '2016-12-14', '2016-12-15', '2016-12-15', '2016-12-15']

bcodes = [b'007610', b'049120', b'054540', b'100660', b'100660', b'052600', b'005030', b'106240', b'053950', b'057030', b'050890', b'075970', b'002140', b'128820', b'049120', b'130740', b'900280', b'224060', b'010470', b'900290', b'073490', b'006910', b'091440', b'224060', b'050890', b'214270', b'039980', b'109960', b'134580', b'053290', b'101390', b'130500', b'054180', b'033340', b'051170', b'122800']

mesutimes = ['09:03:36']

# dates = ['2016-10-13', '2016-09-30']

# bcodes = [b'032800', b'075970']

# mesutimes = ['09:08:03', '09:02:43']

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
    
    seecode = ''
    sd = 0
    for ci, code in enumerate(codes):
        
        exportData = data[data[:,7] == code]
        # firstTime for time conver to index
        x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
        firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

        sec_mesutime = toSecond(mesutimes[0])
        mesuIndex = 0
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
    
            ti = sp.append(ti, (v_time)/10)
            maxr = max(exportData[:i+1,5].astype(float))/30
            ry = ((exportData[:i+1,4].astype(float))/(max(exportData[:i+1,4].astype(float))))*30
            msy = (exportData[:i+1,5].astype(float))/maxr        
            mdy = (exportData[:i+1,6].astype(float))/maxr        
            rate = exportData[i, 3].decode('UTF-8')
            grade = int(exportData[i, 1].decode('UTF-8'))

            if(second < sec_mesutime):
                mesuIndex = i

        mesuIndex = mesuIndex+1
        y = exportData[:mesuIndex+1,3].astype(float)
        maxRate = max(exportData[mesuIndex:, 3].astype(float))
        mesuRate = exportData[mesuIndex,3].astype(float)
        print(len(y))
        print(dates[datei])
        print(bcodes[datei])
        if(len(y) <= 1):
            break

        level = 1
        fit = sp.polyfit(ti[:mesuIndex+1], y, 1)
        gradient = sp.around(fit[0]*10, decimals=2)
        f1 = sp.poly1d(fit)
        # f2 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 11))
        # f3 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 20))
        # f10 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 30))
        # f100 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 40))

        img_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "grd_img")
        plot_models(ti, c, msy, mdy, ry,[f1], mstime = ((sec_mesutime - firstSecond)/10) ,fname = os.path.join(img_dir, str(dates[datei])+ '_' +str(bcodes[datei].decode('utf-8')) + '_' + str(maxRate - mesuRate) + ".png")) 