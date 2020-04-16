# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:34:12 2020

@author: Hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger



def make_jaraem_takhir_dar_pardakht(id_ghest):
    id_ghest = str(id_ghest)
    URL = 'https://api.daricbot.ir/jarime_takhir_dar_pardakht'
    data = requests.get(url = URL)
    data = data.json()
    
    
    data = pd.DataFrame(data)
    
    data = data.loc[data[10].astype(int)<=int(id_ghest)]
    
    def remove_undefind_names(data):
        if data=='undefined':
            return ''
        return data
    #data = data.sort_values(by=[3])
    
    sum_jarime=data[8].astype(float).sum()
    data[0] = range(1,data.shape[0]+1)
    data[0] = data[0].astype(str).apply(enToFarsiPandas)
    data[1] = data[1].astype(str).apply(remove_undefind_names).apply(enToFarsiPandas)
    data[2] = data[2].astype(float).apply(add_commas).astype(str).apply(enToFarsiPandas)
    data[3] = data[3].apply(enToFarsiPandas2)
    data[4] = data[4].apply(enToFarsiPandas2)
    data[6] = data[6].apply(enToFarsiPandas2)
    data[7] = data[7].apply(enToFarsiPandas2)
    data[8] = data[8].astype(float).apply(add_commas).apply(truncate_str).apply(enToFarsiPandas2)
    del(data[9])
    data[10]=data[10].apply(enToFarsiPandas)
    
    data.columns = range(100,data.shape[1]+100)
    
    data[0]=data[100]
    data[1]=data[109]
    data[2]=data[101]
    data[3]=data[102]
    data[4]=data[103]
    data[5]=data[104]
    data[6]=data[106]
    data[7]=data[107]
    data[8]=data[108]
    
    sum_jarime=add_commas(sum_jarime)
    sum_jarime = enToFarsiPandas(sum_jarime)
    
    last_row = ['کل','','','','','','','',sum_jarime]
    for i in range(100,data.shape[1]+100-10+1):
        #print(i)
        del(data[i])
    
    
    
    data = pd.concat([data,pd.DataFrame([last_row])])
    
    
    html = open_html()
        
    output = data.values.tolist()
    headers = ['ردیف','شماره قسط','شماره پرداخت به تاخیر افتاده' , 'مبلغ پرداخت','تاریخ برنامه ای پرداخت','تاریخ جدید پرداخت','تاریخ پرداخت شده']
    headers.append('میزان تاخیر')
    headers.append('جریمه')
    
    
    ghest_number = "شماره قسط"+id_ghest
    ghest_number = enToFarsiPandas2(ghest_number)
    header_contents = ['جرائم تاخیر در پرداخت' , ghest_number, JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html = add_header_document(html , header_contents)
    
    html = add_headers(html , headers)
    
    page_names = add_content(html , output)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,options='a3',css_path='resource/style_2.css')
    file_name='jaraem_takhir_dar_pardakht____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan='جرائم تاخیر در پرداخت'
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)
    return True

#make_jaraem_takhir_dar_pardakht(18)

