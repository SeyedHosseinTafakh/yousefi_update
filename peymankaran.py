


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger


def make_peymankaran_pdf():
    header = ['گذارش پیمانکاران','  ',JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    URL = 'https://api.daricbot.ir/peymankaran'
    r = requests.get(url = URL)
    data = r.json()
    x = pd.DataFrame(data)
    x = x.sort_values(4)
    sum_last_row = pd.DataFrame(x)
    sum_last_row[3] = sum_last_row[3].astype(float)
    sum_last_row[0] = sum_last_row[[0]].applymap(np.int64)
    sum_last_row[0] = list(range(1,len(sum_last_row)+1))
    
    #sum_last_row = sum_last_row.append(pd.Series() , ignore_index=True)
    len_od_df = len(sum_last_row)-1
    sum_last_row = sum_last_row.fillna(0)
    sum_last_row[0] = sum_last_row[[0]].applymap(np.int64)
    
    sum_last_row.loc[len_od_df,0] = 'کل'
    sum_last_row.loc[len_od_df,3] = truncate(sum_last_row[3].sum(skipna=True))
    sum_last_row[0] = sum_last_row[0].astype(str).map(enToFarsiPandas2)
    
    sum_last_row[3] = sum_last_row[3].map(add_commas).map(rv_zeros_af_dot).map(enToFarsiPandas2)
    sum_last_row[2] = sum_last_row[2].map(add_commas)
    sum_last_row[2] = sum_last_row[2].map(rv_zeros_af_dot).map(enToFarsiPandas2)
    
    sum_last_row[4] = sum_last_row[4].astype(str).map(enToFarsiPandas2)
    
    sum_last_row[5] = sum_last_row[5].astype(str).map(enToFarsiPandas2)
    
    
    
    output2 = sum_last_row.values.tolist()
    html_data = open_html()
    headers=['ردیف','نام پیمانکار','تاریخ چک','شماره چک','مبلغ چک','توضیحات']
    header_contents = header
    html_data = add_header_document(html_data , header_contents)
    
    html_data = add_headers(html_data , headers)
    page_names = add_content(html_data , output2,first_page_row_numbers=34,second_page_numbers=35)
    pdf_names = add_page_counters(page_names)
    pdf_names = make_pdfs(page_names,'a4','temp/style_a4_2.css')
    file_name ='peymankaran___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    combine_pdfs(pdf_names,file_name)
    

#testingnkaran_pdf('peymankaran.pdf',{'right':'گﺫﺍﺮﺷ پیﻡﺎﻧکﺍﺭﺎﻧ', 'middle':' ' , 'left':'ﺎﺴﻔﻧﺩ 1398'})
#make_peymankaran_pdf('peymankaran.pdf',{'right':'گذارش پیمانکاران', 'middle':' ' , 'left':'اسفند 1398'})


make_peymankaran_pdf()



