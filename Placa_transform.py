import pandas as pd

try:
    data_csv = pd.read_csv("veiculosgeral14e15set.csv", sep='\t')
    print "Base de dados contém {} passagens com {} características cada.".format(*data_csv.shape)
except:
    print "Dataset could not be loaded. Is the dataset missing??"

try:
    data_csv.drop(data_csv.loc_latitude == 0)
    print "latide zero dropado com sucesso"
except:
    print "falha ao dropar latitude zero"

print data_csv.columns
    
placas_exploded = data_csv['loc_placa'].apply(lambda x: pd.Series(list(x)))
num = pd.DataFrame()
num = placas_exploded[3].map(str) + placas_exploded[4] + placas_exploded[5] + placas_exploded[6]
numeric = pd.to_numeric(num, errors='coerce')
numeric = numeric.mul(numeric).add(1000)
numeric_trans = numeric.mod(10000)
placas = pd.DataFrame({'orig' : num, 'trans':numeric_trans})
data_csv['loc_placa'] = placas_exploded[0].map(str) + placas_exploded[1] + placas_exploded[2] + numeric_trans.map(str)
#data_csv.rename(index=str, columns={"loc_placa": "placa", "loc_latitude": "latitude", "loc_longitude": "longitude"})

try:
    data_csv.to_csv('veiculoscomplacatransformada.csv')
    print "arquivo salvo com sucesso"
except:
    print "erro ao salvar arquivo"