#! /usr/bin/env python
"""
    Hace graficas por fecha de Q o de F para dos estaciones estaciones
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
import sys

Date1, Date2, X1, ErrX1, X2, ErrX2  = [], [], [], [], [], [] #crea listas vacias

#---- Revisa si hay parametros de entrada
if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

#---Lee parametros de entrada

sta1 = sys.argv[1]
sta2 = sys.argv[2]
var = sys.argv[3]
date_i = sys.argv[4]
date_f = sys.argv[5]

#--- Prepara los datos
#os.system("./ordena_awk")

if var == 'F':
    a, b = 3 , 4
elif var == 'Q':
    a, b = 7, 8
else:
    print 'error'
    sys.exit()

r= open('resultado_todo.txt','rU')
sompi=r.readlines()            #lee lineas del archivo

for line in sompi:                  #separa por columnas cada linea
    if sta1 in line:
        nfo=line.split(" ")
        print line
        Date1.append(nfo[0])
        X1.append(float(nfo[a]))
        ErrX1.append(float(nfo[b]))
    if sta2 in line:
        nfo=line.split(" ")
        print line
        Date2.append(nfo[0])
        X2.append(float(nfo[a]))
        ErrX2.append(float(nfo[b]))

for fec in range(len(Date1)):   #transforma strs en objetos datetime
    Date1[fec] = datetime.datetime.strptime(Date1[fec], '%Y/%m/%d%H:%M:%S')


for fec in range(len(Date2)):
    Date2[fec] = datetime.datetime.strptime(Date2[fec], '%Y/%m/%d%H:%M:%S')

Date1= sorted(Date1)
Date2= sorted(Date2)

#---Arregla fechas

date_i = datetime.datetime.strptime(date_i, '%Y%m%d')
date_f = datetime.datetime.strptime(date_f, '%Y%m%d')



####Hace la grafica#####

if var=='Q':
    col1= "darkgreen"
    col2= "lime"
else:
    col1= "red"
    col2= "aqua"

fecha_1 = datetime.datetime.strptime('20100101', '%Y%m%d')
fecha_2 = datetime.datetime.strptime('20110101', '%Y%m%d')
fecha_3 = datetime.datetime.strptime('20020901', '%Y%m%d')
fecha_4 = datetime.datetime.strptime('20021231', '%Y%m%d')

fig, ax = plt.subplots(figsize=(15,6))
plt.plot(Date1, X1, 'o-',color= col1, markersize=10, label=sta1)
plt.errorbar(Date1,X1, ErrX1, xerr=None, fmt=None, ecolor=col1)
plt.plot(Date2, X2, 'o-',color= col2, markersize=10, label=sta2)
plt.errorbar(Date2,X2, ErrX2, xerr=None, fmt=None, ecolor=col2)
#plt.axvspan(fecha_1,fecha_2, alpha=0.3)
#plt.axvspan(fecha_3,fecha_4, alpha=0.3)
#plt.xlabel('fecha',fontsize=20)

if var == 'F':
    plt.ylabel('f (Hz)',fontsize=20)
else:
    plt.ylabel(var,fontsize=20)
#plt.title(sta, fontsize=26)
plt.xticks(rotation=25)
plt.xlim((date_i, date_f))
plt.legend(loc=2)
plt.grid(True)
plt.show()

print  len(X1), max(X1), min(X1), np.mean(X1), np.std(X1)

guardar = raw_input('Desea guardar la imagen?\n')
if guardar == 's':
    fig.savefig("../graficas/periodos_especificos/"+sta1+"_"+sta2+"_"+var+"_"+sys.argv[4]+"-"+sys.argv[5]+".png",format='png',dpi=300)
else:
    sys.exit()
