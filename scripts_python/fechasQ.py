#! /usr/bin/env python
"""
    Graficas de fecha contra Q
    
"""
from pylab import *
import datetime

Date, Q, ErrQ = [], [], []     #crea listas vacias

estaciones=['AGBL','CHAG','COBE','COBN','COBZ','COND','CONV','CURI','CURV','LARO','MINA']

for sta in estaciones:
    r= open('ordenadofecha.txt','rU')
    sompi=r.readlines()            #lee lineas del archivo
    
    for line in sompi:                  #separa por columnas cada linea
        if sta in line:
            nfo=line.split(" ")
            print line
            Date.append(nfo[0])
            Q.append(float(nfo[7]))
            ErrQ.append(float(nfo[8]))


    for fec in range(len(Date)):   #transforma strs en objetos datetime
        Date[fec] = datetime.datetime.strptime(Date[fec], '%Y/%m/%d%H:%M:%S')
        
        print fec, Date[fec]


    #####grafica con pylab######
    
    plot_date(Date,Q,'o-')
    errorbar(Date,Q, ErrQ, xerr=None, fmt=None, ecolor='blue')
    xlabel('fecha')
    ylabel('Q')
    title(sta, fontsize=26)
    xticks(rotation=40)
    
    savefig("../graficas/fechaQ"+sta+".png",dpi=80)
#    savefig("../graficas/fecha"+sta+".pdf",dpi=72)
    show()
    Date, Q, ErrQ = [], [], []