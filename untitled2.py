# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:03:02 2020

@author: hossein
"""

import locale
import requests
from writers import *
import pandas as pd
import numpy as np
def enToArNumb(number): 
    dic = { 
        '0':'۰', 
        '1':'١', 
        '2':'٢', 
        '3':'۳', 
        '4':'۴', 
        '5':'۵', 
        '6':'۶', 
        '7':'۷', 
        '8':'۸', 
        '9':'۹', 
    }
    if number in dic:
        return dic.get(number)    
    return number

#ar_numbers = [enToArNumb(num) for num in numbers]

#i = 0
#for index , row in sum_last_row_str.iterrows():
    #ar_numbers = [enToArNumb(num) for num in row(index)]
    #print(type(sum_last_row.iloc[index][row].tolist()))
#    for value_of_row in sum_last_row_str.iloc[index].tolist():
        #farsi_number = []
        #for cell in value_in_row:
        #    farsi_number.append(enToArNumb(cell))
        
        #farsi_number    
    #print(sum_last_row.iloc(index))

#x = sum_last_row_str.iloc[index].tolist()
#y = sum_last_row_str.iloc[1][1]

#for x in num:
#    print(x)

#t ='1'

#y = enToArNumb(t)

#sum_last_row_str = sum_last_row.astype(str)


#def test(row):
#    print(n.tolist())
#    for row_data in row.tolist():
#        for cell in 
#    return j


def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1

def enToFarsiPandas(row):
    re_row =[]
    for data in row:
        a_cell = []
        for cell in data:
            a_cell.append(enToArNumb(cell))
        re_row.append(listToString(a_cell))
    return listToString(re_row)
 

def add_commas(number):
    if type(number) == str:
        return number
    else:
        number = '{:,.2f}'.format(number)
        return number

def rv_zeros_af_dot(number):
    return number.split('.')[0]


URL = 'https://api.daricbot.ir/peymankaran'
r = requests.get(url = URL)
data = r.json()
x = pd.DataFrame(data)
x = x.sort_values(4)
sum_last_row = pd.DataFrame(x)
sum_last_row[3] = sum_last_row[3].astype(float)
sum_last_row[0] = sum_last_row[[0]].applymap(np.int64)
sum_last_row[0] = list(range(1,len(sum_last_row)+1))

sum_last_row = sum_last_row.append(pd.Series() , ignore_index=True)
len_od_df = len(sum_last_row)-1
sum_last_row = sum_last_row.fillna(0)
sum_last_row[0] = sum_last_row[[0]].applymap(np.int64)

sum_last_row.loc[len_od_df,0] = 'کل'
sum_last_row.loc[len_od_df,3] = truncate(sum_last_row[3].sum(skipna=True))









#------------------------------------------------
#y0 = sum_last_row[2].astype(str)
sum_last_row[0] = sum_last_row[0].astype(str).map(enToFarsiPandas)

sum_last_row[3] = sum_last_row[3].map(add_commas).map(rv_zeros_af_dot).map(enToFarsiPandas)
sum_last_row[2] = sum_last_row[2].map(add_commas)
sum_last_row[2] = sum_last_row[2].map(rv_zeros_af_dot).map(enToFarsiPandas)

sum_last_row[4] = sum_last_row[4].astype(str).map(enToFarsiPandas)

sum_last_row[5] = sum_last_row[5].astype(str).map(enToFarsiPandas)



output2 = sum_last_row.values.tolist()
html_data = open_html()
headers = ['ردیف','نام پیمانکار','شماره چک' , 'مبلغ چک','تاریخ چک','توضیحات']
header_contents = ['گزارش تراز مالی-لوله های 56(نتایج)', 'قسط شماره یکم آذر ماه 1396' , 'گذارش گیری در تاریخ: بهمن 1398']
html_data = add_header_document(html_data , header_contents)

html_data = add_headers(html_data , headers)
page_names = add_content(html_data , output2)
add_page_counters(page_names)

def make_pdfs(page_names,naming_pdf):
    pdfs = []
    for page in page_names:
        pdf_name = randomString() + '.pdf'
        pdfkit.from_file('temp/'+page, pdf_name,configuration=config , options=options)
        pdfs.append(pdf_name)
#--------------------------------------------------
        




        
#-------------------------------------
#y1 = sum_last_row[3].map(rv_zeros_af_dot)
#y2 = y1.map(add_commas)

'''
sum_last_row[2] = sum_last_row.applymap(add_commas_0)[2]

print ("Total cost is: ${:,.2f}".format(10000000.100))


add_commas(y2[1])
add_commas(25000000000)
'{:,.2f}'.format(25000000000)


def handle_the_DOT(number):
    number = number.split('.')
    if number[1] >> 0:
        return





TotalAmount = '25000000000'
print ("Total cost is: ${:,.2f}".format(TotalAmount))

locale.setlocale(locale.LC_ALL, '')
locale.currency(123456, symbol=False, grouping=True)

'''

