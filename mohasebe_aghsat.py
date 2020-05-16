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
    month_ghest = handle_month(id_ghest)
        
    month_ghest = month_ghest.split('-')
    
    if int(month_ghest[1]) <10:
        month_ghest[1] = '0'+month_ghest[1]
    month_ghest = month_ghest[0]+'-'+month_ghest[1]
    def mohasebe_aghsat(id_ghest):
        
        
            
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
    #------------------------------------------------------------------------------
    URL = 'https://api.daricbot.ir/ghest_bandi_kole_gostare_ha_tajamoee?time='+str(month_ghest)
    data = requests.get(url = URL)
    data = data.json()
    
    out_put = pd.DataFrame(data[0],index=(0,10)).T
    gostare = out_put.index
    out_put.index = range(0,10)
    out_put[0]=gostare
    out_put[2]=out_put[10]
    out_put[1]=data[1].values()
    del(out_put[10])
    
    out_put[1] = out_put[1].astype(float).apply(add_commas).astype(str).apply(enToFarsiPandas).apply(add_percentage_sign)
    out_put[2] = out_put[2].astype(float).apply(add_commas).astype(str).apply(enToFarsiPandas)
    
    headers=[]
    headers.append('بخش / ایستگاه')
    headers.append('درصد کار صورت گرفته')
    headers.append('مبلغ تجمعی اقساط')
    
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html , labels)
    html = add_spans(html , spans)
    output=out_put.values.tolist()
    
    html= add_header_document(html , header_contents)
    html = add_headers(html , headers)
    
    page_names = add_content(html , output)
    pdf_names = add_page_counters(page_names)
    first_pdf_name = make_pdfs([page_names[0]],css_path='temp/style_a4_3_Copy - Copy.css',options='a4')
    file_name='mohasebe_aghsta____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    #onvan='پیش پرداخت سدید ماهشهر'
    onvan = 'محاسبه اقساط'
    #combine_pdfs(first_pdf_name,file_name,onvan = onvan,tarikh=tarikh,ghest_number=id_ghest)

    month_ghest = handle_month(id_ghest)
        
    month_ghest = month_ghest.split('-')
    
    if int(month_ghest[1]) <10:
        month_ghest[1] = '0'+month_ghest[1]
    month_ghest = month_ghest[0]+'-'+month_ghest[1]
    #def get_gostare_riz(id_ghest):
    pdf_names=[]
    
    
    
    gostareha=['گستره اهواز خرمشهر و شملچه و ایستگاه کنترل فشار خرمشهر و ایستگاه اندازه گیری شلمچه','گستره کوهدشت چارمله و ایستگاه کنترل فشار کوهدشت و مخابرات','گستره کوهدشت بیستون و ایستگاه کنترل فشار دهگلان','گستره دزفول کوهدشت و ایستگاه کنترل فشار دزفول','گستره بیستون کرمانشاه (34 کیلومتر) و ایستگاه کنترل فشار بیستون','تاسیسات تقویت فشار اهواز','تاسیسات تقویت فشار حسینیه','تاسیسات تقویت فشار کوهدشت','تاسیسات تقویت فشار دیلم','تاسیسات تقویت فشار بیدبلند'           ]
    sahm_az_kol = ['15.95','14.10','15.10','16.83','1.75','7.69','7.69','6.96','6.96','6.96']
    URL = 'https://api.daricbot.ir/ghest_bandi_kole_gostare_ha_tajamoee?time='+str(month_ghest)
    limit = requests.get(url = URL)
    limit = limit.json()
    
    for i in limit[1]:
        if list(limit[0].values())[int(i)-1] > 0:
            gostare_id=i
            URL = 'https://api.daricbot.ir/ghest_bandi_har_pishraft?gostare_id='+str(gostare_id)
            data = requests.get(url = URL)
            data = data.json()
            data = pd.DataFrame(data)
            headers  = list(data.columns)
            headers.insert(0,'تاریخ')
            labels = ['نام گستره :','وزن گستره/تاسیسات از کل پروژه :']
            data.columns = range(1,data.shape[1]+1)
            indexes = data.index
            data.index=range(0,data.shape[0])
            data = pd.concat([pd.DataFrame(indexes),data],axis=1,ignore_index=True)
            
            for n in range(data.shape[1]):
                data[n] = data[n].apply(add_commas).astype(str).apply(truncate_str).apply(enToFarsiPandas2)
            
            spans=[]
            spans.append(gostareha[int(i)-1])
            spans.append(enToFarsiPandas(sahm_az_kol[int(i)-1]))
            shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))
            
            header_contents = ['محاسبه اقساط', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
            
            
            for j in range(0,data.shape[1],5):
                html = open_html()
                html = add_div_and_seprator_for_info(html)
                html = add_labels(html , labels)
                html = add_spans(html , spans)
            
                output=data.iloc[:,j:j+5].values.tolist()
                
                html= add_header_document(html , header_contents)
                headers_ = headers[j:j+5]
                html = add_headers(html , headers_)
                
                page_names = add_content(html , output,first_page_row_numbers=30)
                pages = add_page_counters(page_names)
                pdf_names.append(make_pdfs(pages,css_path='temp/style_a4_4.css',options='a4'))
        
    final_pdfs = []
    final_pdfs.append(first_pdf_name[0])
    for pdfs in pdf_names:
        for pdf in pdfs:
            final_pdfs.append(pdf)
    #return final_pdfs
    return combine_pdfs(final_pdfs,file_name,onvan = onvan,tarikh=tarikh,ghest_number=id_ghest)

















