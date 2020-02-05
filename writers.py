# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:25:36 2020

@author: hossein
"""

import codecs

def open_html(file = 'default_html_template.html'):
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
    file = codecs.open(file_name,'w','utf-8')
    file.write(html_file)
    file.close()

def add_content(html , contents):
    contents_data = "<tr>\n"
    for list_contents in contents:
        a_row_list = '<tr>\n'
        for list_entety in list_contents:
            
            a_row_list = a_row_list + "<td><span>"+str(list_entety)+ "</span></td>\n"
        a_row_list= a_row_list + "</tr>\n"
        contents_data = contents_data + a_row_list
    html = html.split('<tbody>')
    html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
    return html
    
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



#html_data = open_html()
#headers = ['ردیف','جمع ریالی','جمع ارزی','مبلغ ورق','جمع دلاری ساخت و پوشش','ضخامت','متراژ','تناژ','تاریخ تحویل','نوع کالای تحویلی','شماره حواله انبار','شماره تقاضا','شماره قلم','نرخ تسعیر بانک مرکزی','هزینه انبارداری','هزینه صدور بیمه نامه','عوارض گمرکی','هزینه ساخت لوله','هزینه پوشش','مالیات ارزش افزوده و سایر خدمات (ورق)','مالیات ارزش افزوده و سایر خدمات (ساخت و پوشش)']
#html_data = add_headers(html_data , headers)
#data = [[1,2],[3,4],[5,6]]
#html_data = add_content(html_data , data)

#write_html_file('shandool2.html',html_data)




#-------------------------------------------------------------------
html_data = open_html()
headers = ['ردیف','جمع ریالی','جمع ارزی','مبلغ ورق','جمع دلاری ساخت و پوشش','ضخامت','متراژ','تناژ','تاریخ تحویل','نوع کالای تحویلی','شماره حواله انبار','شماره تقاضا','شماره قلم','نرخ تسعیر بانک مرکزی','هزینه انبارداری','هزینه صدور بیمه نامه','عوارض گمرکی','هزینه ساخت لوله','هزینه پوشش','مالیات ارزش افزوده و سایر خدمات (ورق)','مالیات ارزش افزوده و سایر خدمات (ساخت و پوشش)']

header_contents = ['گزارش تراز مالی-لوله های 56(نتایج)', 'قسط شماره یکم آذر ماه 1396' , 'گذارش گیری در تاریخ: بهمن 1398']
html_data = add_header_document(html_data , header_contents)

html_data = add_headers(html_data , headers)
html_data = add_content(html_data , output2)


write_html_file('shandool2.html',html_data)




