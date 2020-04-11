# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:35:46 2020

@author: Hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger



#def make_jaraem_takhir_dar_bahre_bardari(id_gostare,id_ghest):
gostare_id = '6'

id_ghest = '16'


x=[]

for i in range(1,11):
    gostare_id = str(i)
    URL = 'http://api.daricbot.ir/jaraem_taakhir_dar_bahre_bardariV2?gostare_id='+gostare_id+'&'+'id_ghest'+'='+id_ghest+'&date='+handle_month(id_ghest)
    data = requests.get(url = URL)
    data = data.json()
    if len(data['jarime'])>0:
        for j in range(0,len(data['jarime'])):
            data['jarime'][j].append(data['jadval_koli']['esme_gostare'])
#        data['jarime'].append(data['jadval_koli']['esme_gostare'])
        x.append(data['jarime'])
#        data_jadval = pd.concat([data,data_jadval],axis=0)
#del(gostare_id)
#del(URL)
y = pd.DataFrame(columns=list(range(0,8)))
for i in x:
    y = pd.concat([y,pd.DataFrame(i)])


data_jadval = y


y = pd.DataFrame(columns=list(range(0,6)))
y[0]=range(1,data_jadval.shape[0]+1)
y[1] = data_jadval[0].values.tolist()
y[2] = data_jadval[4].values.tolist()
y[3] = data_jadval[2].values.tolist()
y[4] = data_jadval[3].values.tolist()
y[5] = data_jadval[1].values.tolist()
y[6] = data_jadval[7].values.tolist()


y[0] = y[0].astype(str).apply(enToFarsiPandas2)
y[2] = y[2].astype(str).apply(enToFarsiPandas2)
y[3] = y[3].astype(str).apply(enToFarsiPandas2)
y[4] = y[4].astype(str).apply(enToFarsiPandas2).apply(add_percentage_sign)
y[5] = y[5].apply(add_commas).apply(rv_zeros_af_dot).astype(str).apply(enToFarsiPandas2).apply(add_commas)




html = open_html()

data_jadval = y.values.tolist()
headers = ['ردیف','شرح','شماره قسط' , 'تاریخ بهره برداری تجاری','درصد مشمول جریمه','مبلغ جریمه','نام گستره']
#ghest_number = "شماره قسط"+id_ghest
header_contents = ['جرائم تاخیر در بهره برداری' , ' ', handle_month(id_ghest)]
html = add_header_document(html , header_contents)

html = add_headers(html , headers)

page_names = add_content(html , data_jadval)
pdf_names = add_page_counters(page_names)
pdf_names = make_pdfs(page_names,options='a3',css_path='resource/style.css')
file_name='jaraem_takhir_dar_bahre_bardari____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
combine_pdfs(pdf_names,file_name)
#print(file_name)

'''



