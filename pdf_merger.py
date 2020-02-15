# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:06:46 2020

@author: hossein
"""

from PyPDF2 import PdfFileMerger
pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfFileMerger()

for pdf in z:
    merger.append(pdf,import_bookmarks=False)



#merger.append(PdfFileReader(file('test.pdf', 'rb')), import_bookmarks=False)



merger.write("result.pdf")
merger.close()



