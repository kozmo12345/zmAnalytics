#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

def plot_models(x, cs, models, mstime, fname=None, mx=None, ymax=None, xmin=None):
    colors = ['g', 'k', 'b', 'm', 'r']
    linestyles = ['-', '-.', '--', ':', '-']

    plt.clf()
    plt.scatter(x, cs, s=20)
    plt.title("graph")
    plt.xlabel("Time")
    plt.ylabel("Rate")
    # mx = sp.linspace(0, x[-1], 1000)
    # plt.plot([mstime]*len(mx), mx, linestyle=':', linewidth=2, c='m')

    plt.legend(["d=%i" % m.order for m in models], loc="upper right")
    
    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    if ymax: 
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.xlim(xmax=max(x) + 10)
    plt.ylim(ymax=30)
    plt.grid(True, linestyle='-', color='0.75')
    plt.savefig(fname)

def toSecond(s):
    x = time.strptime(s.split(',')[0],'%H:%M:%S')
    return datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

dates = []
bcodes = []
mesutimes = []
medotimes = []

edFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + "ed.txt");
edFile = open(edFilePath, 'r')

for line in edFile:
    eds = line.split(',')
    dates.append(eds[0])
    bcodes.append(eds[3])
    mesutimes.append(eds[10])
    medotimes.append(eds[11])
print("end")            

for datei, da in enumerate(dates):
    
    date = da
    setcode = bcodes[datei] #b'038950'
    
    filePath = os.path.join("C:\\", "Dropbox\\Data\\" + date + "\\" + date + ".txt");
    data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')
    
    plusCnt = 0
    minusCnt = 0
    mesuCost = dict()
    upCost = dict()
    downCost = dict()
    
    exportData = data[data[:,7].astype(str) == bcodes[datei]]
    times = sp.unique(exportData[:,0])

    str_mesutime = mesutimes[datei]
    str_medotime = medotimes[datei]
    mst = time.strptime(str_mesutime, '%H:%M:%S')
    mdt = time.strptime(str_medotime, '%H:%M:%S')
    sec_mesutime = datetime.timedelta(hours=mst.tm_hour,minutes=mst.tm_min,seconds=mst.tm_sec).total_seconds()
    sec_medotime = datetime.timedelta(hours=mdt.tm_hour,minutes=mdt.tm_min,seconds=mdt.tm_sec).total_seconds()
    mesuIndex = 0
    medoIndex = 0

    for i, t in enumerate(times):
        x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
        nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        if(nt == sec_mesutime):
            mesuIndex = i
        if(nt == sec_medotime):
            medoIndex = i
            break;

    c = exportData[mesuIndex:medoIndex, 3].astype(float)

    img_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "grd_img")
    plot_models([x * 10 for x in range(len(c))], c, [], mstime = "" ,fname = os.path.join(img_dir, str(dates[datei])+ '_' +str(bcodes[datei]) + ".png"))