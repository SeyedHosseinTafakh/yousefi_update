# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:48:02 2020

@author: hossein
"""

from PyPDF2 import PdfFileMerger

pdfs = ['sample.pdf', 'out.pdf']
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf,import_bookmarks=False)

merger.write("mergeed.pdf")
merger.close()



