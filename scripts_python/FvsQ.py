#! /usr/bin/env python
"""
Graficas de F vs Q con error 
    
"""
from pylab import *

Freq, Q, ErrQ = [], [], []     #crea listas vacias

estaciones=['AGBL','CHAG','COBE','COBN','COBZ','COND','CONV','CURI','CURV','LARO','MINA']

for sta in estaciones:
    r= open('ordenado.txt','rU')
    sompi=r.readlines()            #lee lineas del archivo

    for line in sompi:                  #separa por columnas cada lineas
        if sta in line:
            nfo=line.split(" ")
            print line
            Freq.append(float(nfo[4]))
            Q.append(float(nfo[8]))
            ErrQ.append(float(nfo[9]))

#####grafica con pylab######

    plot(Freq,Q,'o')
    errorbar(Freq,Q, ErrQ, xerr=None, fmt=None, ecolor='blue')
    xlabel('f (Hz)')
    ylabel('Q')
    title(sta, fontsize=26)

    savefig("../graficas/fvsQ"+sta+".png",dpi=80)
    savefig("../graficas/fvsQ"+sta+".pdf",dpi=72)
    show()
    Freq=[]
    Q=[]
    ErrQ=[]