# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:18:05 2020

@author: hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


def make_56_pdf():

    URL = 'https://api.daricbot.ir/pipeLinesF'
    r = requests.get(url = URL) 
    data = dict(r.json())
    
    i = 0
    output = []
    for data_point in data:
        x = []
        x.append(i)
        x.append(truncate(data[data_point]['motalebat_riyali'],2))
        x.append(data[data_point]['mablaghe_varagh']+data[data_point]['arzi_sakht_va_pooshesh'])
        #x.append(0)
        x.append(truncate(data[data_point]['mablaghe_varagh'],2))
        x.append(truncate(data[data_point]['arzi_sakht_va_pooshesh'],2))
        x.append(truncate(float(data[data_point]['dataBase'][1]),2))#5
        #x.append(data[data_point]['dataBase'][1])
        x.append(float(data[data_point]['dataBase'][2]))
        x.append(truncate(float(data[data_point]['dataBase'][3]),2))
        x.append(data[data_point]['dataBase'][4])
        x.append(data[data_point]['dataBase'][5])
        x.append(data[data_point]['dataBase'][6])
        x.append(data[data_point]['dataBase'][7])
        x.append(data[data_point]['dataBase'][8])
        x.append(data[data_point]['dataBase'][9])
        x.append(data[data_point]['dataBase'][10])
        x.append(data[data_point]['dataBase'][11])
        x.append(truncate(data[data_point]['avarez_gomrok'],2))
        x.append(truncate(data[data_point]['hazine_sakhte_loole'],2))
        x.append(truncate(data[data_point]['hazine_pooshesh'],2))
        x.append(truncate(data[data_point]['maliyat_bar_arzesh_varagh'],2))
        x.append(truncate(data[data_point]['maliyat_bara_arzesh_afzoode_sakhte_pooshesh'],2))
        output.append(x)
        i +=1
    
    
    
    sum_last_row = pd.DataFrame(output,dtype='float64')
    
    sum_last_row = sum_last_row.sort_values(8)
    sum_last_row[0]=range(1,sum_last_row.shape[0]+1)
    #sum_last_row = sum_last_row.append(pd.Series() , ignore_index=True)
    len_od_df = len(sum_last_row)-1
    
    sum_last_row.loc[len_od_df,0]= 'کل'
    sum_last_row.loc[len_od_df,1] = truncate(sum_last_row[1].sum())
    sum_last_row.loc[len_od_df,2] = truncate(sum_last_row[2].sum())
    sum_last_row.loc[len_od_df,3] = truncate(sum_last_row[3].sum())
    sum_last_row.loc[len_od_df,4] = truncate(sum_last_row[4].sum())
    sum_last_row.loc[len_od_df,5] = truncate(sum_last_row[5].sum())
    sum_last_row.loc[len_od_df,6] = truncate(sum_last_row[6].sum(skipna=True))
    #sum_last_row.loc[len_od_df,7] = truncate(sum_last_row[7].sum(skipna=True))
    
    sum_last_row.loc[len_od_df,16] = truncate(sum_last_row[16].sum(skipna=True))
    sum_last_row.loc[len_od_df,17] = truncate(sum_last_row[17].sum())
    
    sum_last_row[0] = sum_last_row[0].astype(str).map(enToFarsiPandas2).map(rv_zeros_af_dot)
    sum_last_row[1] = sum_last_row[1].astype(str).map(enToFarsiPandas2)
    sum_last_row[2] = sum_last_row[2].astype(str).map(enToFarsiPandas2)
    sum_last_row[3] = sum_last_row[3].astype(str).map(enToFarsiPandas2)
    sum_last_row[4] = sum_last_row[4].astype(str).map(enToFarsiPandas2).map(rv_zeros_af_dot)
    sum_last_row[5] = sum_last_row[5].astype(str).map(enToFarsiPandas2).map(rv_zeros_af_dot)
    sum_last_row[6] = sum_last_row[6].astype(str).map(enToFarsiPandas2)
    sum_last_row[7] = sum_last_row[7].astype(str).map(enToFarsiPandas2)
    sum_last_row[8] = sum_last_row[8].astype(str).map(enToFarsiPandas2)
    
    for i in range(9,15):
        sum_last_row[i] = sum_last_row[i].astype(str).map(enToFarsiPandas2).map(rv_zeros_af_dot)
    for i in range(14,21):
        sum_last_row[i] = sum_last_row[i].astype(str).map(truncate_str).map(enToFarsiPandas2)
    
    
    
    output1 = sum_last_row.loc[:,0:13]
    output2 = sum_last_row.loc[:,14:]
    output1 = output1.values.tolist()
    output2 = output2.values.tolist()
    #headers = ['ردیف','جمع ریالی','مبلغ ورق','جمع دلاری ساخت و پوشش','ضخامت','متراژ','تناژ','تاریخ تحویل','نوع کالای تحویلی','شماره حواله انبار','شماره تقاضا','شماره قلم','نرخ تسعیر بانک مرکزی','هزینه انبارداری','هزینه صدور بیمه نامه','عوارض گمرکی','هزینه ساخت لوله','هزینه پوشش','مالیات ارزش افزوده و\n سایر خدمات (ورق)','مالیات ارزش افزوده و سایر خدمات (ساخت و پوشش)']
    #headers = ['ردیف','جمع ریالی','مبلغ ورق','جمع دلاری ساخت و پوشش','ضخامت','متراژ','تناژ','تاریخ تحویل','نوع کالای تحویلی','شماره حواله انبار','شماره تقاضا','شماره قلم','نرخ تسعیر بانک مرکزی','هزینه انبارداری','هزینه صدور بیمه نامه','عوارض گمرکی','هزینه ساخت لوله','هزینه پوشش','مالیات \n (ورق)','مالیات  (ساخت و پوشش)']
    #headers = ['ردیف','جمع ریالی','مبلغ ورق','جمع دلاری ساخت و پوشش','ضخامت','متراژ','تناژ','تاریخ تحویل','نوع کالای تحویلی','شماره حواله انبار','شماره تقاضا','شماره قلم','نرخ تسعیر بانک مرکزی','هزینه انبارداری','هزینه صدور بیمه نامه','عوارض گمرکی','هزینه ساخت لوله','هزینه پوشش','مالیات \n (ورق)','مالیات  (ساخت و پوشش)']
    
    headers = ['ردیف','جمع ریالی','جمع ارزی','مبلغ ورق','جمع دلاری ساخت و پوشش','ضخامت','متراژ','تناژ','تاریخ تحویل','نوع کالای تحویلی','شماره حواله انبار','شماره تقاضا','شماره قلم','نرخ تسعیر بانک مرکزی']
    headers2=['هزینه انبارداری','هزینه صدور بیمه نامه','عوارض گمرکی','هزینه ساخت لوله','هزینه پوشش','مالیات ارزش افزوده و سایر خدمات (ورق)','مالیات ارزش افزوده و سایر خدمات (ساخت و پوشش)']
    
    header_contents = ['گزارش تراز مالی لوله های 56', '' ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    html_data = open_html()
    
    html_data = add_header_document(html_data , header_contents)
    html_data = add_headers(html_data , headers)
    html_data = add_content(html_data , output1)
    page_names = add_page_counters(html_data)
    
    
    html_data = open_html()
    html_data = add_header_document(html_data , header_contents)
    html_data = add_headers(html_data , headers2)
    html_data = add_content(html_data , output2)
    page_names += add_page_counters(html_data,slider='/1')
    
    file_name ='taraz_mali_56___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    pdf_names = make_pdfs(page_names,css_path='resource/style.css',options='a3')
    tarikh=JalaliDatetime.now().strftime('%Y/%m/%d')
    onvan='ترازمالی –نتایج کلی –لوله های 56اینچ'
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number='',onvan=onvan,tarikh=tarikh)



    return True

#make_56_pdf()


