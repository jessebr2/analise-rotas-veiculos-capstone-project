import pandas as pd
import numpy as np

try:
    data_csv = pd.read_csv("veiculosrestricao12e13out_count.csv", sep='\t')
    print "Base de dados contem {} passagens com {} caracteristicas cada.".format(*data_csv.shape)
except:
    print "Dataset could not be loaded. Is the dataset missing??"

try:
    data_csv.drop(data_csv.loc_latitude == 0, inplace=True)
    print "latide zero dropado com sucesso"
except:
    print "falha ao dropar latitude zero"

print data_csv.shape
print data_csv.loc[0:5]

bloco=int(data_csv.shape[0]/10)

placa_column = 'placa' #### PREENCHER COM O NOME DA COLUNA DA PLACA
latitude_column = 'loc_latitude'
longitude_column = 'loc_longitude'

for i in range(10): #tratamento da placa
    inicio = i*bloco
    fim = inicio+bloco
    placas_exploded = data_csv.loc[inicio:fim][placa_column].apply(lambda x: pd.Series(list(x)))
    data_csv.loc[inicio:fim][placa_column] = placas_exploded[0].map(str) + placas_exploded[2] + placas_exploded[1] + placas_exploded[6] + placas_exploded[4] + placas_exploded[5] + placas_exploded[3]


for i in range(10): #tratamento da latitude
    inicio = i*bloco
    fim = inicio+bloco
    num = data_csv.loc[inicio:fim][latitude_column].apply(lambda x: x*-2000000)
    data_csv.loc[inicio:fim][latitude_column] = num.mod(10000)
    
for i in range(10): #tratamento da longitude
    inicio = i*bloco
    fim = inicio+bloco
    num = data_csv.loc[inicio:fim][longitude_column].apply(lambda x: x*-1000000)
    data_csv.loc[inicio:fim][longitude_column] = num.mod(10000)


data_csv[latitude_column] = data_csv[latitude_column].astype(int)
data_csv[longitude_column] = data_csv[longitude_column].astype(int)

print data_csv.shape
print data_csv.loc[0:5]
try:
    data_csv.to_csv('veiculosrestricao12e13out_trans.csv')
    print "arquivo salvo com sucesso"
except:
    print "erro ao salvar arquivo"