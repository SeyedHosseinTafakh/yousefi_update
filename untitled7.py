# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:47:05 2020

@author: hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger





gostare_id = '3'
id_ghest = '13'
URL = 'http://api.daricbot.ir/jaraem_taakhir_dar_bahre_bardariV2?gostare_id='+gostare_id+'&'+'id_ghest'+'='+id_ghest+'&date='+handle_month(id_ghest)
data = requests.get(url = URL)
data = data.json()


labels = ['نام گستره :','وزن گستره از کل :','درصد تحقق یافته :','درصد باقی مانده :','تاریخ بهره برداری برنامه ریزی شده :']

jarime_koli = data['jadval_koli']

jarime_koli = list(jarime_koli.values())

jarime_koli[1] = enToFarsiPandas(jarime_koli[1])
jarime_koli[2] = enToFarsiPandas(str(jarime_koli[2]))
jarime_koli[3] = enToFarsiPandas(str(jarime_koli[3]))
jarime_koli[4] = enToFarsiPandas(str(jarime_koli[4]))



appendence = data['an_ghozi']
appendence.append(id_ghest)
appendence.append(data['moghadasi_jat'])

data = data['jarime']
data = pd.DataFrame(data)
data = data.sort_values(2)
del data[6]
jarime_kol = data[1].sum() + appendence[1]

data = data.append([appendence],ignore_index=True)


data[0] = data[0].map(enToFarsiPandas)
data[1] = data[1].map(add_commas).astype(str).map(truncate_str).map(enToFarsiPandas).map(rv_zeros_af_dot)
data[2] = data[2].map(enToFarsiPandas2)

data[3] = data[3].astype(str).map(truncate_str).map(enToFarsiPandas).map(add_percentage_sign)
data[4] = data[4].astype(str).map(enToFarsiPandas)
data[5] = data[5].astype(str).map(add_check_mark)

appendence = ['جمع کل',enToFarsiPandas(truncate_str(str(jarime_kol))),'-',add_percentage_sign(jarime_koli[1]) , enToFarsiPandas(str(id_ghest)),'-']
data = data.append([appendence],ignore_index=True)

html = open_html()
html = add_div_and_seprator_for_info(html)
html = add_labels(html , labels)
html = add_spans(html , jarime_koli)

#write_html_file('testing_new_extentions_method.html',html)

output = pd.DataFrame(data.values.tolist())
output[0] = range(1,data.shape[0]+1)
output[1] = data[0]
output[2] = data[4]
output[3] = data[2]
output[4] = data[3]
output[5] = data[1]
output[6] = data[5]


output = output.values.tolist()
#html_data = open_html()
html_data = html
headers = ['ردیف','شرح','شماره قسط' , 'تاریخ بهره برداری تجاری','درصد مشمول جریمه','مبلغ جریمه','در محاسبات اقساط لحاظ گردد']
header_contents = ['right' , 'middle', 'left']
html_data = add_header_document(html_data , header_contents)

html_data = add_headers(html_data , headers)
#todo :: have to add css editor and end this section
page_names = add_content(html_data , output)
pdf_names = add_page_counters(page_names)
pdf_names = make_pdfs(page_names)
combine_pdfs(pdf_names,'test_jaraem_taakhir_dar_bahrebardari.pdf')
















