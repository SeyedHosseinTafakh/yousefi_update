# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 04:37:44 2020

@author: Hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


def get_peymankaran_d():
    return ([0,0,0])
    
    
    
    

def get_56_d():
    URL = 'http://api.daricbot.ir/jadval56_dollar'
    
    r = requests.get(url = URL)
    data = r.json()
    
    
    data['befor_p56']['sharh'] = 'پرداخت شده توسط شرکت نفتانیر'
    data['0']['sharh'] = 'پرداخت شده توسط شرکت نفتانیر'
    len(data)
    
    f = pd.DataFrame(columns=['idies'],data=list(range(1,len(data)+1)))
    x=pd.DataFrame(data).T
    
    x = x.reset_index()
    d = [f,x]
    x = pd.concat(d,axis=1,ignore_index=True,sort=False)
    
    x = x.fillna(0)
    x[4] = x[4].astype(float)
    
    x[4].sum()
    x[7].sum()
    return([x[4].sum(),x[7].sum(),x[4].sum()+x[7].sum()])
def get_36_d():
    URL = 'http://api.daricbot.ir/jadval36_dollar'
    
    r = requests.get(url = URL)
    data = r.json()
    
    x = pd.DataFrame(data)
    
    def replace_sharh(data):
        if data=='sharh':
            return 'تعهدات پرداخت 30'
        return data
    
    
    f = pd.DataFrame(columns=['idies'],data=list(range(1,len(data)+1)))
    x=pd.DataFrame(data)
    d = [f,x]
    x = pd.concat(d,axis=1,ignore_index=True,sort=False)
    
    
    
    x.index = range(1,x.shape[0]+1)
    x.columns = range(0,x.shape[1])
    
    x[3].sum()
    x[4].sum()
    return ([x[3].sum(),x[4].sum(),x[3].sum()+x[4].sum()])
def jadval_loole_sazi_sadid_d():
    
    return([0,0,0])

    
    
    

def get_arazi_d():
    return ([0,0,0])


def make_natayej_koli_d(id_ghest):
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))
        
    x=[]
    x.append(get_peymankaran_d())
    x.append(get_56_d())
    x.append(get_36_d())
    x.append(jadval_loole_sazi_sadid_d())
    x.append(get_arazi_d())
    
    y = pd.DataFrame(x)
    
    #idies = range(1,7)
    sharh = ['پیمانکاران','تامین لوله 56 اینچ','تامین لوله 30اینچ','لوله سازی سدید','تحصیل اراضی','کل']
    x = pd.concat([pd.DataFrame(sharh,columns=['sharh']),y],ignore_index=True,axis=1)
    x=x.fillna(0)
    x.at[5, 1]=x[1].sum()
    x.at[5, 2]=x[2].sum()
    x.at[5, 3]=x[3].sum()
    
    idies = pd.DataFrame(range(1,x.shape[0]+1))
    x = pd.concat([idies,x],axis=1)
    
    x.columns = range(0,5)
    
    x[0] = x[0].astype(str).apply(enToFarsiPandas)
    x[2] = x[2].astype(str).apply(enToFarsiPandas)
    x[3] = x[3].astype(str).apply(enToFarsiPandas)
    x[4] = x[4].astype(str).apply(enToFarsiPandas)
    
    
    output = x.values.tolist()
    headers = ['ردیف','شرح','اصل مطالبات','جریمه ها','کل مطالبات']
    header_contents = ['گزارش نتایج نهایی', shomare_ghest , JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = open_html()
    
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    html_data = add_content(html_data , output)
    page_names = add_page_counters(html_data)
    
    pdf_names = make_pdfs(page_names,css_path='temp/style_a4_2.css',options='a4')
    
    file_name='natayej_koli_dollar____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan=' ترازمالی –نتایج کلی –نتایج کلی دلاری'
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number=id_ghest,onvan=onvan,tarikh=tarikh)


    return True

#make_natayej_koli_d()



