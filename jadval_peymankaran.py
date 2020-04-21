# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 04:54:54 2020

@author: Hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger

def make_jadval_peymankaran(id_ghest):
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))

    URL = 'http://api.daricbot.ir/jadval_peymankaran'
    data = requests.get(url = URL)
    data = data.json()
    dore_ghabl_data = data['dore_ghable']
    del(data['dore_ghable'])
    
    x = pd.DataFrame(data).T
    
    dore_ghabl = {
        "sharh":"پرداخت شده توسط نفتانیر",
        "tozihat":"مبالغ ریالی پرداخت شده توسط نفتانیر تا تاریخ 94/12/27",
        "tarikh":dore_ghabl_data['tarikh'],
        "pool":dore_ghabl_data['pool'],
        "pardakht_nashode_dore_ghable":0,
        "jarime":0,
        "kole_motalebat":dore_ghabl_data['kole_motalebat']    
        }
    
    dore_ghabl=[dore_ghabl]
    dore_ghabl = pd.DataFrame(dore_ghabl)
    del(dore_ghabl_data)
    x = pd.concat([dore_ghabl,x])
    del(dore_ghabl)
    def delete_tg_coming(data):
        if data=='telegram coming':
            return ""
        return data
    
    x.columns = range(x.shape[1])
    
    last_row = ['کل','','','','',enToFarsiPandas(add_commas(x[5].sum())),'','']
    
    last_row = pd.DataFrame(last_row).T
    x[1] = x[1].apply(delete_tg_coming)
    x[2] = x[2].astype(str).apply(enToFarsiPandas2)
    x[3] = x[3].apply(abs).apply(add_commas).apply(enToFarsiPandas)
    x[4] = x[4].apply(add_commas).apply(enToFarsiPandas)
    x[5] = x[5].apply(add_commas).apply(enToFarsiPandas)
    x[6] = x[6].apply(add_commas).apply(enToFarsiPandas)
    
    idies = pd.Series(range(1,x.shape[0]+1)).T
    #x = pd.concat([idies,x],axis=1)
    #x = pd.concat([x,last_row])
    x.index = range(x.shape[0])
    
    #idies=pd.DataFrame(idies)
    y = pd.concat([idies,x],axis=1)
    y.columns = range(y.shape[1])
    y=pd.concat([y,last_row])
    
    output =y.values.tolist()
    html_data = open_html()
    headers=['ردیف','شرح','توضیحات','تاریخ','مبلغ','جریمه پرداخت نشده دوره قبل','جریمه','کل مطالبات']
    header_contents = ['نتایج کلی پیمانکاران',shomare_ghest,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output,first_page_row_numbers=34,second_page_numbers=35)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,'a3','resource/style.css')
    file_name ='jadval_peymankaran___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    onvan = '  ترازمالی –نتایج کلی –پیمانکاران'
    tarikh = tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    combine_pdfs(pdf_names,file_name,ghest_number=id_ghest,tarikh=tarikh , onvan=onvan)
    return True








