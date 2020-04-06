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

def make_jadval_sadid_mahshahr():
    URL = 'http://api.daricbot.ir/jadval_loole_sazi_sadid?time_now=1396-9-17'
    
    r = requests.get(url = URL)
    data = r.json()
    
    x = pd.DataFrame(data).T
    
    
    f = pd.DataFrame(columns=['idies'],data=list(range(1,len(data)+1)))
    
    
    
    
    x.index = range(0,x.shape[0])
    x.columns = range(0,x.shape[1])
    
    
    d = [f,x]
    x = pd.concat(d,axis=1,ignore_index=True,sort=False)
    
    
    
    
    
    x[0][x.shape[0]-1] = 'کل'
    
    
    
    
    x[0]=x[0].astype(str).apply(enToFarsiPandas2)
    x[1]=x[1].astype(str).apply(enToFarsiPandas2)
    x[2]=x[2].astype(str).apply(enToFarsiPandas2)
    x[3]=x[3].astype(float).abs().astype(str).apply(enToFarsiPandas)
    x[4]=x[4].astype(float).abs().astype(str).apply(enToFarsiPandas)
    
    x[5]=x[5].astype(str).apply(enToFarsiPandas2)
    
    
    output2 = x.values.tolist()
    html_data = open_html()
    headers=['ردیف','تاریخ','تعهد به پرداخت','پرداخت نشده دوره قبل','جریمه','کل مطالبات']
    header_contents = ['گذارش جدول لوله های سدید ماهشهر',' ',JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output2,first_page_row_numbers=35,second_page_numbers=35)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,'a4','temp/style_a4_2.css')
    file_name ='sadid_mahshahr_jadval___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    combine_pdfs(pdf_names,file_name)
    return True





