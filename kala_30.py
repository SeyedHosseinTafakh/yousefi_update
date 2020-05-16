# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 06:27:22 2020

@author: Hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger



    
def make_kala_30(id_ghest):
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))

    URL = 'http://api.daricbot.ir/kala_30'
    data = requests.get(url = URL)
    data = data.json()
    
    
    labels=[]
    labels.append('استعلام 1:')
    labels.append('استعلام 2:')
    labels.append('استعلام 3:')
    labels.append('میانگین سه استعلام :')
    labels.append('مالیات ارزش افزوده و سایر خدمات :')
    
    spans=[]
    spans.append(data['database_record1'][0])
    spans.append(data['database_record1'][1])
    spans.append(data['database_record1'][2])
    spans.append(data['miyangin__1'])
    spans.append(data['maliayt__1'])
    
    spans[0]=enToFarsiPandas(rv_zeros_af_dot((add_commas(spans[0]))))
    spans[1]=enToFarsiPandas(rv_zeros_af_dot((add_commas(spans[1]))))
    spans[2]=enToFarsiPandas(rv_zeros_af_dot((add_commas(spans[2]))))
    spans[3]=enToFarsiPandas((add_commas(spans[3])))
    spans[4]=enToFarsiPandas((add_commas(spans[4])))
    
    
    header_contents = ['کالاهای 30 اینچ' , shomare_ghest, JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html , labels)
    html = add_spans(html , spans)
    output=[]
    html= add_header_document(html , header_contents)
    page_names = add_content(html , output)
    pdf_names = add_page_counters(page_names)
    first_pdf_name = make_pdfs([page_names[0]],css_path='temp/style_a4_3_Copy.css',options='a4')
    file_name='kala_30_inch____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    #onvan='پیش پرداخت سدید ماهشهر'
    onvan = 'ترازمالی – لوله های سدید ماهشهر'
    return combine_pdfs(first_pdf_name,file_name,onvan = onvan,tarikh=tarikh,ghest_number=id_ghest)
    
#make_kala_30()







