# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:46:53 2020

@author: hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


def make_tahodat_mohandesi_pdf(file_name , headers):

    URL = 'http://api.daricbot.ir/jadvalArazi'
    data = requests.get(url = URL)
    data = data.json()
    
    for key in list(data.keys()):
        data[key]= list(data[key].values())
    data = list(data.values())
    
    data = pd.DataFrame(data)
    data[1]=data[1].map(enToFarsiPandas2)
    data[2]=data[2].map(add_commas).map(enToFarsiPandas).map(rv_zeros_af_dot)
    data[3]=data[3].map(add_commas).map(enToFarsiPandas).map(rv_zeros_af_dot)
    data[4]=data[4].map(add_commas).map(enToFarsiPandas).map(rv_zeros_af_dot)
    data[5]=data[5].map(add_commas).map(enToFarsiPandas).map(rv_zeros_af_dot)
    data1 = pd.DataFrame({'0':list(range(1,len(data)+1))})
    data = data1.join(data)
    data['0']=data['0'].astype(str).map(enToFarsiPandas2)
    
    output = data.values.tolist()
    headers = ['ردیف','شرح','تاریخ','تعهد به پرداخت','پرداخت شده دوره قبل','جمع کل باقی مانده '+'ماه قبل و جریمه مربوطه','جمع کل مطالبات']
    header_contents = ['گذارش تحصیل اراضی', ' ' , JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = open_html()
    
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    html_data = add_content(html_data , output)
    page_names = add_page_counters(html_data)
    
    pdf_names = make_pdfs(page_names,css_path='resource/style.css',options='a3')
    
    file_name='torbo_copresor____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    
    combine_pdfs(pdf_names,file_name)
    return True









