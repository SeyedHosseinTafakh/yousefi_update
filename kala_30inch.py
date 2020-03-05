# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:16:36 2020

@author: hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


#def make_tahodat_mohandesi_pdf(file_name , headers):

URL = 'http://api.daricbot.ir/kala_30'
data = requests.get(url = URL)
data = data.json()


labels = ['استعلام 1:','استعلام 2:','استعلام 3:','میانگین سه استعلام :','مالیات ارزش افزوده و سایر خدمات :']
spans = []
for record in data['database_record1']:
    spans.append(truncate_str(enToFarsiPandas2(str(add_commas(record)))))
spans.append(truncate_str(enToFarsiPandas2(str(add_commas(data['miyangin__1'])))))
spans.append(truncate_str(enToFarsiPandas2(str(add_commas(data['maliayt__1'])))))

header_contents = ['right' , 'middle', 'left']

html = open_html()
html = add_div_and_seprator_for_info(html)
html = add_labels(html , labels)
html = add_spans(html , spans)
output=[]
html= add_header_document(html , header_contents)
page_names = add_content(html , output)
pdf_names = add_page_counters(page_names)
first_pdf_name = make_pdfs([page_names[0]],'resource/style_height.css')
combine_pdfs(first_pdf_name,'test_kala_30.pdf')










