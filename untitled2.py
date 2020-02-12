# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:03:02 2020

@author: hossein
"""

import locale

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

num=[1,3,4,5]

#ar_numbers = [enToArNumb(num) for num in numbers]

#i = 0
#for index , row in sum_last_row_str.iterrows():
    #ar_numbers = [enToArNumb(num) for num in row(index)]
    #print(type(sum_last_row.iloc[index][row].tolist()))
#    for value_of_row in sum_last_row_str.iloc[index].tolist():
        #farsi_number = []
        #for cell in value_in_row:
        #    farsi_number.append(enToArNumb(cell))
        
        #farsi_number    
    #print(sum_last_row.iloc(index))

#x = sum_last_row_str.iloc[index].tolist()
#y = sum_last_row_str.iloc[1][1]

#for x in num:
#    print(x)

#t ='1'

#y = enToArNumb(t)

#sum_last_row_str = sum_last_row.astype(str)


#def test(row):
#    print(n.tolist())
#    for row_data in row.tolist():
#        for cell in 
#    return j


def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1

def enToFarsiPandas(row):
    re_row =[]
    for data in row:
        a_cell = []
        for cell in data:
            a_cell.append(enToArNumb(cell))
        re_row.append(listToString(a_cell))
    return listToString(re_row)
 

def add_commas(number):
    if type(number) == str:
        return number
    else:
        number = '{:,.2f}'.format(number)
        return number

def rv_zeros_af_dot(number):
    return number.split('.')[0]
#y0 = sum_last_row[2].astype(str)
sum_last_row[0] = sum_last_row[0].astype(str).map(enToFarsiPandas)

sum_last_row[3] = sum_last_row[3].map(add_commas).map(rv_zeros_af_dot).map(enToFarsiPandas)
sum_last_row[2] = sum_last_row[2].map(add_commas)
sum_last_row[2] = sum_last_row[2].map(rv_zeros_af_dot).map(enToFarsiPandas)

sum_last_row[4] = sum_last_row[4].astype(str).map(enToFarsiPandas)

sum_last_row[5] = sum_last_row[5].astype(str).map(enToFarsiPandas)
#-------------------------------------
#y1 = sum_last_row[3].map(rv_zeros_af_dot)
#y2 = y1.map(add_commas)

'''
sum_last_row[2] = sum_last_row.applymap(add_commas_0)[2]

print ("Total cost is: ${:,.2f}".format(10000000.100))


add_commas(y2[1])
add_commas(25000000000)
'{:,.2f}'.format(25000000000)


def handle_the_DOT(number):
    number = number.split('.')
    if number[1] >> 0:
        return





TotalAmount = '25000000000'
print ("Total cost is: ${:,.2f}".format(TotalAmount))

locale.setlocale(locale.LC_ALL, '')
locale.currency(123456, symbol=False, grouping=True)

'''

