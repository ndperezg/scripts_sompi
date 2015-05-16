#! /usr/bin/env python
"""
    Graficas de fecha contra F
    
"""
from pylab import *
import datetime

Date, Freq, ErrFreq = [], [], []     #crea listas vacias

estaciones=['AGBL','CHAG','COBE','COBN','COBZ','COND','CONV','CURI','CURV','LARO','MINA']

for sta in estaciones:
    r= open('ordenadofecha.txt','rU')
    sompi=r.readlines()            #lee lineas del archivo
    
    for line in sompi:                  #separa por columnas cada linea
        if sta in line:
            nfo=line.split(" ")
            print line
            Date.append(nfo[0])
            Freq.append(float(nfo[3]))
            ErrFreq.append(float(nfo[4]))
    
    
    for fec in range(len(Date)):   #transforma strs en objetos datetime
        Date[fec] = datetime.datetime.strptime(Date[fec], '%Y/%m/%d%H:%M:%S')
        
        print fec, Date[fec]
    
    
    #####grafica con pylab######
    
    plot_date(Date,Freq,'o-')
    errorbar(Date,Freq, ErrFreq, xerr=None, fmt=None, ecolor='blue')
    xlabel('fecha', fontsize=12)
    ylabel('F (Hz)')
    title(sta, fontsize=26)
    xticks(rotation=40)
    
    savefig("../graficas/fechaFreq"+sta+".png",dpi=80)
#    savefig("../graficas/frecuencia"+sta+".pdf",dpi=72)
    show()
    Date, Freq, ErrFreq = [], [], []