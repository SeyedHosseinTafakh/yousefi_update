# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:58:10 2020

@author: Hossein
"""

import pandas as pd
from writers import *


def make_model_mali_pdf(id_ghest):
    shomare_ghest = 'شماره قسط'+enToFarsiPandas2(str(id_ghest))

    kole_gharardad = pd.read_csv('model_mali/01.csv')
    
    kole_gharardad.columns = range(0,5)
    
    def replace_dots_with_commas(data):
        data = data.replace('.',',')
        return data
    
    kole_gharardad[2]=kole_gharardad[2].apply(replace_dots_with_commas).apply(enToFarsiPandas)
    kole_gharardad[1]=kole_gharardad[1].apply(replace_dots_with_commas).apply(enToFarsiPandas)
    kole_gharardad[3]=kole_gharardad[3].apply(replace_dots_with_commas).apply(enToFarsiPandas)
    kole_gharardad[4]=kole_gharardad[4].apply(replace_dots_with_commas).apply(enToFarsiPandas)
    kole_gharardad[0]=kole_gharardad[0].astype(str).apply(enToFarsiPandas)
    
    headers = ['ماه','کل قرارداد','هزینه','بازپرداخت','جریان نقدی']
    labels = ['هزینه اجرایی :','مالیات بر ارزش افزوده :','بازپرداخت :','IRR :','هزینه مدیریت :','سرمایه گذاری :','وزن از کل :']
    spans=['13,870,000,000','1,470,220,000','228,000,000','23.879 %','832,200,000','-1,617,242,000','100 %']
    
    #spans[5]=int(spans[5])*-1
    #spans[5]=add_commas(spans[5])
    #spans[5]=enToFarsiPandas(spans[5])
    for i in range(len(spans)):
        spans[i] = enToFarsiPandas(spans[i])
    
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html, labels)
    html = add_spans(html , spans)
    
    
    header_contents = ['مدل مالی کل قرارداد', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    #test = kole_gharardad.iloc[:14]
    output= kole_gharardad.iloc[:22].values.tolist()
    
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output)
    page_names = add_page_counters(html)
    
    pdf_names = make_pdfs(page_names,css_path='temp/style_a4_2_Copy.css',options='a4')
    
    output=kole_gharardad.iloc[22:].values.tolist()
    html = open_html()
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output)
    page_names= add_page_counters(html,pusher=1)
    pdf_names += make_pdfs(page_names,css_path='temp/style_a4_2.css',options='a4')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #----------------------------------------------------------------
    
    csv_gostareha = pd.read_csv('model_mali/etelaatmodemali.csv')
    
    
    for i in range(0,csv_gostareha.shape[0]):
        csv_gostareha.loc[i] = csv_gostareha.loc[i].astype(str).apply(replace_dots_with_commas).apply(enToFarsiPandas)
    csv_gostareha.columns = range(0,15)
    
    gostare_1 = csv_gostareha.loc[1:,0:4]
    
    headers = csv_gostareha.loc[:0].fillna('-').values.tolist()[0][0:5]
    headers[2]=''
    
    header_contents = [' مدل مالی به تفکیک گستره ها و خطوط فشار', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    output = gostare_1.values.tolist()
    output=gostare_1.values.tolist()
    html = open_html()
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output,first_page_row_numbers=21)
    page_names= add_page_counters(html)
    pdf_names += make_pdfs(page_names,css_path='resource/style.css',options='a3')
    #-----------------------------------------------------------------
    gostare_2 = csv_gostareha.loc[1:,5:9]
    
    headers = csv_gostareha.loc[:0].fillna('-').values.tolist()[0][5:10]
    
    header_contents = [' مدل مالی به تفکیک گستره ها و خطوط فشار', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    output=gostare_2.values.tolist()
    html = open_html()
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output,first_page_row_numbers=21)
    page_names= add_page_counters(html,slider='-1')
    pdf_names += make_pdfs(page_names,css_path='resource/style.css',options='a3')
    #-----------------------------------------------------------------
    gostare_3 = csv_gostareha.loc[1:,10:15]
    
    headers = csv_gostareha.loc[:0].fillna('-').values.tolist()[0][10:15]
    
    header_contents = [' مدل مالی به تفکیک گستره ها و خطوط فشار', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    
    output=gostare_3.values.tolist()
    html = open_html()
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output,first_page_row_numbers=21)
    page_names= add_page_counters(html,slider='-2')
    pdf_names += make_pdfs(page_names,css_path='resource/style.css',options='a3')
    
    
    
    
    #------------------------------------------------------------------
    
    khotoote_enteghal = pd.read_csv('model_mali/011.csv')
    
    headers = ['ماه','کل قرارداد','هزینه','بازپرداخت','جریان نقدی']
    
    labels = ['هزینه اجرایی :','هزینه مدیریت :','مالیات بر ارزش افزوده :','سرمایه گذاری :','بازپرداخت :','وزن از کل :','IRR :']
    
    
    
    spans=['88,393,510,000,000','53,036,106','93,697,121','-1,030,668,327','1,488,659,361','67.73 %','23.879 %']
    
    
    for i in range(len(spans)):
        spans[i] = enToFarsiPandas2(spans[i])
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html, labels)
    html = add_spans(html , spans)
    
    khotoote_enteghal.columns = range(0,5)
    
    khotoote_enteghal[0]=khotoote_enteghal[0].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[1]=khotoote_enteghal[1].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[2]=khotoote_enteghal[2].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[3]=khotoote_enteghal[3].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[4]=khotoote_enteghal[4].astype(str).apply(enToFarsiPandas)
    
    
    header_contents = ['مدل مالی خطوط انتقال', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    #test = kole_gharardad.iloc[:14]
    output= khotoote_enteghal.iloc[:22].values.tolist()
    
    
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html, labels)
    html = add_spans(html , spans)
    
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output)
    page_names = add_page_counters(html)
    
    pdf_names += make_pdfs(page_names,css_path='temp/style_a4_2_Copy.css',options='a4')
    
    output= khotoote_enteghal.iloc[22:].values.tolist()
    html = open_html()
    
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output)
    page_names = add_page_counters(html,pusher=1)
    pdf_names += make_pdfs(page_names,css_path='temp/style_a4_2_Copy.css',options='a4')
    
    
    #------------------------------------------------------
    
    
    
    khotoote_enteghal = pd.read_csv('model_mali/012.csv')
    monthes = range(1,43)
    monthes = pd.DataFrame(monthes)
    
    headers = ['ماه','کل قرارداد','هزینه','بازپرداخت','جریان نقدی']
    
    labels = ['هزینه اجرایی :','هزینه مدیریت :','مالیات بر ارزش افزوده :','سرمایه گذاری :','بازپرداخت :','وزن از کل :','IRR :']
    
    
    spans=['503,064,900,000','30,183,894,879','53,324','-586,573,673','791,340,639','36.27 %','23.879 %']
    
    
    for i in range(len(spans)):
        spans[i] = enToFarsiPandas2(spans[i])
    
    khotoote_enteghal.columns = range(0,5)
    del(khotoote_enteghal[4])
    khotoote_enteghal.columns = range(1,5)
    khotoote_enteghal.index = range(0,42)
    khotoote_enteghal = pd.concat([monthes,khotoote_enteghal],ignore_index=True,axis=1)
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html, labels)
    html = add_spans(html , spans)
    
    
    khotoote_enteghal[0]=khotoote_enteghal[0].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[1]=khotoote_enteghal[1].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[2]=khotoote_enteghal[2].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[3]=khotoote_enteghal[3].astype(str).apply(enToFarsiPandas)
    khotoote_enteghal[4]=khotoote_enteghal[4].astype(str).apply(enToFarsiPandas)
    
    
    header_contents = ['مدل مالی خطوط انتقال', shomare_ghest ,JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')]
    #test = kole_gharardad.iloc[:14]
    output= khotoote_enteghal.iloc[:22].values.tolist()
    
    
    
    html = open_html()
    html = add_div_and_seprator_for_info(html)
    html = add_labels(html, labels)
    html = add_spans(html , spans)
    
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output)
    page_names = add_page_counters(html)
    pdf_names += make_pdfs(page_names,css_path='temp/style_a4_2_Copy.css',options='a4')
    
    output= khotoote_enteghal.iloc[22:].values.tolist()
    html = open_html()
    
    html = add_header_document(html , header_contents)
    html = add_headers(html , headers)
    html= add_content(html , output)
    page_names = add_page_counters(html,pusher=1)
    pdf_names += make_pdfs(page_names,css_path='temp/style_a4_2_Copy.css',options='a4')
    
    
    
    
    file_name ='model_mali___'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
    
    tarikh=JalaliDatetime.now().strftime('%B')+'  '  + JalaliDatetime.now().strftime('%Y')
    onvan='گزارش مدل مالی'
    combine_pdfs(pdfs=pdf_names,result_name=file_name,ghest_number='',onvan=onvan,tarikh=tarikh)
    return True





