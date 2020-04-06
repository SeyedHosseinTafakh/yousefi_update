# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:35:46 2020

@author: Hossein
"""


import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger



def make_jaraem_takhir_dar_bahre_bardari(id_gostare,id_ghest):
	gostare_id = id_gostare
	id_ghest = id_ghest
	URL = 'http://api.daricbot.ir/jaraem_taakhir_dar_bahre_bardariV2?gostare_id='+gostare_id+'&'+'id_ghest'+'='+id_ghest+'&date='+handle_month(id_ghest)
	data = requests.get(url = URL)
	data = data.json()
	del(gostare_id)
	del(URL)


	jadval_koli = data['jadval_koli']

	jadval_koli['vazne_kole_khat'] = enToFarsiPandas(str(jadval_koli['vazne_kole_khat']))
	jadval_koli['tarikh'] = enToFarsiPandas(str(jadval_koli['tarikh']))
	jadval_koli['darsad_tahaghogh_yafte'] = enToFarsiPandas(str(jadval_koli['darsad_tahaghogh_yafte']))
	jadval_koli['darsad_baghi_mande'] = enToFarsiPandas(str(jadval_koli['darsad_baghi_mande']))


	sum_jadval = data['an_ghozi']
	sum_jadval[1] = enToFarsiPandas(str(sum_jadval[1]))
	sum_jadval[2] = enToFarsiPandas(str(sum_jadval[2]))
	sum_jadval[3] = enToFarsiPandas(str(sum_jadval[3]))


	data_jadval = data['jarime']
	del(data)

	data_jadval = pd.DataFrame(data_jadval)
	del(data_jadval[6])

	data_jadval[1] = data_jadval[1].astype(str).map(enToFarsiPandas)
	data_jadval[2] = data_jadval[2].astype(str).map(enToFarsiPandas2)
	data_jadval[3] = data_jadval[3].astype(str).map(enToFarsiPandas2)
	data_jadval[4] = data_jadval[4].astype(str).map(enToFarsiPandas)
	data_jadval[5] = data_jadval[5].astype(str).map(enToFarsiPandas)



	data_jadval = data_jadval.values.tolist()
	labels = ['نام گستره :','وزن گستره از کل :','درصد تحقق یافته :','درصد باقی مانده :','تاریخ بهره برداری برنامه ریزی شده :']

	#sum_of_data = ['کار باقی مانده تجمعی',enToFarsiPandas2(id_ghest),enToFarsiPandas2(handle_month(id_ghest)),add_percentage_sign(jadval_koli['darsad_tahaghogh_yafte']),]
	sum_of_data = [sum_jadval[0],enToFarsiPandas2(id_ghest),enToFarsiPandas2(handle_month(id_ghest)),add_percentage_sign(truncate_str(str(sum_jadval[3]))),sum_jadval[1]]

	html = open_html()
	html = add_div_and_seprator_for_info(html)
	html = add_labels(html , labels)
	html = add_spans(html , jadval_koli.values())


	headers = ['ردیف','شرح','شماره قسط' , 'تاریخ بهره برداری تجاری','درصد مشمول جریمه','مبلغ جریمه','در محاسبات اقساط لحاظ گردد']
	header_contents = ['جرائم تاخیر در بهره برداری' , ' ', handle_month(id_ghest)]
	html = add_header_document(html , header_contents)

	html = add_headers(html , headers)

	page_names = add_content(html , data_jadval)
	pdf_names = add_page_counters(page_names)
	pdf_names = make_pdfs(page_names,options='a4',css_path='temp/style_a4__jaraem_taakhir_dar_bahrebardari.css')
	file_name='jaraem_takhir_dar_bahre_bardari____'+JalaliDatetime.now().strftime('%Y-%m-%d')+'.pdf'
	combine_pdfs(pdf_names,file_name)
	print(file_name)





