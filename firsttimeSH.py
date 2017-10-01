import csv
import pandas as pd
import time
import numpy as np

every5mintes = ['a','A','C','A','K','L','O','C','s','1','C','5']
pre5mintes = ['l','P','s','C','k','L','o','W','E','7','D','0']
nex5mintes = ['k','T','9','11','S','M','N','S','P','1','C','5']
total = list()
total.extend(every5mintes)
total.extend(pre5mintes)
total.extend(nex5mintes)
uniqeHis = np.unique(total)
date = time.strftime('%Y/%m/%d')
HisDataF = pd.DataFrame({'Data' : uniqeHis,
                        'Date': date})
#print(HisDataF)
HisDataF.to_csv('HisDataF.csv',header=True,index=False)

firstDay = ['A','C','K','L']
secondDay = ['C','S','L','P']
thirdDay = ['0','C','9','L']
fourthDay = ['C','K','U','L']

firstDayS = set(firstDay)
secondDayS = set(secondDay)
thirdDayS = set(thirdDay)
fourthDayS = set(fourthDay)

totalS = list(firstDayS&secondDayS&thirdDayS&fourthDayS)

StaffDataF = pd.DataFrame({'Data' : totalS,
                        'Date': date})
StaffDataF.to_csv('StaffDataF.csv',header=True,index=False)
