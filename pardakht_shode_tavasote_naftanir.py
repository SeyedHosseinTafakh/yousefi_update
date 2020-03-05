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
header_contents = ['right' , 'middle', 'left']

data[0] = pd.Series(list(range(1,len(data)+1)))
data[0] = data[0].astype(str).map(enToFarsiPandas)
data[1] = data[1].astype(str).map(enToFarsiPandas2)
data[2] = data[2].astype('int64').map(add_commas).astype(str).map(rv_zeros_af_dot).map(enToFarsiPandas2)
data[4] = data[4].map(enToFarsiPandas)


baghi_jadval = pd.DataFrame(data)
data = data.iloc[:17]
output = data.values.tolist()


html_data = add_header_document(html , header_contents)
html_data = add_headers(html_data , headers)
page_names = add_content(html_data , output)
pdf_names = add_page_counters(page_names)
first_pdf_name = make_pdfs([page_names[0]],'resource/style_height.css')
if baghi_jadval.shape[0]-data.shape[0]>0:
    output = pd.DataFrame(baghi_jadval.iloc[17:]).values.tolist()
    html = open_html()
    html_data = add_header_document(html , header_contents)
    html_data = add_headers(html_data , headers)

    page_names = add_content(html_data , output)
    pdf_names = pdf_names+add_page_counters(page_names,pusher=1)
    #first_pdf_name = make_pdfs([page_names[0]],'resource/style_height.css')
    del(pdf_names[0])
    pdf_names=make_pdfs(page_names,'resource/style.css')

    combine_pdfs(first_pdf_name+pdf_names,'test_pardakht_naftanir.pdf')
else:
    del(pdf_names[0])
    combine_pdfs(first_pdf_name,'test_pardakht_naftanir.pdf')

#TODO:: have lot of fixes









