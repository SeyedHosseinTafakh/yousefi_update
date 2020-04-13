# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:28:49 2020

@author: Hossein
"""
import pandas as pd


csv = pd.read_csv('data.csv')


#file_name ='taraz_mali_30___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
onvan='گزارش تراز مالی لوله های 30 اینچ'
combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number='',onvan=onvan,tarikh=tarikh)

