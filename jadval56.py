# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:06:19 2020

@author: Hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


def make_jadval_56(id_ghest):
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))

    URL = 'http://api.daricbot.ir/jadval56'
    
    r = requests.get(url = URL)
    data = r.json()
    
    
    data['befor']['sharh'] = 'پرداخت شده توسط شرکت نفتانیر'
    data['0']['sharh'] = 'پرداخت شده توسط شرکت نفتانیر'
    len(data)
    
    f = pd.DataFrame(columns=['idies'],data=list(range(1,len(data)+1)))
    x=pd.DataFrame(data).T
    
    x = x.reset_index()
    d = [f,x]
    x = pd.concat(d,axis=1,ignore_index=True,sort=False)
    del(x[1])
#    x['idies'] = range(1,x.shape[0]+1)
    #x.columns = range(0,x.shape[1])
    #x.index = range(1,x.shape[0]+1)
    x[0]=x[0].astype(str).apply(enToFarsiPandas2)
    x[3]=x[3].apply(enToFarsiPandas2)
    x[4]=x[4].astype(float).abs().astype(str).apply(enToFarsiPandas)
    x[5]=x[5].astype(float).abs().astype(str).apply(enToFarsiPandas)
    x[6]=x[6].astype(float).abs().astype(str).apply(enToFarsiPandas)
    x[7]=x[7].fillna(0).astype(float).abs().astype(str).apply(enToFarsiPandas)
    output2 = x.values.tolist()
    html_data = open_html()
    headers=['ردیف','شرح','تاریخ','مبلغ','پرداخت نشده دوره قبل','جریمه','کل مطالبات']
    header_contents = ['گزارش جدول لوله های 56 اینچ',shomare_ghest,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output2,first_page_row_numbers=35,second_page_numbers=35)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,'a4','temp/style_a4_2.css')
    file_name ='jadval56___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan='ترازمالی –نتایج کلی –لوله های 56اینچ'
    return combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)

#    combine_pdfs(pdf_names,file_name)


#make_jadval_56(10)



