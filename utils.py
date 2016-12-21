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
                msTime1 = times[i-1]
                msTime2 = times[i-2]
                break;

        for i, t in enumerate(times):
            x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
            nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            if(nt > sec_medotime):
                mdTime = t
                mdTime1 = times[i-1]
                mdTime2 = times[i-2]
                break;

        ttimeData = data[data[:,0] == msTime]
        ttimeData2 = ttimeData[ttimeData[:,1].astype(int) < 31]
        ttimeData3 = ttimeData2[ttimeData2[:,8].astype(float) > 1900]
        mscodes = ttimeData3[:,7]

        ttimeData4 = data[data[:,0] == mdTime]
        ttimeData5 = ttimeData4[ttimeData4[:,1].astype(int) < 31]
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

            data1 = data[data[:,0] == msTime1]
            data11 = data1[data1[:,7] == code]
            data2 = data[data[:,0] == msTime2]
            data22 = data2[data2[:,7] == code]

            codeData = data[data[:,7] == code]
            y = []
            for line in codeData:
                if(line[0] == msTime):
                    break;
                grade = line[1].astype(float) - codeData[0][1].astype(float)
                y.append(grade)

            if(len(y) <= 1):
                break
            level = 1
            fit = sp.polyfit(sp.arange(len(y)), y, level)
            gradient = sp.around(fit[0], decimals=2)

            ms = bb[0][3].astype(float)
            md = dd[0][3].astype(float)
            grade = bb[0][1].astype(float)
            gr = bb[0][4].astype(float)
            msr = bb[0][5].astype(float)
            mdr = bb[0][6].astype(float)
            rm = msr/mdr
            val = bb[0][8].astype(float)
            
            # if(len(data11) == 0):
            #     continue;
            # sms_md = sp.sum((msr + data11[0][5].astype(float))/(mdr + data11[0][6].astype(float)))

            if(rm > 1 and gradient > 0 and grade > 11):
                print(y)
                print(gradient)
                setFile.write( str(code) + ',' + str(md) + ',' + str(ms) +  ',' + str(md - ms) + ',' + str(grade) + ',' + str(gr) + ',' + str(msr) + ',' + str(mdr) + ',' + str(rm) + ',' + str(val) + ',' + str(gradient) + '\n')

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