#! /usr/bin/env python
"""
    Calcula la evolucion temporal de la longitud L de la grieta para una estacion

"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
import sys

Date, X, ErrX, Date1, X1, ErrX1, L, date = [], [], [], [], [], [], [], [] #crea listas vacias

#---- Revisa si hay parametros de entrada
if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

#---Lee parametros de entrada

sta = sys.argv[1]
date_i = sys.argv[2]
date_f = sys.argv[3]

#--- Prepara los datos
#os.system("./ordena_awk")


r= open('resultado_todo.txt','rU')
sompi=r.readlines()            #lee lineas del archivo

for line in sompi: #separa por columnas cada linea
    if sta in line:
        nfo=line.split(" ")
        print line
        Date.append(nfo[0])
        X.append(float(nfo[3]))
        ErrX.append(float(nfo[4]))
for fec in range(len(Date)):   #transforma strs en objetos datetime
    Date[fec] = datetime.datetime.strptime(Date[fec], '%Y/%m/%d%H:%M:%S')
    
print fec, Date[fec]
Date= sorted(Date)

#---Arregla fechas

date_i = datetime.datetime.strptime(date_i, '%Y%m%d')
date_f = datetime.datetime.strptime(date_f, '%Y%m%d')

for i in range(len(Date)):
    if date_i <= Date[i] <= date_f:
        X1.append(X[i])
        ErrX1.append(ErrX[i])
        Date1.append(Date[i])

epsilon = 0.1129

####Calcula la longitud L####
def longitud(f):
    a = 800
    C = 3*10e4*(1/120)*(1/5)*(1/5)
    B= 2*f*np.power(1+epsilon*C, 0.5)
    return(a/B)

X1= np.array(X1)

for j in range(len(X1)):
    if  X[j] > 8.0:
         L.append(longitud(X1[j]))
         date.append(Date1[j])


####Hace la grafica#####



fecha_1 = datetime.datetime.strptime('20100101', '%Y%m%d')
fecha_2 = datetime.datetime.strptime('20110101', '%Y%m%d')
fecha_3 = datetime.datetime.strptime('20020901', '%Y%m%d')
fecha_4 = datetime.datetime.strptime('20021231', '%Y%m%d')

fig = plt.figure(figsize=(15,6))
plt.plot(date, L, 'o--',color= 'b', markersize=10)
#plt.errorbar(Date,X1, ErrX1, xerr=None, fmt=None, ecolor='k')
#plt.axvspan(fecha_1,fecha_2, alpha=0.3)
#plt.axvspan(fecha_3,fecha_4, alpha=0.3)
#plt.xlabel('fecha',fontsize=20)


plt.ylabel('L (m)',fontsize=20)
plt.title(sta+"  $\epsilon=$"+str(epsilon)+"  f > 8 Hz", fontsize=26)
plt.xticks(rotation=30)
plt.xlim((date_i, date_f))
plt.grid(True)
plt.show()

print  len(X1), max(X1), min(X1), np.mean(X1), np.std(X1)

guardar = raw_input('Desea guardar la imagen?\n')
if guardar == 's':
    fig.savefig("../graficas/periodos_especificos/"+sta+"_L1_"+sys.argv[2]+"-"+sys.argv[3]+".png",format='png',dpi=300)
else:
    sys.exit()
