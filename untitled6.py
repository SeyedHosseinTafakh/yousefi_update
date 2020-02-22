# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:09:09 2020

@author: hossein
"""

options = {
    'page-size': 'A3',
     'margin-top': '0in',
     'margin-right': '0in',
     'margin-bottom': '0in',
     'margin-left': '0in',
     'orientation' : 'landscape',
}
import pdfkit
#config = pdfkit.configuration()

from pyvirtualdisplay import Display
display = Display(visible=0, size=(600,600))
display.start()

#pdfkit.from_file("empty_test.html", 'pdfs/1.pdf', options=options,configuration=config)
from writers import *
combine_pdfs(['dzuf.pdf','qmdb.pdf','hwyz.pdf'],'2.pdf')


print('we did')
