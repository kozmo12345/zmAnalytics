#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

mstimes = [
    datetime.timedelta(hours=9,minutes=2,seconds=00).total_seconds(),
    datetime.timedelta(hours=9,minutes=2,seconds=05).total_seconds(),
    datetime.timedelta(hours=9,minutes=2,seconds=10).total_seconds(),
    datetime.timedelta(hours=9,minutes=2,seconds=15).total_seconds(),
]
for mesui, mstime in enumerate(mstimes):
    dataFile = open(os.path.join("C:\\", "Test\\test" + str(mesui) + ".txt"), 'w')
    dataFile.write( 'date,grade,code,mesur,medor,msr_mdr,sgrad,ssd,grad,sd,srgrad,srsd,rgrad,rsd,gr,mesu,maxc_msc,10c_msc,20c_msc,30c_msc,msc_min10c,msc_min20c,msc_min30c,max,min,cost\n')
    for dirname, dirnames, filenames in os.walk("C:\\Test\\"):
        for subdirname in dirnames:
            date = subdirname
    
            filePath = os.path.join("C:\\", "Test\\" + date + "\\" + date + ".txt");
            data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')

            realfilePath = os.path.join("C:\\", "Dropbox\\Data\\" + date + "\\" + date + ".txt");
            realdata = sp.genfromtxt(realfilePath, delimiter="\t", dtype='|S20')

            realcodes = sp.unique(realdata[realdata[:,7] != b''][:,7])
            codes = sp.unique(data[data[:,7] != b''][:,7])
            times = sp.unique(data[data[:,0] != b''][:,0])
            
            plusCnt = 0
            minusCnt = 0
            mesuCost = dict()
            upCost = dict()
            downCost = dict()
            maxCost = dict()
            minCost = dict()
            tenCost = dict()
            ten2Cost = dict()
            ten3Cost = dict()
            sd = dict()   #cost증가율 1차 편차
            ssd = dict()  #cost증가율 2차 편차
            rsd = dict()  #r증가율 1차 편차
            srsd = dict() #r증가율 2차 편차
            grd = dict() #r량
            gradient = dict() #cost증가율 1차
            sgradient = dict() #cost증가율 2차
            rgradient = dict() #r증가율 1차
            srgradient = dict()#r증가율 2차
            gradeDic = dict() #등급
            Cost = dict() #가격
            mesur = dict() #수량 1차
            medor = dict() #도량 1차
            mesur_medor = dict() #수량/도량 증가율 1차
            mintenCost = dict()
            minten2Cost = dict()
            minten3Cost = dict()

            str_standardTime = mstime
            str_medoTime = datetime.timedelta(hours=15,minutes=20,seconds=00).total_seconds()
            str_tenTime = datetime.timedelta(hours=9,minutes=10,seconds=00).total_seconds()
            str_ten2Time = datetime.timedelta(hours=9,minutes=20,seconds=00).total_seconds()
            str_ten3Time = datetime.timedelta(hours=9,minutes=30,seconds=00).total_seconds()
            
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
            
            second_tenTime = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_tenTime = nt
                if(nt > str_tenTime):
                    str_tenTime = t.decode('utf-8')
                    break;
            
            second_ten2Time = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_ten2Time = nt
                if(nt > str_ten2Time):
                    str_ten2Time = t.decode('utf-8')
                    break;
            
            second_ten3Time = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_ten3Time = nt
                if(nt > str_ten3Time):
                    str_ten3Time = t.decode('utf-8')
                    break;
            
            for ci, code in enumerate(codes):
                exportData = data[data[:,7] == code]
                realexportData = realdata[realdata[:,7] == code]
            
                # firstTime for time conver to index
                x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
                firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            
                maxlist = sp.array([])
                ti = sp.array([])
                ms_md = sp.array([])
                c = exportData[:, 3].astype(float)
                realc = realexportData[:, 3].astype(float)
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
                    rate = exportData[i, 3].decode('UTF-8')
                    grade = int(exportData[i, 1].decode('UTF-8'))
                    cost = int(exportData[i, 8].decode('UTF-8'))
                    gr = int(exportData[i, 4].decode('UTF-8'))
                    ms =  int(exportData[i, 5].decode('UTF-8'))
                    md =  int(exportData[i, 6].decode('UTF-8'))
    
                    if(b_currentTime.decode('utf-8') == str_standardTime and grade < 6 and ms != 0 and md != 0):
                        x = ti
                        y = exportData[:i+1,3].astype(float)
                        if(len(y) <= 1):
                            continue
                        level = 1
                        fit = sp.polyfit(x, y, level)
                        sd[code.decode('utf-8')] = (sp.std(sp.array([x, y])))*10
                        gradient[code.decode('utf-8')] = sp.around(fit[0]*10, decimals=2)
    
                        slist = [b - a for a,b in zip(y,y[1:])]
                        sfit = sp.polyfit(x[:-1], slist, level)
                        ssd[code.decode('utf-8')] = (sp.std(sp.array([x[:-1], slist])))*10
                        sgradient[code.decode('utf-8')] = sp.around(sfit[0]*10, decimals=2)
    
                        maxr = (max(exportData[:,4].astype(float)))/30
                        ry = (exportData[:i+1,4].astype(float))/maxr
                        rfit = sp.polyfit(x, ry, level)
                        rsd[code.decode('utf-8')] = (sp.std(sp.array([x, ry])))*10
                        rgradient[code.decode('utf-8')] = sp.around(rfit[0]*10, decimals=2)
    
                        mesuy = (exportData[:i+1,5].astype(float))/maxr
                        msfit = sp.polyfit(x, mesuy, level)
                        mesur[code.decode('utf-8')] = sp.around(msfit[0]*10, decimals=2)
                        medoy = (exportData[:i+1,6].astype(float))/maxr
                        mdfit = sp.polyfit(x, medoy, level)
                        medor[code.decode('utf-8')] = sp.around(mdfit[0]*10, decimals=2)
                        ms_mdfit = sp.polyfit(x, mesuy, level)
                        mesur_medor[code.decode('utf-8')] = sp.around(ms_mdfit[0]*10, decimals=2)

                        srlist = [b - a for a,b in zip(ry,ry[1:])]
                        srfit = sp.polyfit(x[:-1], srlist, level)
                        srsd[code.decode('utf-8')] = (sp.std(sp.array([x[:-1], srlist])))*10
                        srgradient[code.decode('utf-8')] = sp.around(srfit[0]*10, decimals=2)
    
                        mesuCost[code.decode('utf-8')] = float(rate)
                        upCost[code.decode('utf-8')] = float(rate)
                        downCost[code.decode('utf-8')] = float(rate)
                        tenCost[code.decode('utf-8')] = float(rate)
                        ten2Cost[code.decode('utf-8')] = float(rate)
                        ten3Cost[code.decode('utf-8')] = float(rate)
                        mintenCost[code.decode('utf-8')] = float(rate)
                        minten2Cost[code.decode('utf-8')] = float(rate)
                        minten3Cost[code.decode('utf-8')] = float(rate)
                        maxCost[code.decode('utf-8')] = max(realc)
                        minCost[code.decode('utf-8')] = min(c)
                        gradeDic[code.decode('utf-8')] = grade
                        Cost[code.decode('utf-8')] = cost
                        grd[code.decode('utf-8')] = gr

                    if(second_standardTime < second and second <= second_tenTime and code.decode('utf-8') in tenCost and tenCost[code.decode('utf-8')] < float(rate)):
                        tenCost[code.decode('utf-8')] = float(rate)
    
                    if(second_standardTime < second and second <= second_tenTime and code.decode('utf-8') in mintenCost and mintenCost[code.decode('utf-8')] >= float(rate)):
                        mintenCost[code.decode('utf-8')] = float(rate) 
            
                    if(second_tenTime < second and second <= second_ten2Time and code.decode('utf-8') in ten2Cost and ten2Cost[code.decode('utf-8')] < float(rate)):
                        ten2Cost[code.decode('utf-8')] = float(rate)
            
                    if(second_tenTime < second and second <= second_ten2Time and code.decode('utf-8') in minten2Cost and minten2Cost[code.decode('utf-8')] >= float(rate)):
                        minten2Cost[code.decode('utf-8')] = float(rate)         
    
                    if(second_ten2Time < second and second <= second_ten3Time and code.decode('utf-8') in ten3Cost and ten3Cost[code.decode('utf-8')] < float(rate)):
                        ten3Cost[code.decode('utf-8')] = float(rate)
    
                    if(second_ten2Time < second and second <= second_ten3Time and code.decode('utf-8') in minten3Cost and minten3Cost[code.decode('utf-8')] >= float(rate)):
                        minten3Cost[code.decode('utf-8')] = float(rate)         
            
                    if(second_standardTime < second and second <= str_medoTime and code.decode('utf-8') in maxCost and maxCost[code.decode('utf-8')] < float(rate)):
                        maxCost[code.decode('utf-8')] = float(rate)        
            
                    if(second_standardTime < second and second <= str_medoTime and code.decode('utf-8') in minCost and minCost[code.decode('utf-8')] >= float(rate)):
                        minCost[code.decode('utf-8')] = float(rate)                                          
            
            
            for k, v in mesuCost.items():
                dataFile.write( date + ',' + str(gradeDic[k]) + ',' + str(k) + ',' + str(mesur[k]) + ',' + str(medor[k]) + ',' + str(mesur_medor[k]) + ',' + str(sgradient[k]) + ',' + str(ssd[k]) + ',' + str(gradient[k]) + ',' + str(sd[k]) + ',' + str(srgradient[k]) + ',' + str(srsd[k]) + ',' + str(rgradient[k]) + ',' + str(rsd[k]) + ',' + str(grd[k]) + ',' + str(v) + ',' + str(maxCost[k]-mesuCost[k]) + ',' + str(tenCost[k]-mesuCost[k]) + ',' + str(ten2Cost[k]-mesuCost[k]) + ',' + str(ten3Cost[k]-mesuCost[k]) + ',' + str(mintenCost[k] - mesuCost[k]) + ',' + str(minten2Cost[k] - mesuCost[k]) + ',' + str(minten3Cost[k] - mesuCost[k]) + ',' + str(maxCost[k]) + ',' + str(minCost[k]) + ',' + str(Cost[k]) + '\n')