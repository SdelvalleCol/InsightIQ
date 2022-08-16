import matplotlib.pyplot as mp
import csv

def converter(x):
    for i in range(len(x)):
        x[i] = float(x[i])

def histograma(x):
    mp.hist(x)
    mp.title('Histograma')
    mp.xlabel("Valor de datos")
    mp.ylabel("Cantidad de datos")
    mp.show()

def bloxplot(x):
    mp.boxplot(x)
    mp.title('Caja y Bigotes')
    mp.xlabel("Valor de datos")
    mp.ylabel("Cantidad de datos")
    mp.show()

data= []
sub_data = []
with open ("abalone.csv") as f:
    reader = csv.reader(f)
    for x in reader:
        data.append(x)
    for j in range(len(data[0])-1):
        columna = [fila[j+1] for fila in data]
        converter(columna)
        sub_data.append(columna)  