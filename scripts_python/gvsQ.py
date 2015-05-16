#! /usr/bin/env python
"""
    Graficas de g vs Q con error
    
    """
from pylab import *

Gro, Q, ErrQ = [], [], []     #crea listas vacias

estaciones=['AGBL','CHAG','COBE','COBN','COBZ','COND','CONV','CURI','CURV','LARO','MINA']

for sta in estaciones:
    r= open('ordenado.txt','rU')
    sompi=r.readlines()            #lee lineas del archivo
    
    for line in sompi:                  #separa por columnas cada linea
        if sta in line:
            nfo=line.split(" ")
            print line
            Gro.append(float(nfo[6]))
            Q.append(float(nfo[8]))
            ErrQ.append(float(nfo[9]))
    
    #####grafica con pylab######
    
    plot(Gro,Q,'go')
    errorbar(Gro,Q, ErrQ, xerr=None, fmt=None, ecolor='green')
    xlabel('g (Hz)')
    ylabel('Q')
    title(sta, fontsize=26)
    
    savefig("../graficas/gvsQ"+sta+".png",dpi=80)
    savefig("../graficas/gvsQ"+sta+".pdf",dpi=72)
    show()
    Gro, Q, ErrQ=[], [], []