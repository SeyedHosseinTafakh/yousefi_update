# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 08:09:14 2020

@author: hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger



    
def make_pardakht_shode_tavasote_naftanir(id_ghest):
    id_ghest=5
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))
    URL = 'http://api.daricbot.ir/pardakht_shode_tavasote_naftanir_TM'
    data = requests.get(url = URL)
    data = data.json()
    
    data = pd.DataFrame(data)
    del(data[6])
    del(data[7])
    
    labels = ['جمع کل بابت همه :','جمع کل بابت پیمانکاران :','جمع کل بابت لوله های 56 اینچ','جمع کل بابت تحصیل اراضی :']
    peymankaran = data.loc[data[3] =='پیمانکاران']
    pipe_56 = data.loc[data[3] =='لوله های 56 اینچ']
    arazi = data.loc[data[3]=='تحصیل اراضی']
    
    spans = []
    spans.append(enToFarsiPandas(str(peymankaran[2].astype(np.int64).sum())))
    spans.append(enToFarsiPandas(str(pipe_56[2].astype(np.int64).sum())))
    spans.append(enToFarsiPandas(str(arazi[2].astype(np.int64).sum())))
    spans.append(enToFarsiPandas(str(data[2].astype(np.int64).sum())))
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html , labels)
    html = add_spans(html , spans)
    
    
    headers = ['ردیف','تاریخ پرداخت','مبلغ دریافتی','شماره سند دریافت','پرداختی بابت','توضیحات']
    header_contents = ['پرداخت شده توسط نفتانیر' , ' ', JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    data[0] = pd.Series(list(range(1,len(data)+1)))
    data[0] = data[0].astype(str).map(enToFarsiPandas)
    data[1] = data[1].astype(str).map(enToFarsiPandas2)
    data[2] = data[2].astype('int64').map(add_commas).astype(str).map(rv_zeros_af_dot).map(enToFarsiPandas2)
    data[4] = data[4].map(enToFarsiPandas)
    
    
    baghi_jadval = pd.DataFrame(data)
    data = data.iloc[:20]
    output = data.values.tolist()
    
    onvan='تراز مالی - نتایج - پرداخت شده توسط نفتانیر'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    file_name='pardakht_shote_tavasot_naftanir____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    
    html_data = add_header_document(html , header_contents)
    html_data = add_headers(html_data , headers)
    
    page_names = add_content(html_data , output,first_page_row_numbers=16)
    
    pdf_names = add_page_counters(page_names)
    first_pdf_name = make_pdfs([page_names[0]],options='a5',css_path='resource/style_pardakh_shode_tavasote_naftanir_height.css')
    
    
    
    
    if baghi_jadval.shape[0]-16>0:    
        output = pd.DataFrame(baghi_jadval.iloc[17:]).values.tolist()
        html = open_html()
        html_data = add_header_document(html , header_contents)
        html_data = add_headers(html_data , headers)
        
        
        
        page_names = add_content(html_data , output)
        pdf_names = add_page_counters(page_names,pusher=1)
        #first_pdf_name = make_pdfs([page_names[0]],'resource/style_height.css')
        
        pdf_names = make_pdfs(page_names,options='a5',css_path='resource/style_pardakh_shode_tavasote_naftanir.css')
        pdf_names = first_pdf_name + pdf_names
        combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)
    
    else:
        del(pdf_names[0])
        combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)
    


#make_pardakht_shode_tavasote_naftanir(5)











