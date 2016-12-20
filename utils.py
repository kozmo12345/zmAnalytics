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
endTime = datetime.timedelta(hours=9,minutes=2,seconds=00).total_seconds()
fMedoTime = datetime.timedelta(hours=9,minutes=18,seconds=00).total_seconds()
allMedoTime = datetime.timedelta(hours=9,minutes=19,seconds=00).total_seconds()
wanna = 1
mesuLimit = 2
rateLimit = 0.31
stdLimit = 2
sumEd = 0
originM = 2000000
for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        print(today)
        setFile = open(os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "moa4.txt"), 'w')
        realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + ".txt");
        
        data = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')
        codes = sp.unique(data[data[:,7] != b''][:,7])
        times = sp.unique(data[data[:,0] != b''][:,0])


        sec_mesutime = endTime
        sec_medotime = fMedoTime
        mesuIndex = 0
        medoIndex = 0
        msTime = times[20];
        mdTime = times[20];

        for i, t in enumerate(times):
            x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
            nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            if(nt > sec_mesutime):
                msTime = t
                break;

        for i, t in enumerate(times):
            x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
            nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            if(nt > sec_medotime):
                mdTime = t
                break;

        ttimeData = data[data[:,0] == msTime]
        ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 21]
        ttimeData3 = ttimeData2[ttimeData2[:,8].astype(float) > 1900]
        mscodes = ttimeData3[:,7]

        ttimeData4 = data[data[:,0] == mdTime]
        ttimeData5 = ttimeData4[ttimeData4[:,1].astype(int) < 21]
        ttimeData6 = ttimeData5[ttimeData5[:,8].astype(float) > 1900]
        mdcodes = ttimeData6[:,7]        
        
        for code in mscodes:
            if(code == b''):
                continue;
            if(not code in mdcodes):
                continue;

            aa = ttimeData3[ttimeData3[:,7] == code]
            bb = aa[aa[:,0] == msTime]
            cc = ttimeData6[ttimeData6[:,7] == code]
            dd = cc[cc[:,0] == mdTime]

            ms = bb[0][3].astype(float)
            md = dd[0][3].astype(float)
            if(md - ms > 3):
                setFile.write( str(code) + ',' + str(md) + ',' + str(ms) +  ',' + str(md - ms) +  '\n')

        print(today)

edFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + "good.txt");
edFile = open(edFilePath, 'w')

edFile.write('day' +  ',' + 'code' +  ',' + 'md' +  ',' + 'ms' +  ',' + 'ed' + '\n')

for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
    for subdirname in dirnames:
        today = subdirname

        setFilePath = os.path.join("C:\\", "Dropbox\\Data\\" + today + "\\" + today + "moa4.txt");
        setFile = open(setFilePath, 'r')
        
        for line in setFile:
            edFile.write(today + ',' + line)

print("end")            

now = datetime.datetime.now()
print(str(datetime.datetime.now()))