# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 01:45:36 2020

@author: hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger




def make_sadid_mahshar(id_ghest):
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))

    #URL = 'http://api.daricbot.ir/pardakht_shode_tavasote_naftanir_TM'
    #data = requests.get(url = URL)
    #data = data.json()
    
    
    labels = ['شرح :','مبلغ اصل :','تاریخ شروع اقساط:']
    spans = ['75 درصد پیش پرداخت ماهشهر','794,046,139,500','1396-09-17'] 
    
    spans[0] = enToFarsiPandas2(spans[0])
    spans[1] = enToFarsiPandas2(spans[1])
    spans[2] = enToFarsiPandas2(spans[2])
    header_contents = ['پیش پرداخت لوله های سدید ماهشهر' , shomare_ghest, JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html , labels)
    html = add_spans(html , spans)
    output=[]
    html= add_header_document(html , header_contents)
    page_names = add_content(html , output)
    pdf_names = add_page_counters(page_names)
    first_pdf_name = make_pdfs([page_names[0]],css_path='resource/style_height.css',options='a4')
    file_name='pish_pardakht_sadid_mahshahr____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    #onvan='پیش پرداخت سدید ماهشهر'
    onvan = 'ترازمالی – لوله های سدید ماهشهر'
    return combine_pdfs(first_pdf_name,file_name,onvan = onvan,tarikh=tarikh,ghest_number=id_ghest)


#make_sadid_mahshar()







