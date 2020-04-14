
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:32:38 2020

@author: Hossein
"""

import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger

    
def make_jadval_36_dollar():
    URL = 'http://api.daricbot.ir/jadval36_dollar'
    
    r = requests.get(url = URL)
    data = r.json()
    
    x = pd.DataFrame(data)
    
    def replace_sharh(data):
        if data=='sharh':
            return 'تعهدات پرداخت 30'
        return data
    
    
    f = pd.DataFrame(columns=['idies'],data=list(range(1,len(data)+1)))
    x=pd.DataFrame(data)
    d = [f,x]
    x = pd.concat(d,axis=1,ignore_index=True,sort=False)
    
    
    
    x.index = range(1,x.shape[0]+1)
    x.columns = range(0,x.shape[1])
    
    
    sum_last_row = []
    sum_last_row.append('کل')
    sum_last_row.append(' ')
    sum_last_row.append(' ')
    sum_last_row.append(enToFarsiPandas2(x[3].astype(float).sum().astype(str)))
    sum_last_row.append(' ')
    sum_last_row.append(' ')
    sum_last_row.append(enToFarsiPandas2(x[4].astype(float).sum().astype(str)))
    sum_last_row = pd.DataFrame([sum_last_row])
    
    
    x[1] = x[1].apply(replace_sharh)
    x[0]=x[0].astype(str).apply(enToFarsiPandas2)
    
    x[2]=x[2].astype(str).apply(enToFarsiPandas2)
    x[3]=x[3].astype(float).abs().astype(str).apply(enToFarsiPandas)
    x[4]=x[4].astype(float).abs().astype(str).apply(enToFarsiPandas)
    
    x[5]=x[5].astype(float).abs().astype(str).apply(enToFarsiPandas)
    
    x[6]=x[6].astype(float).abs().astype(str).apply(enToFarsiPandas)
    
    x = pd.concat([x,sum_last_row])
    
    
    
    output2 = x.values.tolist()
    html_data = open_html()
    headers=['ردیف','شرح','تاریخ','مبلغ','پرداخت نشده دوره قبل','کل مطالبات','جریمه']
    header_contents = ['گذارش جدول لوله های 30 اینچ',' ',JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output2,first_page_row_numbers=35,second_page_numbers=35)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,'a4','temp/style_a4_2.css')
    file_name ='jadval30___dollar_'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan='ترازمالی –نتایج کلی –لوله های 36اینچ'
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number='',onvan=onvan,tarikh=tarikh)
    
    return True



#make_jadval_36_dollar()

