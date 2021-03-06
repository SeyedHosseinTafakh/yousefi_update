# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:46:00 2020

@author: hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger

URL = 'http://api.daricbot.ir/arazi'
data = requests.get(url = URL)
data = data.json()


data = pd.DataFrame(data)
headers = ['ردیف','شرح','مبلغ درخواستی نفتانیر','مبلغ مورد تاییدامور حقوقی','تاریخ تایید امور حقوقی','مبلغ تایید مالی','تاریخ تاییدامور مالی']
header_contents = ['گزارش تحصیل اراضی', '  ' , 'گذارش گیری در تاریخ: بهمن 1398']
del(data[7])
del(data[8])

data[0]=data[0].astype(str).map(enToFarsiPandas2)
data[2] = data[2].astype(str).map(enToFarsiPandas2)
data[3] = data[3].astype(str).map(enToFarsiPandas2)
data[5] = data[5].astype(str).map(enToFarsiPandas2)

data[4] = data[4].astype(str).map(enToFarsiPandas2)
data[6] = data[6].astype(str).map(enToFarsiPandas2)
output= data.values.tolist()
options = {
    'page-size': 'A4',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'Portrait',
}


html_data = open_html()
html_data = add_header_document(html_data , header_contents)
html_data = add_headers(html_data , headers)
page_names = add_content(html_data , output)
pdf_names = add_page_counters(page_names)
pdf_names = make_pdfs(page_names)
combine_pdfs(pdf_names,'test_tahsil_arazi.pdf')

