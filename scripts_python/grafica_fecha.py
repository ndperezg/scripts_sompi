#! /usr/bin/env python
"""
    Hace graficas por fecha de Q o de F para una estacion
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
import sys

Date, X, ErrX = [], [], [] #crea listas vacias

#---- Revisa si hay parametros de entrada
if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

#---Lee parametros de entrada

sta = sys.argv[1]
var = sys.argv[2]
date_i = sys.argv[3]
date_f = sys.argv[4]

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
    if sta in line:
        nfo=line.split(" ")
        print line
        Date.append(nfo[0])
        X.append(float(nfo[a]))
        ErrX.append(float(nfo[b]))
for fec in range(len(Date)):   #transforma strs en objetos datetime
    Date[fec] = datetime.datetime.strptime(Date[fec], '%Y/%m/%d%H:%M:%S')
    
    print fec, Date[fec]
Date= sorted(Date)

#---Arregla fechas

date_i = datetime.datetime.strptime(date_i, '%Y%m%d')
date_f = datetime.datetime.strptime(date_f, '%Y%m%d')



####Hace la grafica#####

if var=='Q':
    col= "green"
else:
    col= "red"

fecha_1 = datetime.datetime.strptime('20100101', '%Y%m%d')
fecha_2 = datetime.datetime.strptime('20110101', '%Y%m%d')
fecha_3 = datetime.datetime.strptime('20020901', '%Y%m%d')
fecha_4 = datetime.datetime.strptime('20021231', '%Y%m%d')

fig = plt.figure(figsize=(15,6))
plt.plot(Date, X, 'o-',color= col, markersize=10)
plt.errorbar(Date,X, ErrX, xerr=None, fmt=None, ecolor=col)
#plt.axvspan(fecha_1,fecha_2, alpha=0.3)
#plt.axvspan(fecha_3,fecha_4, alpha=0.3)
#plt.xlabel('fecha',fontsize=20)

if var == 'F':
    plt.ylabel('f (Hz)',fontsize=20)
else:
    plt.ylabel(var,fontsize=20)
plt.title(sta, fontsize=26)
plt.xticks(rotation=30)
plt.xlim((date_i, date_f))
plt.grid(True)
plt.show()

print  len(X), max(X), min(X), np.mean(X), np.std(X)

guardar = raw_input('Desea guardar la imagen?\n')
if guardar == 's':
	fig.savefig("../graficas/periodos_especificos/"+sta+"_"+var+"_"+sys.argv[3]+"-"+sys.argv[4]+".png",format='png',dpi=300)
else:
	sys.exit()
