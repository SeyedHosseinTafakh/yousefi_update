
import pandas as pd
import requests 

URL = 'https://api.daricbot.ir/pipeLinesF'


r = requests.get(url = URL) 
data = dict(r.json())

test = []

for i in data.keys():
    test.append(data[str(i)]['dataBase'])

x = pd.DataFrame(test)



x = x.sort_values(4)


data['0']

for index,value in x[0].items():
    data[index] = data[str(index)]
    del(data[str(index)])

for key in data.keys():
    print(data[key])
    break

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

i = 0
output = []

for data_point in data:
    x = []
    x.append(i)
    x.append(truncate(data[data_point]['motalebat_riyali'],2))
    x.append(0)
    x.append(truncate(data[data_point]['mablaghe_varagh'],2))
    x.append(truncate(data[data_point]['arzi_sakht_va_pooshesh'],2))
    x.append(truncate(float(data[data_point]['dataBase'][1]),2))#5
    x.append(float(data[data_point]['dataBase'][2]))
    x.append(truncate(float(data[data_point]['dataBase'][3]),2))
    x.append(data[data_point]['dataBase'][4])
    x.append(data[data_point]['dataBase'][5])
    x.append(data[data_point]['dataBase'][6])
    x.append(data[data_point]['dataBase'][7])
    x.append(data[data_point]['dataBase'][8])
    x.append(data[data_point]['dataBase'][9])
    x.append(data[data_point]['dataBase'][10])
    x.append(data[data_point]['dataBase'][11])
    x.append(truncate(data[data_point]['avarez_gomrok'],2))
    x.append(truncate(data[data_point]['hazine_sakhte_loole'],2))
    x.append(truncate(data[data_point]['hazine_pooshesh'],2))
    x.append(truncate(data[data_point]['maliyat_bar_arzesh_varagh'],2))
    x.append(truncate(data[data_point]['maliyat_bara_arzesh_afzoode_sakhte_pooshesh'],2))
    output.append(x)
    i +=1


del(data_point)
del(i)
del(index)
del(key)
del(data)
del(test)
del(value)
del(x)

sum_last_row = pd.DataFrame(output,dtype='float64')
sum_last_row = sum_last_row.append(pd.Series() , ignore_index=True)
len_od_df = len(sum_last_row)-1
sum_last_row.loc[len_od_df,1] = truncate(sum_last_row[1].sum())
sum_last_row.loc[len_od_df,2] = truncate(sum_last_row[2].sum())
sum_last_row.loc[len_od_df,3] = truncate(sum_last_row[3].sum())
sum_last_row.loc[len_od_df,4] = truncate(sum_last_row[4].sum())
sum_last_row.loc[len_od_df,5] = truncate(sum_last_row[5].sum())
sum_last_row.loc[len_od_df,6] = truncate(sum_last_row[6].sum(skipna=True))
sum_last_row.loc[len_od_df,7] = truncate(sum_last_row[7].sum(skipna=True))

sum_last_row.loc[len_od_df,16] = truncate(sum_last_row[16].sum(skipna=True))
sum_last_row.loc[len_od_df,17] = truncate(sum_last_row[17].sum())



output2 = sum_last_row.values.tolist()





