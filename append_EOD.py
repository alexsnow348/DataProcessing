import csv
import pandas as pd
import datetime as datetime
import time


date = '2017/10/02'
dataHD = pd.read_csv('HisDataF.csv')
dataSD = pd.read_csv('StaffDataF.csv')

uniqeToday = ['Z','V','X','M']
staffToday = ['A','K','C']

HisDataF = list(dataHD.Data)
staffHis = list(dataSD.Data)

toAppendH = list()
for each in uniqeToday:
    if each not in HisDataF:
        toAppendH.append(each)

toAppendS = list()
for each in staffToday:
    if each not in staffHis:
        toAppendS.append(each)

todayDataH = pd.DataFrame({'Data' : toAppendH,
                        'Date': date})
todayDataS = pd.DataFrame({'Data' : toAppendS,
                        'Date': date})

toWriteHD =  pd.concat([dataHD,todayDataH])
toWriteHD.to_csv('HisDataF.csv',header=True,index=False)
toWriteSD =  pd.concat([dataSD,todayDataS])
toWriteSD.to_csv('StaffDataF.csv',header=True,index=False)
