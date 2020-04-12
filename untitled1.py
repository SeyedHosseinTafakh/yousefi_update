# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:28:49 2020

@author: Hossein
"""
import pandas as pd

csv = pd.DataFrame([['1','2','3','4']])

csv.to_csv('data.csv',index=False)


csv = pd.read_csv('data.csv')

tarikh ='tarikh'
ghest_number='16'
onvan='shandool'
result_name='.pdf'

csv_data=[]
csv_data.append(tarikh)
csv_data.append(ghest_number)
csv_data.append(onvan)
csv_data.append(result_name)
csv = pd.DataFrame(csv_data).T
csv.columns=range(0,4)

csv_old = pd.read_csv('data.csv')
csv_old.columns=range(0,4)
csv_concat = pd.concat([csv_old,csv],axis=0)

JalaliDatetime.now().strftime('%Y,%M')



