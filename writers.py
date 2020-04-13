# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:25:36 2020

@author: hossein
"""
from PyPDF2 import PdfFileMerger
import codecs
import random
import string
import os
import pdfkit
import pathlib
from os import path as path_os
from PyPDF2 import PdfFileMerger
from pyvirtualdisplay import Display
from datetime import timedelta
from khayyam import JalaliDate, JalaliDatetime
import datetime
import calendar
import pandas as pd
import platform

from khayyam import *
from datetime import date
JalaliDatetime(989, 3, 25, 10, 43, 23, 345453)

#repository
#df.append(pandas.Series(), ignore_index=True)


#dont touch

if platform.system() =='Linux':
    #---------------------------linux-------------------------------
    display = Display(visible=0, size=(800,600))
    display.start()
    config = pdfkit.configuration()
else:
    #---------------------------windows-------------------------------
    path_wkhtmltopdf = r'wkhtmltox\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#options = {
#    'page-size': 'A3',
#     'margin-top': '0in',
#     'margin-right': '0in',
#     'margin-bottom': '0in',
#     'margin-left': '0in',
#     'orientation' : 'landscape',
#}
#options = {
#    'page-size': 'A4',
#     'margin-top': '0in',
#     'margin-right': '0in',
#     'margin-bottom': '0in',
#     'margin-left': '0in',
#       landscape
#     'orientation' : 'portrait ',
#}


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def open_html(file = 'default_html_template.html'):
    path = pathlib.Path().absolute().__str__()
    file = path + '/' + file
    html = codecs.open(file , 'r','utf-8')
    html_content = html.read()
    html.close()
    return html_content


def add_headers(html,headers):
    html_half = html.split('<thead>')
    ready_headers = '<tr>\n'
    for header in headers:
        ready_headers = ready_headers + "<th scope='col'><span>" + header +"</span></th>\n"
    ready_headers = ready_headers + "</tr>"
    html_half = html_half[0] + "<thead>\n" + ready_headers + html_half[1]
    return html_half

def write_html_file(file_name , html_file):
    path = pathlib.Path().absolute().__str__()
    print(path)
    file = codecs.open(path+'/temp/'+file_name,'w','utf-8')
    file.write(html_file)
    file.close()

def add_content(html_original , contents , first_page_row_numbers=22,second_page_numbers=22):
    contents_data = ""
    i = 0
    pages = []
    for list_contents in contents:
        a_row_list = '<tr>\n'
        for list_entety in list_contents:
            
            a_row_list = a_row_list + "<td><span>"+str(list_entety)+ "</span></td>\n"
        a_row_list= a_row_list + "</tr>\n"
        contents_data = contents_data + a_row_list
        if i ==first_page_row_numbers :
            
            html = html_original.split('<tbody>')
            html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
            page_name = randomString(4)+'.html'
            pages.append(page_name)
            write_html_file(page_name , html)
            contents_data = ""
            i = 0
            first_page_row_numbers = second_page_numbers
            continue
        '''if i ==25 and len(pages) != 0:
            html = html_original.split('<tbody>')
            html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
            pages.append(str(i)+'.html')
            print(pages)
    
            write_html_file(str(i)+'.html' , html)
            contents_data = ""
            i = 0
            continue'''
                
        
        i +=1
    html = html_original.split('<tbody>')
    html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
    page_name = randomString(4)+'.html'
    pages.append(page_name)
    
    write_html_file(page_name , html)
    contents_data = ""
    html = html_original.split('<tbody>')
    html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
    return pages
    
def add_header_document(html , contents):
    contents_data = '<div style="padding-top: 1px;"></div>\n'
    contents_data += '<div align="center" class="col-container">\n'
    contents_data += '  <div class="col" style="text-align: right;">\n'
    contents_data += '<h2>' + contents[0] + '</h2> \n'
    contents_data += '  </div>\n'
    contents_data += '  <div class="col" style="text-align: center;"> \n'
    contents_data +='<h2>' + contents[1] + '</h2> \n'
    contents_data += '  </div>\n'
    contents_data += '  <div class="col" style="text-align: left;"> \n'
    contents_data +='<h2>' + contents[2] + '</h2> \n'
    contents_data += '  </div> \n</div>\n'
    html = html.split('<body>')
    html[0] += '<body>'
    html = html[0] + contents_data +html[1]
    return html

def add_page_counters(pages,numbers = [],pusher=0,slider=''):
    #path = pathlib.Path().absolute().__str__()
    x = []
    if len(numbers) ==0:
        numbers = range(1,len(pages)+1)
    for number , page in zip(numbers , pages):
        html = open_html('temp/'+page)
        html = html.replace('page_counter',enToFarsiPandas(str(number+pusher)+slider))
        write_html_file(page , html)
        x.append(page)
    return x

def combine_pdfs(pdfs,result_name,ghest_number,tarikh,onvan):
    print('i dont fucking know')
    path = pathlib.Path().absolute().__str__()
    merger = PdfFileMerger()
    for pdf in pdfs:
        pdf = pdf
        
        merger.append(open(pdf,'rb'),import_bookmarks=False)
    merger.write(path+'/pdfs/'+result_name)
    merger.close()
    csv_data=[]    
    csv_data.append(tarikh)
    csv_data.append(ghest_number)
    csv_data.append(onvan)
    csv_data.append(result_name)
    csv = pd.DataFrame(csv_data).T
    csv.columns=range(0,4)
    csv_old = pd.read_csv('data.csv')
    csv_old.columns=range(0,4)
    csv_old = pd.concat([csv_old,csv],axis=0)
    csv_old.to_csv('data.csv',index=False)
    print(csv_old)
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1





def add_commas(number):
    if type(number) == str:
        return number
    else:
        number = '{:,.2f}'.format(number)
        return number


def rv_zeros_af_dot(number):
    return number.split('.')[0]

def enToArNumb(number):
    dic = {
        '0':'۰',
        '1':'١',
        '2':'٢',
        '3':'۳',
        '4':'۴',
        '5':'۵',
        '6':'۶',
        '7':'۷',
        '8':'۸',
        '9':'۹',
    }
    if number in dic:
        return dic.get(number)
    return number



def make_pdfs(page_names,options,css_path='temp/style.css'):
    css = [css_path]
   


    if options =='a4':
        options = {'page-size': 'A4',
                   'margin-top': '0in',
                   'margin-right': '0in',
                   'margin-bottom': '0in',
                   'margin-left': '0in',
                   'orientation' : 'portrait',
                   } 
    else:
        options = {
                   'page-size': 'A3',
                   'margin-top': '0in',
                   'margin-right': '0in',
                   'margin-bottom': '0in',
                   'margin-left': '0in',
                   'orientation' : 'landscape',}
    pdfs = []
    for page in page_names:
        path = pathlib.Path().absolute().__str__()
        pdf_name = page.split('.html')[0] + '.pdf'
#        print('1')
        page_str = open_html('temp/'+page)
#        print('2')
        
#        print('3')
        pdfkit.from_string(page_str , pdf_name , css= css,options=options,configuration=config)
#        print('4')
        #css = ['temp/style.css']
        #pdfkit.from_file('temp/'+page , pdf_name,configuration=config , options=options,css=css)
        pdfs.append(pdf_name)
        #display.popen.terminate()
#        print('5')
    return pdfs


def truncate_str(data_org):
    data = data_org.split('.')
    if len(data) == 2 :
        y = ''
        data = data[0] +'.'+ y.join(list(data[1])[0:2])
        return data
    return data_org




def enToFarsiPandas(row):
    re_row = []
    for data in row:
        a_cell = []
        for cell in data:
            a_cell.append(enToArNumb(cell))
        re_row.append(listToString(a_cell))
    return listToString(re_row)

def enToFarsiPandas2(data):
    cell_list = []
    data = data.replace('-','space')
    for cell in data:
        cell_list.append(enToArNumb(cell))
    data = ''
    for n in cell_list:
        data +=n
    data = data.replace('space','/')
    return data


def add_div_and_seprator_for_info(html):
    data = '<div class="seprator"></div> \n <div class="info_background">  \n<!-- label_place_holder --> \n <!-- span_place_holder -->\n </div>'
    if html.find('<!-- div_container_and_seprator_place_holder -->') >=0:
        html = html.replace('<!-- div_container_and_seprator_place_holder -->' , data)
        return html
    return html
def add_labels(html, labels):
    data = ['<div class="labels">\n']
    for label in labels:
        data.append('<h4 style="text-align: left">'+label+'</h4> \n')
    data = listToString(data)
    data += '</div>'
    html = html.replace('<!-- label_place_holder -->',data)
    return html

def add_spans(html , spans):
    data = ['<div class="spans">\n']
    for span in spans:
        data.append('<h5 style=" direction: ltr;">'+span+'</h5> \n')
    data= listToString(data)
    data +='</div>'
    html = html.replace('<!-- span_place_holder -->',data)
    return html

def add_percentage_sign(data):
    if type(data) == str:
        data = data+ ' %'
    return data


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def handle_month(number):
    month_center = 4
    to_month = int(number) - month_center
    time = JalaliDatetime(1396, 12, 17)
    time = add_months(time , to_month)
    time = [str(time.year) , str(time.month) , '17']
    return time[0]+'-'+time[1]+'-'+time[2]



def add_check_mark(data):
    if data=='1':
        return '<p>&#10004;</p>'
    if data=='0':
        return '<p>&#10006;</p>'
    return data
def check_file(file_name):
    path = pathlib.Path().absolute().__str__()
    if path_os.exists(path + '\\'+file_name):
        return True
    return False

def deleter(file_name):
    if check_file(file_name):
        os.remove(file_name)
        
        


def change_gostare_id_to_name(data):
    x = {'1':'گستره اهواز خرمشهر و شملچه و ایستگاه کنترل فشار خرمشهر و ایستگاه اندازه گیری شلمچه',
         '2':' گستره کوهدشت چارمله و ایستگاه کنترل فشار کوهدشت و مخابرات ',     
         '3':'گستره کوهدشت بیستون و ایستگاه کنترل فشار دهگلان',     
         '4':'گستره دزفول کوهدشت و ایستگاه کنترل فشار دزفول',       
'5':'گستره بیستون کرمانشاه (34 کیلومتر) و ایستگاه کنترل فشار بیستون',       
'6':'تاسیسات تقویت فشار اهواز',     
'7':'تاسیسات تقویت فشار حسینیه',        
'8':'تاسیسات تقویت فشار کوهدشت',        
'9':'تاسیسات تقویت فشار دیلم',      
'10':'تاسیسات تقویت فشار بیدبلند',      
         }
    if data in x:
        return x[data]
    return data

        
