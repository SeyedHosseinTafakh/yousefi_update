# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:09:24 2020

@author: hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


def make_tahodat_mohandesi_pdf(id_ghest='None'):
    if id_ghest =='None':
    #TODO:: have to add shomare_ghest number in this function
        URL = 'http://api.daricbot.ir/taahodat_pardakht_sherkat_mohandesi_tose_gas'
    else:
        URL = 'http://api.daricbot.ir/taahodat_pardakht_sherkat_mohandesi_tose_gas?id_ghest='+id_ghest
    data = requests.get(url = URL)
    data = data.json()
    data = pd.DataFrame(data)
    
    
    data = data.sort_values(1)
    data = data.drop(0,axis=1)
    
    
    data[3] = data[3].astype(float).map(add_commas).map(rv_zeros_af_dot).map(enToFarsiPandas2)
    
    data[4] = data[4].map(enToFarsiPandas2)
    data[1] = data[1].map(enToFarsiPandas2)
    data[6] = data[6].astype(str).map(enToFarsiPandas2)
    data[7] = range(1 , data.shape[0]+1)
    data[7] = data[7].astype(str).map(enToFarsiPandas2)
    
    output = pd.DataFrame(data[7].tolist())
    output[1] = data[6]
    output[2] = data[1]
    output[3] = data[2]
    output[4] = data[3]
    output[5] = data[4]
    
    
    output = output.values.tolist()
    html_data = open_html()
    headers = ['ردیف','شماره قسط','تاریخ' , 'شرح','مبلغ دلاری','توضیحات']
    header_contents = ['تعهدات پرداخت شرکت مهندسی و توسعه گاز ایران' , ' ', JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,options ='a4',css_path='temp/style_a4_2.css')
    file_name='taahodat_mohandesi____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan='تعهدات پرداخت شرکت مهندسی و توسعه گاز ایران'
    return combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)
    

#testing    
#make_tahodat_mohandesi_pdf(str('5'))
    
    
    