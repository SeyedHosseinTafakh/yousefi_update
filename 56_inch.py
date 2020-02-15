# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:18:05 2020

@author: hossein
"""


import pandas as pd
import requests 
from writers import *
import pdfkit 
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
options = {
    'page-size': 'A3',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'landscape',
}


def make_56_pdf(file_name):    
    URL = 'https://api_resource.daricbot.ir/pipeLinesF'
    r = requests.get(url = URL) 
    data = dict(r.json())
    test = []
    for i in data.keys():
        test.append(data[str(i)]['dataBase'])
    x = pd.DataFrame(test)
    x = x.sort_values(4)
        
    for index,value in x[0].items():
        data[index] = data[str(index)]
        del(data[str(index)])
    i = 0
    output = []
    for data_point in data:
        x = []
        x.append(i)
        x.append(truncate(data[data_point]['motalebat_riyali'],2))
        x.append(0)
        x.append(truncate(data[data_point]['mablaghe_varagh'],2))
        x.append(truncate(data[data_point]['arzi_sakht_va_pooshesh'],2))
        x.append(truncate(float(data[data_point]['dataBase'][1]),2))#5
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
    sum_last_row = sum_last_row.append(pd.Series() , ignore_index=True)
    len_od_df = len(sum_last_row)-1
    
    sum_last_row.loc[len_od_df,0]= 'کل'
    sum_last_row.loc[len_od_df,1] = truncate(sum_last_row[1].sum())
    sum_last_row.loc[len_od_df,2] = truncate(sum_last_row[2].sum())
    sum_last_row.loc[len_od_df,3] = truncate(sum_last_row[3].sum())
    sum_last_row.loc[len_od_df,4] = truncate(sum_last_row[4].sum())
    sum_last_row.loc[len_od_df,5] = truncate(sum_last_row[5].sum())
    sum_last_row.loc[len_od_df,6] = truncate(sum_last_row[6].sum(skipna=True))
    sum_last_row.loc[len_od_df,7] = truncate(sum_last_row[7].sum(skipna=True))
    
    sum_last_row.loc[len_od_df,16] = truncate(sum_last_row[16].sum(skipna=True))
    sum_last_row.loc[len_od_df,17] = truncate(sum_last_row[17].sum())
    
    
    
    output2 = sum_last_row.values.tolist()
    html_data = open_html()
    headers = ['ردیف','جمع ریالی','جمع ارزی','مبلغ ورق','جمع دلاری ساخت و پوشش','ضخامت','متراژ','تناژ','تاریخ تحویل','نوع کالای تحویلی','شماره حواله انبار','شماره تقاضا','شماره قلم','نرخ تسعیر بانک مرکزی','هزینه انبارداری','هزینه صدور بیمه نامه','عوارض گمرکی','هزینه ساخت لوله','هزینه پوشش','مالیات ارزش افزوده و سایر خدمات (ورق)','مالیات ارزش افزوده و سایر خدمات (ساخت و پوشش)']

    header_contents = ['گزارش تراز مالی-لوله های 56(نتایج)', 'قسط شماره یکم آذر ماه 1396' , 'گذارش گیری در تاریخ: بهمن 1398']
    html_data = add_header_document(html_data , header_contents)

    html_data = add_headers(html_data , headers)
    html_data = add_content(html_data , output2)


    write_html_file('56_inch_html_file.html',html_data)
    pdfkit.from_file('shandool2.html', file_name,configuration=config , options=options)
    return True

make_56_pdf('testing.pdf')


