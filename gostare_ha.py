# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:09:30 2020

@author: Hossein
"""

from writers import *
import requests

def make_gostare_pdf(id_ghest , id_gostare):
    
    
    month = handle_month(int(id_ghest)).split('-')
    
    if int(month[1]) < 10:
        month[1]= '0'+month[1]
    
    month = month[0]+'-'+month[1]+'-'+month[2]
    
    
    URL = 'http://api.daricbot.ir/show_gostareha?gostare_id='+id_gostare+'&tarikh='+month
    r = requests.get(url = URL) 
    data = dict(r.json())
    
    
    labels=['نام گستره :','وزن گستره از کل :','درصد تحقق یافته :','درصد باقی مانده :','تاریخ بهره برداری برنامه ریزی شده :','مبلغ قابل پرداخت کل :','مبلغ پرداخت شده تا کنون :',' جریمه تاخیر در بهره برداری تاکنون :']
    
    spans=[data['name_gostare'],data['vazne_gostare_az_kol'],data['kare_anjam_gerefte'],data['baghimande_pishraft'],data['tarikh_barname_rizi_shode'],data['mablaghe_pardakhti_kol'],data['mablaghe_pardakhti_ta_konoon'],data['jaraem_tajamoee']]
    
    
    spans[1]=add_percentage_sign(enToFarsiPandas(spans[1]))
    spans[2]=add_percentage_sign(enToFarsiPandas(str(spans[2])))
    spans[3]=add_percentage_sign(enToFarsiPandas(str(spans[3])))
    
    spans[4] = enToFarsiPandas2(str(spans[4]))
    
    
    spans[5]= enToFarsiPandas(rv_zeros_af_dot(add_commas(spans[5])))
    
    spans[6]= enToFarsiPandas(rv_zeros_af_dot(add_commas(spans[6])))
    spans[7]= enToFarsiPandas(rv_zeros_af_dot(add_commas(spans[7])))
    
    
    
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html, labels)
    html = add_spans(html , spans)
    
    
    ghest_number = 'شماره قسط ' +' ' +enToFarsiPandas(id_ghest)
    
    header_contents = ['گزارش گستره ها', ghest_number ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    html = add_header_document(html , header_contents)
    output=[]
    html= add_content(html , output)
    
    
    page_names = add_page_counters(html)
    
    pdf_names = make_pdfs(page_names,css_path='temp/style_a4_2_Copy.css',options='a4')
    file_name ='gostare_ha___'+id_gostare+'__'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
        
    tarikh=JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')
    onvan='گزارش گستره'+' '+enToFarsiPandas(spans[0])
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number='',onvan=onvan,tarikh=tarikh)
    return True



