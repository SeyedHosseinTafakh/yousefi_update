# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 04:37:44 2020

@author: Hossein
"""



import pandas as pd
import requests
from writers import *
import pdfkit
import numpy as np
from PyPDF2 import PdfFileMerger





URL = 'https://api.daricbot.ir/peymankaran'
r = requests.get(url = URL)
data = r.json()
x = pd.DataFrame(data)
x = x.sort_values(4)
sum_last_row = pd.DataFrame(x)
sum_last_row[3] = sum_last_row[3].astype(float)
sum_last_row[0] = sum_last_row[[0]].applymap(np.int64)
sum_last_row[0] = list(range(1,len(sum_last_row)+1))


