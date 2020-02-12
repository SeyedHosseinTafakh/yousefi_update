# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:50:28 2020

@author: hossein
"""

contents = output2
html_original = open_html()
#------------------------

contents_data = ""
i = 0
pages = []
for list_contents in contents:
    print(i)
    if i ==22 and len(pages) == 0:
        
        html = html_original.split('<tbody>')
        html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
        pages.append(str(i)+'.html')
        print(pages)
        write_html_file(str(i)+'.html' , html)
        contents_data = ""
        i = 0
        continue
    if i ==25 and len(pages) != 0:
        html = html_original.split('<tbody>')
        html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
        pages.append(str(i)+'.html')
        print(pages)

        write_html_file(str(i)+'.html' , html)
        contents_data = ""
        i = 0
        continue
            
    a_row_list = '<tr>\n'
    for list_entety in list_contents:
        
        a_row_list = a_row_list + "<td><span>"+str(list_entety)+ "</span></td>\n"
    a_row_list= a_row_list + "</tr>\n"
    contents_data = contents_data + a_row_list
    i +=1
html = html_original.split('<tbody>')
html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]
pages.append(str(i)+'.html')

write_html_file(str(i)+'.html' , html)
contents_data = ""
html = html_original.split('<tbody>')
html = html[0]+"<tbody>\n" +contents_data + "</tbody>\n" + html[1]























