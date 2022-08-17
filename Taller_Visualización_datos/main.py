from asyncio.windows_events import NULL
from tkinter import Tk, ttk
import matplotlib.pyplot as mp
import csv
import tkinter
import numpy
import scipy
from tkinter import *

data= []
sub_data = []
sub_data_limpio = []
def inicio(p,y,z):
    with open ("abalone.csv") as f:
        reader = csv.reader(f)
        for x in reader:
            p.append(x)
        for j in range(len(data[0])-1):
            clear_data = []
            columna = [fila[j+1] for fila in p]
            converter(columna)
            superior = numpy.quantile(columna,.75)
            inferior = numpy.quantile(columna,.25)
            iqr = superior -inferior
            limite_inferior = inferior - 1.5 * iqr
            limite_superior = superior + 1.5 * iqr
            for n in columna:
                if(n > limite_inferior and n < limite_superior):
                    clear_data.append(n)
            z.append(clear_data)
            y.append(columna)
            

def converter(x):
    for i in range(len(x)):
        x[i] = float(x[i])

def indice(op,y):
    return op.index(y)

def histograma(x):
    if opcion.get():
        dataz = sub_data[x]
    else:
        dataz = sub_data_limpio[x]
    mp.hist(dataz)
    mp.title('Histograma')
    mp.xlabel("Valor de datos")
    mp.ylabel("Cantidad de datos")
    mp.show()

def bloxplot(x):
    if opcion.get():
        dataz = sub_data[x]
    else:
        dataz = sub_data_limpio[x]
    mp.boxplot(dataz)
    mp.title('Caja y Bigotes')
    mp.xlabel("Valor de datos")
    mp.ylabel("Cantidad de datos")
    mp.show()

def normal(x):
    if opcion.get():
        dataz = sub_data[x]
    else:
        dataz = sub_data_limpio[x]
    mp.plot(dataz)
    mp.title('Normal')
    mp.xlabel("Valor de datos")
    mp.ylabel("Cantidad de datos")
    mp.show()
    

def scatter(x,y):
    if opcion.get():
        dataz = sub_data[x]
        datay = sub_data[y]
    else:
        dataz = sub_data_limpio[x]
        datay = sub_data_limpio[y]
    mp.scatter(dataz,datay)
    mp.title("Scatter")
    mp.show()

def probability(x):
    if opcion.get():
        dataz = sub_data[x]
    else:
        dataz = sub_data_limpio[x]
    fig = mp.figure()
    ax = fig.add_subplot(111)
    scipy.stats.probplot(dataz, dist=scipy.stats.norm,plot=ax)
    mp.show()

def ver():
    if(opcion.get()):
        print("SIU")
    else:
        print("NOUSS")
    
inicio(data,sub_data,sub_data_limpio)
ventana = tkinter.Tk()
ventana.title("IA")
ventana.geometry("640x480")
etiqueta = tkinter.Label(ventana,text="IA").place(x=320,y=20)
etiqueta = tkinter.Label(ventana,text="Gráficos").place(x=50,y=80)
etiqueta = tkinter.Label(ventana,text="Comparaciones").place(x=50,y=250)
separator = ttk.Separator(ventana, orient='horizontal')
separator.pack(fill='x')
list_1 = ttk.Combobox(ventana,width=17,state="readonly")
list_1.place(x=280,y=80)
opciones = [
    "Length",
    "Diameter",
    "Height",
    "Whole-weight",
    "Shucked-weight",
    "Viscera-weight",
    "Shell-weight",
    "Rings"
]
list_1['values'] = opciones

list_2 = ttk.Combobox(ventana,width=13,state="readonly")
list_2.place(x=300,y=250)
opciones_2 = [
    "Length",
    "Diameter",
    "Height",
    "Whole-weight",
    "Shucked-weight",
    "Viscera-weight",
    "Shell-weight",
    "Rings"
]
list_2['values'] = opciones_2

list_3 = ttk.Combobox(ventana,width=13,state="readonly")
list_3.place(x=175,y=250)
opciones_3 = [
    "Length",
    "Diameter",
    "Height",
    "Whole-weight",
    "Shucked-weight",
    "Viscera-weight",
    "Shell-weight",
    "Rings"
]
list_3['values'] = opciones_3

boton_1 = tkinter.Button(ventana,text="Histograma",command= lambda: histograma(indice(opciones,list_1.get())))
boton_1.place(x=480,y=80)

boton_2 = tkinter.Button(ventana,text="Boxplot",command= lambda: bloxplot(indice(opciones,list_1.get())))
boton_2.place(x=480,y=120)

boton_4 = tkinter.Button(ventana,text="Normal",command= lambda: probability(indice(opciones,list_1.get())))
boton_4.place(x=480,y=160)

boton_5 = tkinter.Button(ventana,text="Scatter",command= lambda: scatter(indice(opciones,list_2.get()),indice(opciones,list_3.get())))
boton_5.place(x=480,y=250)

opcion = IntVar() # Como StrinVar pero en entero
atipico = Checkbutton(ventana, text="atipico", variable=opcion, onvalue=1, offvalue=0 , command= lambda: ver()).place(x=360,y=80)

ventana.mainloop()