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


def get_peymankaran():
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
    return ([x[3].sum(),x[5].apply(abs).sum(),x[3].sum()+x[5].apply(abs).sum()])
    
    
    
    

def get_56():
    URL = 'http://api.daricbot.ir/jadval56'
    
    r = requests.get(url = URL)
    data = r.json()
    
    
    data['befor']['sharh'] = 'پرداخت شده توسط شرکت نفتانیر'
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
def get_36():
    URL = 'http://api.daricbot.ir/jadval36'
    
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
def jadval_loole_sazi_sadid():
    URL = 'http://api.daricbot.ir/jadval_loole_sazi_sadid'
    
    r = requests.get(url = URL)
    data = r.json()
    
    x = pd.DataFrame(data).T
    
    
    x.columns = range(0,x.shape[1])
    
    x[0].astype(float).sum()
    x[2].astype(float).sum()
    return([x[0].astype(float).sum(),x[2].astype(float).sum(),x[0].astype(float).sum()+x[2].astype(float).sum()])

    
    
    

def get_arazi():
    URL = 'http://api.daricbot.ir/jadvalArazi'
    data = requests.get(url = URL)
    data = data.json()
    
    for key in list(data.keys()):
        data[key]= list(data[key].values())
    data = list(data.values())
    
    data = pd.DataFrame(data)
    
    data[2].sum()
    data[4].sum()
    return ([data[2].sum(),data[4].sum(),data[2].sum()+data[4].sum()])


def make_natayej_koli():
        
    x=[]
    x.append(get_peymankaran())
    x.append(get_56())
    x.append(get_36())
    x.append(jadval_loole_sazi_sadid())
    x.append(get_arazi())
    
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
    header_contents = ['گذارش نتایج نهایی', ' ' , JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = open_html()
    
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    html_data = add_content(html_data , output)
    page_names = add_page_counters(html_data)
    
    pdf_names = make_pdfs(page_names,css_path='temp/style_a4_2.css',options='a4')
    
    file_name='natayej_koli____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan='گذارش نتایج نهایی'
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number='',onvan=onvan,tarikh=tarikh)


    return True

#make_natayej_koli()
