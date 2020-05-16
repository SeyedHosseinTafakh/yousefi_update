# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:28:23 2020

@author: Hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger



def make_torbocompresssor_pdf(id_ghest):
    URL = 'http://api.daricbot.ir/comperosor'
    data = requests.get(url = URL)
    data = data.json()
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))

    x=[]
    for d in data:
        x.append(data[d]['dataBase'])
    
    df = pd.DataFrame(x)
    
    
    last_row_sum = ['کل','','',df[3].astype(float).sum(),df[4].astype(float).sum(),'','','','','','']
    
    
    last_row_sum = np.array(last_row_sum).reshape(1,11)
    last_row_sum = pd.DataFrame(last_row_sum)
    
    df = df.append(last_row_sum)
    
    del(df[5])
    del(df[6])
    del(df[10])
    
    
    df[0] = df[0].astype(str).apply(enToFarsiPandas2)
    df[3] = df[3].astype(str).apply(enToFarsiPandas2)
    df[4] = df[4].astype(str).apply(enToFarsiPandas2)
    
    df[7] = df[7].astype(str).apply(enToFarsiPandas2)
    df[8] = df[8].astype(str).apply(enToFarsiPandas2)
    
    header = ['ردیف','نام ایستگاه','نوع توربین','مبلغ مآزاد - دلار','مبلغ مآزاد - یورو','تاریخ شروع تحویل','تاریخ پرداخت','توضیحات']
    header_content = ['توربو کمپرسور ها',shomare_ghest,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    
    
    html = open_html()
    html = add_header_document(html , header_content)
    
    html = add_headers(html , header)
    
    page_names = add_content(html , df.values.tolist())
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,options='a4',css_path='temp/style_a4_2.css')
    file_name='torbo_copresor____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    
#    combine_pdfs(pdf_names,file_name)
    
    
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan='تراز مالی - نتایج - توربو کمپرسورها'
    return combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)




#make_torbocompresssor_pdf()


