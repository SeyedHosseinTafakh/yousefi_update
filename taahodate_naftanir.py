# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:56:08 2020

@author: hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger

def make_tahodat_naftanir_pdf(file_name,headers)
    
    
    URL = ' http://api.daricbot.ir/taahodat_pardakht_sherkat_naftanir'
    data = requests.get(url = URL)
    data = data.json()
    data = pd.DataFrame(data)
    
    
    data = data.sort_values(1)
    data = data.drop(0,axis=1)
    
    
    data[3] = data[3].astype(float).map(add_commas).map(rv_zeros_af_dot).map(enToFarsiPandas)
    
    data[4] = data[4].map(enToFarsiPandas)
    data[1] = data[1].map(enToFarsiPandas)
    data[6] = data[6].map(enToFarsiPandas)
    data[7] = range(1 , data.shape[0]+1)
    data[7] = data[7].astype(str).map(enToFarsiPandas)
    
    output = pd.DataFrame(data[7].tolist())
    output[1] = data[6]
    output[2] = data[1]
    output[3] = data[2]
    output[4] = data[3]
    output[5] = data[4]
    
    
    output = output.values.tolist()
    html_data = open_html()
    headers = ['ردیف','شماره قسط','تاریخ' , 'شرح','مبلغ دلاری','توضیحات']
    header_contents = ['right' , 'middle', 'left']
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names)
    combine_pdfs(pdf_names,'test_taahodat_naftanir.pdf')
    
#testing    
make_tahodat_naftanir_pdf('test_taahodat_naftanir.pdf' , ['left','middle','right'])
    
    
    
    
    
