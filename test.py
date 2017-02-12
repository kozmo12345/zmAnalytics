
                        sumsd = exportData[:i+1,5].astype(float)/exportData[:i+1,6].astype(float)
                        sumfit = sp.polyfit(ti[:i+1], sumsd, 1)
                        sumgrad = sp.around(sumfit[0]*10, decimals=2)    
                        csms_md = sp.sum(exportData[i-4:i+1,5].astype(float))/sp.sum(exportData[i-4:i+1,6].astype(float))
                        
                        x = ti
                        y = exportData[:i+1,3].astype(float)
                        if(len(y) <= 1):
                            break
                        level = 1
                        fit = sp.polyfit(x, y, level)
                        gradient = sp.around(fit[0]*10, decimals=2)
                
                        maxr = 100000
                        ry = (exportData[:i+1,4].astype(float))/maxr
                        srlist = [b - a for a,b in zip(ry,ry[1:])]
                        srfit = sp.polyfit(x[:-1], srlist, level)
                        srgrad = sp.around(srfit[0]*10, decimals=2)
        
                        if(sumgrad > 0.2 and i > 3 and srgrad > 0 and csms_md > 0.8 and gradient > 0.7):
                            if(code.decode('utf-8') in tempdic):
                                tempdic[code.decode('utf-8')] = tempdic[code.decode('utf-8')] + 1
                            else:
                                tempdic[code.decode('utf-8')] = tempdic.get(code.decode('utf-8'), 0)
        
                        if(code.decode('utf-8') in tempdic and tempdic[code.decode('utf-8')] == 2 and code not in comps):
                            tempdic[code.decode('utf-8')] = tempdic[code.decode('utf-8')] + 1
                            comps.append((code))
                            mesuStart[code.decode('utf-8')] = i
                            msGradient[code.decode('utf-8')] = gradient
                            msGr[code.decode('utf-8')] = 0
                            msSmdms[code.decode('utf-8')] = 0 
                            msGrade[code.decode('utf-8')] = grade
                            msSrgrad[code.decode('utf-8')] = 0
                            msRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                            rmsRate[code.decode('utf-8')] = float(exportData[i, 3].decode('UTF-8'))
                            pick[code.decode('utf-8')] = False
                            setFile.write( str(code.decode('utf-8')) + ',' + str(float(rate)) +  ',' + str(float(exportData[i, 3].decode('UTF-8'))) + '\n')


