# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:30:36 2020

@author: hossein
"""

import pandas as pd
import requests 
from writers import *
import pdfkit 


def make_turobocompressor_pdf():
    URL = 'http://api.daricbot.ir/comperosor'
    r = requests.get(url = URL) 
    data = r.json()
    clean_data = []
    for i in data:
        data[i]['dataBase'].append(data[i]['natayej_motalebat'])
    #    print(data[i]['natayej_motalebat'])
        clean_data.append(data[i]['dataBase'])
    
    x = pd.DataFrame(clean_data)
    x = x.sort_values(7)
    
    
    sum_last_row = pd.DataFrame(x)
    sum_last_row = sum_last_row.append(pd.Series() , ignore_index=True)
    len_od_df = len(sum_last_row)-1
    
    
    sum_last_row[3] = sum_last_row[3].astype(float)
    sum_last_row[4] = sum_last_row[4].astype(float)
    sum_last_row.loc[len_od_df,0] = 'کل'
    sum_last_row.loc[len_od_df,3] = truncate(sum_last_row[3].sum(skipna=True))
    sum_last_row.loc[len_od_df,4] = truncate(sum_last_row[4].sum(skipna=True))
    
    del(sum_last_row[5])
    del(sum_last_row[6])
    del(sum_last_row[11])
    del(sum_last_row[10])
    
    output2 = sum_last_row.values.tolist()
    html_data = open_html()
    headers = ['ردیف','نام ایستگاه','نوع توربین','مبلغ مازاد دلار','مبلغ مازاد یورو','تاریخ شروع تحویل','تاریخ پرداخت','توضیحات']
    header_contents = ['گزارش تراز مالی-لوله های 56(نتایج)', 'قسط شماره یکم آذر ماه 1396' , 'گذارش گیری در تاریخ: بهمن 1398']
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    html_data = add_content(html_data , output2)
    
    
    #write_html_file('torbocompress_html_file.html',html_data)
    file_name='torbo_copresor____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    pdfkit.from_file('torbocompress_html_file.html', file_name,configuration=config , options=options)
    return True

#make_turobocompressor_pdf()


