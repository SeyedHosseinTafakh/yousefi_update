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


def make_pishraft_fiziki_pdf(id_ghest):
#id_gostare = '1'
#id_ghest=16
    URL = 'https://api.daricbot.ir/gostare'
    data = requests.get(url = URL)
    data = data.json()
    
    pishraft_data = pd.DataFrame(data['pishraft'])
    
    
    pishraft_info = pishraft_data.loc[pishraft_data[4]<=int(id_ghest)]
    
    pishraft_info = pishraft_info.reset_index()
    x = pishraft_info[1].astype(str).apply(change_gostare_id_to_name)
    pishraft_info[1] = x
    pishraft_info[0] = range(1,pishraft_info.shape[0]+1)
    #del(pishraft_info['level_0'])
    del(pishraft_info[6])
    del(pishraft_info['index'])
    del(pishraft_info[7])
    #del(pishraft_info[0])
    #del(pishraft_info[1])
    labels = ['نام گستره :','وزن گستره از کل :','درصد تحقق یافته :','درصد باقی مانده :']
    
    #pishraft_re = []
    #pishraft_re.append(list(range(1,pishraft_info.shape[0]+1)))
    #pishraft_re.append(pishraft_info[4].tolist())
    #pishraft_re.append(pishraft_info[5].tolist())
    #pishraft_re.append(pishraft_info[3].tolist())
    #pishraft_re.append(pishraft_info[2].tolist())
    #pishraft_re.append(pishraft_info[7].tolist())
    
    #columns = {'1':list(range(1,pishraft_info.shape[0]+1)),
    #           '2':pishraft_info[4].tolist(),
    #           '3':pishraft_info[5].tolist(),
    #           '4':pishraft_info[3].tolist(),
    #           '5':pishraft_info[2].tolist(),
    #           '6':pishraft_info[7].tolist()}
    #pishraft_re = pd.DataFrame(columns)
    #pishraft_re = pishraft_re.append(pishraft_re)
        
    #----------------farsi sazi
    
    pishraft_info[0]=pishraft_info[0].astype(str).apply(enToFarsiPandas2)
    pishraft_info[2]=pishraft_info[2].astype(str).apply(enToFarsiPandas2)
    pishraft_info[3]=pishraft_info[3].astype(str).apply(enToFarsiPandas2)
    pishraft_info[4]=pishraft_info[4].astype(str).apply(enToFarsiPandas2)
    
    
    #pishraft_re['1'] = pishraft_re['1'].astype(str).map(enToFarsiPandas)
    #pishraft_re['2'] = pishraft_re['2'].astype(str).map(enToFarsiPandas)
    #pishraft_re['4'] = pishraft_re['4'].astype(str).map(enToFarsiPandas2)
    #pishraft_re['5'] = pishraft_re['5'].astype(str).map(enToFarsiPandas)
    #pishraft_re['6'] = pishraft_re['6'].astype(str).map(enToFarsiPandas)
    
    
    
    
    #----------------end farsi sazi
    #baghi_jadval = pd.DataFrame(pishraft_re)
    #pishraft_re = pishraft_re.iloc[:17]
    
    
    output = pishraft_info.values.tolist()
    #---------------------------------------------------
    #pdf_name = ' گذارش پیشرفت فیزیکی' +' '+gostare_info[0][1]+' '+ JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')+".pdf"
    #pdf_name='pishraft_fiziki___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    #---------------------------------------------------
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    #html = add_labels(html , labels)
    #html = add_spans(html , jadval_info)
    time = JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')
    headers = ['ردیف','نام گستره','درصد تحقق یافته','تاریخ','شماره قسط','شرح']
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))
    header_contents = ['گزارش پیشرفت فیزیکی' , shomare_ghest, time]
    
    html_data = add_header_document(html , header_contents)
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output)
    pdf_names = add_page_counters(page_names)
    pdf_names=make_pdfs(page_names,'a3','resource/style.css')
    #combine_pdfs(pdf_names,pdf_name)
    
    
    
    
    file_name ='pishraft_fiziki___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')

    onvan='تراز مالی - نتایج - پیشرفت فیزیکی'
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)

    
    
    return True


#make_pishraft_fiziki_pdf(16)



