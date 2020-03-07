# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:12:07 2020

@author: hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


def make_pishraft_fiziki_pdf(id_gostare):
    #id_gostare = '1'
    URL = 'http://api.daricbot.ir/gostare'
    data = requests.get(url = URL)
    data = data.json()
    
    options = {
     'page-size': 'A4',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'portrait',
      }
    
    gostare_data = pd.DataFrame(data['gostareha'])
    pishraft_data = pd.DataFrame(data['pishraft'])
    
    
    gostare_info=gostare_data.loc[gostare_data[0]==int(id_gostare)]
    pishraft_info = pishraft_data.loc[pishraft_data[1]==int(id_gostare)]
    
    labels = ['نام گستره :','وزن گستره از کل :','درصد تحقق یافته :','درصد باقی مانده :']
    gostare_info = gostare_info.values.tolist()
    
    jadval_info = []
    jadval_info.append(gostare_info[0][1])
    jadval_info.append(gostare_info[0][2])
    jadval_info.append(str(pishraft_info[2].astype(float).sum()))
    jadval_info.append(str(pishraft_info[2].astype(float).sum() -float(gostare_info[0][2])))
    
    
    del(pishraft_info[0])
    del(pishraft_info[1])
    
    pishraft_re = []
    pishraft_re.append(list(range(1,pishraft_info.shape[0]+1)))
    pishraft_re.append(pishraft_info[4].tolist())
    pishraft_re.append(pishraft_info[5].tolist())
    pishraft_re.append(pishraft_info[3].tolist())
    pishraft_re.append(pishraft_info[2].tolist())
    pishraft_re.append(pishraft_info[7].tolist())
    
    columns = {'1':list(range(1,pishraft_info.shape[0]+1)),
               '2':pishraft_info[4].tolist(),
               '3':pishraft_info[5].tolist(),
               '4':pishraft_info[3].tolist(),
               '5':pishraft_info[2].tolist(),
               '6':pishraft_info[7].tolist()}
    pishraft_re = pd.DataFrame(columns)
    #pishraft_re = pishraft_re.append(pishraft_re)
        
    #----------------farsi sazi
    
    pishraft_re['1'] = pishraft_re['1'].astype(str).map(enToFarsiPandas)
    pishraft_re['2'] = pishraft_re['2'].astype(str).map(enToFarsiPandas)
    pishraft_re['4'] = pishraft_re['4'].astype(str).map(enToFarsiPandas2)
    pishraft_re['5'] = pishraft_re['5'].astype(str).map(enToFarsiPandas)
    pishraft_re['6'] = pishraft_re['6'].astype(str).map(enToFarsiPandas)
    
    
    
    
    #----------------end farsi sazi
    baghi_jadval = pd.DataFrame(pishraft_re)
    pishraft_re = pishraft_re.iloc[:17]
    
    
    output = pishraft_re.values.tolist()
    #---------------------------------------------------
    #pdf_name = ' گذارش پیشرفت فیزیکی' +' '+gostare_info[0][1]+' '+ JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')+".pdf"
    pdf_name='pishraft_fiziki.pdf'
    #---------------------------------------------------
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html , labels)
    html = add_spans(html , jadval_info)
    time = JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')
    headers = ['ردیف','شماره قسط','شرح','تاریخ','درصد تحقق یافته','-']
    header_contents = ['گذارش پیشرفت فیزیکی' , ' ', time]
    
    html_data = add_header_document(html , header_contents)
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output)
    pdf_names = add_page_counters(page_names)
    first_pdf_name = make_pdfs([page_names[0]],'a4','resource/style_height_pishraft_fiziki.css')
    if baghi_jadval.shape[0]-pishraft_re.shape[0]>0:
        output = pd.DataFrame(baghi_jadval.iloc[17:]).values.tolist()
        html = open_html()
        html_data = add_header_document(html , header_contents)
        html_data = add_headers(html_data , headers)
    
        page_names = add_content(html_data , output)
        pdf_names = pdf_names+add_page_counters(page_names,pusher=1)
        #first_pdf_name = make_pdfs([page_names[0]],'resource/style_height.css')
        del(pdf_names[0])
        pdf_names=make_pdfs(page_names,'a4','temp/style_a4_1.css')
    
        combine_pdfs(first_pdf_name+pdf_names,pdf_name)
    else:
        del(pdf_names[0])
        combine_pdfs(first_pdf_name,pdf_name)
    return True






