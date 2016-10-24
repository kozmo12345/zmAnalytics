#-*- coding: utf-8 -*-

import os
import datetime
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import time 

sp.random.seed(3)  # 이후에 같은 데이터를 생성하기 위해

mstimes = [
    datetime.timedelta(hours=9,minutes=00,seconds=50).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=00).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=10).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=20).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=30).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=35).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=40).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=45).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=50).total_seconds(),
    datetime.timedelta(hours=9,minutes=1,seconds=55).total_seconds(),
    datetime.timedelta(hours=9,minutes=2,seconds=00).total_seconds(),
    datetime.timedelta(hours=9,minutes=2,seconds=10).total_seconds(),
]

dataFile = open(os.path.join("C:\\", "Data\\alldata" + ".txt"), 'w')
dataFile.write( 'date,grade,code,mesur,medor,msr_mdr,smesur,smedor,smsr_mdr,sgrad,ssd,grad,sd,second, srgrad,srsd,rgrad,rsd,gr,mesu,maxc_msc,3c_msc,5c_msc,7c_msc,10c_msc,15c_msc,20c_msc,30c_msc,msc_min10c,msc_min20c,msc_min30c,max,min,cost\n')

for mesui, mstime in enumerate(mstimes):
    for dirname, dirnames, filenames in os.walk("C:\\Dropbox\\Data\\"):
        for subdirname in dirnames:
            date = subdirname
    
            filePath = os.path.join("C:\\", "Dropbox\\Data\\" + date + "\\" + date + ".txt");
            data = sp.genfromtxt(filePath, delimiter="\t", dtype='|S20')
            
            codes = sp.unique(data[data[:,7] != b''][:,7])
            times = sp.unique(data[data[:,0] != b''][:,0])
            
            plusCnt = 0
            minusCnt = 0
            mesuCost = dict()
            upCost = dict()
            downCost = dict()
            maxCost = dict()
            minCost = dict()
            trCost = dict()
            fiCost = dict()
            seCost = dict()
            tenCost = dict()
            tenfCost = dict()
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
            mesur = dict() #수량
            medor = dict() #도량
            mesur_medor = dict() #수량/도량 
            smesur = dict() #수량 sum
            smedor = dict() #도량 sum
            smesur_medor = dict() #수량/도량 sum            
            mintenCost = dict()
            minten2Cost = dict()
            minten3Cost = dict()
            mesusecond = dict()

            str_standardTime = mstime
            str_medoTime = datetime.timedelta(hours=15,minutes=20,seconds=00).total_seconds()
            str_trTime = datetime.timedelta(hours=9,minutes=3,seconds=00).total_seconds()
            str_fiTime = datetime.timedelta(hours=9,minutes=5,seconds=00).total_seconds()
            str_seTime = datetime.timedelta(hours=9,minutes=7,seconds=00).total_seconds()
            str_tenTime = datetime.timedelta(hours=9,minutes=10,seconds=00).total_seconds()
            str_tenfTime = datetime.timedelta(hours=9,minutes=15,seconds=00).total_seconds()
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
            
            second_trTime = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_trTime = nt
                if(nt > str_trTime):
                    str_trTime = t.decode('utf-8')
                    break;            
            
            second_fiTime = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_fiTime = nt
                if(nt > str_fiTime):
                    str_fiTime = t.decode('utf-8')
                    break;

            second_seTime = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_seTime = nt
                if(nt > str_seTime):
                    str_seTime = t.decode('utf-8')
                    break;

            second_tenTime = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_tenTime = nt
                if(nt > str_tenTime):
                    str_tenTime = t.decode('utf-8')
                    break;

            second_tenfTime = 0
            for i, t in enumerate(times):
                x = time.strptime(t.decode('utf-8'), '%H:%M:%S')
                nt = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                second_tenfTime = nt
                if(nt > str_tenfTime):
                    str_tenfTime = t.decode('utf-8')
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
            
                # firstTime for time conver to index
                x = time.strptime(exportData[0,0].decode('utf-8'), '%H:%M:%S')
                firstSecond = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            
                maxlist = sp.array([])
                ti = sp.array([])
                ms_md = sp.array([])
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
                    rate = exportData[i, 3].decode('UTF-8')
                    grade = int(exportData[i, 1].decode('UTF-8'))
                    cost = int(exportData[i, 8].decode('UTF-8'))
                    gr = int(exportData[i, 4].decode('UTF-8'))
                    ms =  int(exportData[i, 5].decode('UTF-8'))
                    md =  int(exportData[i, 6].decode('UTF-8'))
    
                    if(b_currentTime.decode('utf-8') == str_standardTime and grade < 20):
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
    
                        # maxr = exportData[i,4].astype(float)/30
                        maxr = 100000
                        ry = (exportData[:i+1,4].astype(float))/maxr
                        rfit = sp.polyfit(x, ry, level)
                        rsd[code.decode('utf-8')] = (sp.std(sp.array([x, ry])))*10
                        rgradient[code.decode('utf-8')] = sp.around(rfit[0]*10, decimals=2)
    
                        mesuy = (exportData[:i+1,5].astype(float))/maxr
                        msfit = sp.polyfit(x, mesuy, level)
                        mesur[code.decode('utf-8')] = exportData[i,5].astype(float)
                        smesur[code.decode('utf-8')] = sp.sum(exportData[:i+1,5].astype(float))
                        medoy = (exportData[:i+1,6].astype(float))/maxr
                        mdfit = sp.polyfit(x, medoy, level)
                        medor[code.decode('utf-8')] = exportData[i,6].astype(float)
                        smedor[code.decode('utf-8')] = sp.sum(exportData[:i+1,6].astype(float))
                        ms_md = sp.append(ms_md, (mesuy.astype(float))/(medoy.astype(float)))
                        ms_mdfit = sp.polyfit(x, mesuy, level)
                        mesur_medor[code.decode('utf-8')] = (mesur[code.decode('utf-8')])/(medor[code.decode('utf-8')])
                        smesur_medor[code.decode('utf-8')] = sp.sum((smesur[code.decode('utf-8')])/(smedor[code.decode('utf-8')]))
                        
                        srlist = [b - a for a,b in zip(ry,ry[1:])]
                        srfit = sp.polyfit(x[:-1], srlist, level)
                        srsd[code.decode('utf-8')] = (sp.std(sp.array([x[:-1], srlist])))*10
                        srgradient[code.decode('utf-8')] = sp.around(srfit[0]*10, decimals=2)
                        mesusecond[code.decode('utf-8')] = mstime
                        mesuCost[code.decode('utf-8')] = float(rate)
                        upCost[code.decode('utf-8')] = float(rate)
                        downCost[code.decode('utf-8')] = float(rate)
                        trCost[code.decode('utf-8')] = float(rate)
                        fiCost[code.decode('utf-8')] = float(rate)
                        seCost[code.decode('utf-8')] = float(rate)
                        tenCost[code.decode('utf-8')] = float(rate)
                        tenfCost[code.decode('utf-8')] = float(rate)
                        ten2Cost[code.decode('utf-8')] = float(rate)
                        ten3Cost[code.decode('utf-8')] = float(rate)
                        mintenCost[code.decode('utf-8')] = float(rate)
                        minten2Cost[code.decode('utf-8')] = float(rate)
                        minten3Cost[code.decode('utf-8')] = float(rate)
                        maxCost[code.decode('utf-8')] = max(c)
                        minCost[code.decode('utf-8')] = min(c)
                        gradeDic[code.decode('utf-8')] = grade
                        Cost[code.decode('utf-8')] = cost
                        grd[code.decode('utf-8')] = gr

                    if(second_standardTime < second and second <= second_trTime and code.decode('utf-8') in trCost and trCost[code.decode('utf-8')] < float(rate)):
                        trCost[code.decode('utf-8')] = float(rate)

                    if(second_trTime < second and second <= second_fiTime and code.decode('utf-8') in fiCost and fiCost[code.decode('utf-8')] < float(rate)):
                        fiCost[code.decode('utf-8')] = float(rate)

                    if(second_fiTime < second and second <= second_seTime and code.decode('utf-8') in seCost and seCost[code.decode('utf-8')] < float(rate)):
                        seCost[code.decode('utf-8')] = float(rate)

                    if(second_seTime < second and second <= second_tenTime and code.decode('utf-8') in tenCost and tenCost[code.decode('utf-8')] < float(rate)):
                        tenCost[code.decode('utf-8')] = float(rate)

                    if(second_seTime < second and second <= second_tenTime and code.decode('utf-8') in mintenCost and mintenCost[code.decode('utf-8')] >= float(rate)):
                        mintenCost[code.decode('utf-8')] = float(rate) 

                    if(second_tenTime < second and second <= second_tenfTime and code.decode('utf-8') in tenfCost and tenfCost[code.decode('utf-8')] < float(rate)):
                        tenfCost[code.decode('utf-8')] = float(rate)

                    if(second_tenfTime < second and second <= second_ten2Time and code.decode('utf-8') in ten2Cost and ten2Cost[code.decode('utf-8')] < float(rate)):
                        ten2Cost[code.decode('utf-8')] = float(rate)
            
                    if(second_tenfTime < second and second <= second_ten2Time and code.decode('utf-8') in minten2Cost and minten2Cost[code.decode('utf-8')] >= float(rate)):
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
                dataFile.write( date + ',' + str(gradeDic[k]) + ',' + str(k) + ',' + str(mesur[k]) + ',' + str(medor[k]) + ',' + str(mesur_medor[k]) + ',' + str(smesur[k]) + ',' + str(smedor[k]) + ',' + str(smesur_medor[k]) + ',' + str(sgradient[k]) + ',' + str(ssd[k]) + ',' + str(gradient[k]) + ',' + str(sd[k]) + ',' + str(mesusecond[k]) +  ',' + str(srgradient[k]) + ',' + str(srsd[k]) + ',' + str(rgradient[k]) + ',' + str(rsd[k]) + ',' + str(grd[k]) + ',' + str(v) + ',' + str(maxCost[k]-mesuCost[k]) + ',' + str(trCost[k]-mesuCost[k]) + ',' + str(fiCost[k]-mesuCost[k]) + ',' + str(seCost[k]-mesuCost[k]) + ',' + str(tenCost[k]-mesuCost[k]) + ',' + str(tenfCost[k]-mesuCost[k]) + ',' + str(ten2Cost[k]-mesuCost[k]) + ',' + str(ten3Cost[k]-mesuCost[k]) + ',' + str(mintenCost[k] - mesuCost[k]) + ',' + str(minten2Cost[k] - mesuCost[k]) + ',' + str(minten3Cost[k] - mesuCost[k]) + ',' + str(maxCost[k]) + ',' + str(minCost[k]) + ',' + str(Cost[k]) + '\n')