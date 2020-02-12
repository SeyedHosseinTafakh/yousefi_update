# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:18:05 2020

@author: hossein
"""


import pandas as pd
import requests 
from writers import *
import pdfkit 
import numpy as np
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
options = {
    'page-size': 'A3',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'landscape',
}


def make_peymankaran_pdf(file_name):    
    URL = 'https://api.daricbot.ir/peymankaran'
    r = requests.get(url = URL) 
    data = r.json()
    x = pd.DataFrame(data)
    x = x.sort_values(4)
    
    
    sum_last_row = pd.DataFrame(x)
    sum_last_row = sum_last_row.append(pd.Series() , ignore_index=True)
    len_od_df = len(sum_last_row)-1
    sum_last_row[3] = sum_last_row[3].astype(float)
    
    sum_last_row.loc[len_od_df,0] = 'کل'
    sum_last_row.loc[len_od_df,2] = truncate(sum_last_row[2].sum(skipna=True))
    sum_last_row.loc[len_od_df,3] = truncate(sum_last_row[3].sum(skipna=True))
    
    
    
    output2 = sum_last_row.values.tolist()
    html_data = open_html()
    headers = ['ردیف','نام پیمانکار','شماره چک' , 'مبلغ چک','تاریخ چک','توضیحات']
    header_contents = ['گزارش تراز مالی-لوله های 56(نتایج)', 'قسط شماره یکم آذر ماه 1396' , 'گذارش گیری در تاریخ: بهمن 1398']
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    html_data = add_content(html_data , output2)
    
    
    write_html_file('peymankaran_html_file.html',html_data)
    
    pdfkit.from_file('peymankaran_html_file.html', file_name,configuration=config , options=options)
    return True

make_56_pdf('testing.pdf')

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



output2 = sum_last_row.values.tolist()
html_data = open_html()
headers = ['ردیف','نام پیمانکار','شماره چک' , 'مبلغ چک','تاریخ چک','توضیحات']
header_contents = ['گزارش تراز مالی-لوله های 56(نتایج)', 'قسط شماره یکم آذر ماه 1396' , 'گذارش گیری در تاریخ: بهمن 1398']
html_data = add_header_document(html_data , header_contents)

html_data = add_headers(html_data , headers)
page_names = add_content(html_data , output2)
add_page_counters(page_names)

#write_html_file('peymankaran_html_file.html',html_data)

pdfkit.from_file('temp/vwlr.html', 'test_peymankaran2.pdf',configuration=config , options=options)

