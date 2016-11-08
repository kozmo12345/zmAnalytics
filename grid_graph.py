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
    #     # if mx is None:
    #         # mx = sp.linspace(0, x[-1], 1000)
    #     for model, style, color in zip(models, linestyles, colors):
    #         plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

    plt.legend(["d=%i" % m.order for m in models], loc="upper right")

    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    if ymax: 
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.ylim(ymax=40)
    plt.grid(True, linestyle='-', color='0.75')
    plt.savefig(fname)

def toSecond(s):
    x = time.strptime(s.split(',')[0],'%H:%M:%S')
    return datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

dates = ['2016-09-21', '2016-09-21', '2016-09-22', '2016-09-22', '2016-09-22', '2016-09-23', '2016-09-23', '2016-09-23', '2016-09-23', '2016-09-26', '2016-09-26', '2016-09-26', '2016-09-28', '2016-09-28', '2016-09-28', '2016-09-28', '2016-09-28', '2016-09-29', '2016-09-29', '2016-09-29', '2016-09-30', '2016-09-30', '2016-10-04', '2016-10-04', '2016-10-05', '2016-10-05', '2016-10-05', '2016-10-05', '2016-10-06', '2016-10-06', '2016-10-06', '2016-10-07', '2016-10-07', '2016-10-07', '2016-10-07', '2016-10-11', '2016-10-11', '2016-10-11', '2016-10-12', '2016-10-12', '2016-10-12', '2016-10-12', '2016-10-12', '2016-10-12', '2016-10-13', '2016-10-13', '2016-10-13', '2016-10-14', '2016-10-17', '2016-10-18', '2016-10-18', '2016-10-19', '2016-10-19', '2016-10-19', '2016-10-20', '2016-10-20', '2016-10-21', '2016-10-21', '2016-10-21', '2016-10-21', '2016-10-24', '2016-10-24', '2016-10-24', '2016-10-25', '2016-10-26', '2016-10-26', '2016-10-26', '2016-10-26', '2016-10-27', '2016-10-27', '2016-10-28', '2016-10-28', '2016-10-31', '2016-10-31', '2016-10-31', '2016-10-31', '2016-10-31', '2016-11-01', '2016-11-01', '2016-11-01', '2016-11-01', '2016-11-02', '2016-11-02', '2016-11-02', '2016-11-02', '2016-11-02', '2016-11-02', '2016-11-02', '2016-11-03', '2016-11-03', '2016-11-03', '2016-11-03', '2016-11-03', '2016-11-03', '2016-11-03', '2016-11-03']

bcodes = [b'049120', b'007610', b'100660', b'025890', b'054540', b'100660', b'141020', b'049120', b'052600', b'106240', b'005030', b'054220', b'220260', b'036260', b'050890', b'053950', b'057030', b'012340', b'049120', b'006110', b'075970', b'081150', b'189860', b'002140', b'011500', b'131100', b'047440', b'081150', b'128820', b'017650', b'047440', b'004060', b'005030', b'080010', b'089150', b'196700', b'201490', b'226350', b'012690', b'208640', b'220260', b'049120', b'067730', b'089150', b'226350', b'032800', b'083470', b'201490', b'047400', b'035480', b'007190', b'011500', b'054300', b'079170', b'011320', b'032280', b'011810', b'001420', b'051170', b'053160', b'017040', b'900280', b'950140', b'046110', b'013000', b'201490', b'020180', b'050320', b'018700', b'051170', b'002140', b'086670', b'139050', b'002140', b'032860', b'069730', b'900280', b'200230', b'002140', b'026910', b'090150', b'011090', b'016670', b'201490', b'003060', b'049120', b'058220', b'090150', b'217730', b'037950', b'049120', b'053060', b'068330', b'069330', b'900280', b'900290']

mesutimes = ['09:02:56', '09:05:46', '09:11:39', '09:23:19', '09:01:49', '09:01:42', '09:44:12', '09:05:42', '09:11:12', '09:02:44', '09:05:04', '09:15:24', '09:31:10', '09:23:20', '09:10:20', '09:06:30', '09:07:20', '09:11:56', '09:16:56', '09:21:36', '09:02:03', '09:34:13', '09:13:06', '09:02:16', '09:03:26', '09:04:14', '09:04:32', '09:23:42', '09:34:42', '09:17:05', '09:38:02', '09:06:02', '09:07:23', '09:21:50', '09:19:54', '09:30:01', '09:19:01', '09:16:28', '09:38:42', '09:03:35', '09:09:20', '09:10:26', '09:02:26', '09:23:52', '09:15:27', '09:07:30', '09:40:40', '09:05:05', '09:12:47', '09:02:46', '09:10:49', '09:04:50', '09:25:51', '09:12:14', '09:13:12', '09:04:54', '09:17:17', '09:12:23', '09:01:49', '09:36:12', '09:06:28', '09:02:52', '09:02:31', '09:02:15', '09:17:41', '09:04:26', '09:03:44', '09:29:42', '09:06:47', '09:02:20', '09:07:29', '09:06:08', '09:02:30', '09:12:21', '09:10:51', '09:03:45', '09:06:12', '09:24:02', '09:03:09', '09:30:52', '09:07:27', '09:04:14', '09:09:23', '09:03:22', '09:20:40', '09:07:19', '09:07:46', '09:09:17', '09:48:40', '09:02:02', '09:08:53', '09:15:27', '09:10:53', '09:08:56', '09:20:40', '09:15:33']

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
    
    # fa = []
    seecode = ''
    sd = 0
    for ci, code in enumerate(codes):
        
        exportData = data[data[:,7] == code]
        # firstTime for time conver to index
        x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
        firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

        sec_mesutime = toSecond(mesutimes[datei])
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
        print(len(y))
        print(dates[datei])
        print(bcodes[datei])
        if(len(y) <= 1):
            break

        level = 1
        fit = sp.polyfit(ti[:mesuIndex+1], y, level)
        gradient = sp.around(fit[0]*10, decimals=2)
        f1 = sp.poly1d(fit)
        f2 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 3))
        f3 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 4))
        f10 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 15))
        f100 = sp.poly1d(sp.polyfit(ti[:mesuIndex+1], y, 30))

        img_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        plot_models(ti, c, msy, mdy, ry,[f1, f2, f3, f10, f100], mstime = ((sec_mesutime - firstSecond)/10) ,fname = os.path.join(img_dir, str(dates[datei])+ '_' +str(bcodes[datei]) + '_' + str(gradient) + ".png")) 