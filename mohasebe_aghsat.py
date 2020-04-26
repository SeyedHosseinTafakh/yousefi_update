# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 08:52:44 2020

@author: Hossein
"""

import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger




def make_mohosabe_aghsta_pdf(id_ghest):
    id_ghest = int(id_ghest)
    def mohasebe_aghsat(id_ghest):    
        month_ghest = handle_month(id_ghest)
        
        month_ghest = month_ghest.split('-')
        
        if int(month_ghest[1]) <10:
            month_ghest[1] = '0'+month_ghest[1]
        month_ghest = month_ghest[0]+'-'+month_ghest[1]
        
        month_ghest
            
        URL = 'https://api.daricbot.ir/ghest_bandi_kole_gostare_ha_tajamoee?time='+month_ghest
        data = requests.get(url = URL)
        data = data.json()
        
        x = pd.DataFrame(data[0],index=range(0,1))
        
        x = x.loc[0].sum()
        
        labels=[]
        labels.append('سهم گستره ها')
        spans = []
        spans.append(x)
        
        URL = 'https://api.daricbot.ir/mohasebe_aghsat_tajamoee?id_ghest='+str(id_ghest)
        data = requests.get(url = URL)
        data = data.json()
        
        labels.append('تعهدات پرداخت شرکت مهندسی و توسعه گاز ایران')
        labels.append('جرائم تاخیر در پرداخت اقساط')
        labels.append('کل مبلغ پرداختی')
        spans.append(data['taahodat_pardakht_sherkat_mohandesi_tose_gas'])
        spans.append(data['jarime_taakhir_dar_pardakht'])
        spans.append(sum(spans))
        
        
        
        
        
        URL = 'https://api.daricbot.ir/mohasebe_aghsat_tajamoee?id_ghest='+str(int(id_ghest)-1)
        data = requests.get(url = URL)
        data = data.json()
        
        labels.append('تعهدات پرداخت شرکت نفتانیر')
        spans.append(data['taahodat_pardakht_sherkat_naftanir'])
        
        #-----------------------------------------
        URL = 'https://api.daricbot.ir/jaraem_taakhir_dar_bahre_bardariV3?id_ghest='+str(id_ghest)
        data = requests.get(url = URL)
        data = data.json()
        
        f = 0
        for i in data:
            f += data[i]
        labels.append('جرائم تاخیر در بهره برداری')
        spans.append(f)
        #-----------------------------------------
        
        labels.append('کل مبلغ کسورات')
        spans.append(spans[4]+spans[5])
        
        
        labels.append('مبلغ قابل پرداخت تجمعی')
        spans.append(spans[3]-spans[6])
        
        return (labels , spans)
    
    x = mohasebe_aghsat(id_ghest-1)
    mablagh_dore_ghable = x[1][7]
    x = mohasebe_aghsat(id_ghest)
    labels = x[0]
    spans = x[1]
    labels.append('مبلغ پرداختی در دوره های قبل')
    spans.append(mablagh_dore_ghable)
    
    labels.append('مانده قابل پرداخت')
    spans.append(abs(mablagh_dore_ghable - x[1][7]))
    
    
    for i in range(len(spans)):
        spans[i] = enToFarsiPandas2(add_commas(spans[i]))
    
    
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))
    
    header_contents = ['محاسبه اقساط', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    #header_contents = ['right' , 'middle', 'left']
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html , labels)
    html = add_spans(html , spans)
    output=[]
    html= add_header_document(html , header_contents)
    page_names = add_content(html , output)
    pdf_names = add_page_counters(page_names)
    first_pdf_name = make_pdfs([page_names[0]],css_path='temp/style_a4_3_Copy - Copy.css',options='a4')
    file_name='mohasebe_aghsta____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    #onvan='پیش پرداخت سدید ماهشهر'
    onvan = 'محاسبه اقساط'
    combine_pdfs(first_pdf_name,file_name,onvan = onvan,tarikh=tarikh,ghest_number=id_ghest)
    
#make_mohosabe_aghsta_pdf(1)



