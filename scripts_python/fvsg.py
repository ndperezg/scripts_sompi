#! /usr/bin/env python
"""
    Graficas de f vs g  con error
    
    """
from pylab import *

Freq, Gro, ErrG = [], [], []     #crea listas vacias

estaciones=['AGBL','CHAG','COBE','COBN','COBZ','COND','CONV','CURI','CURV','LARO','MINA']

for sta in estaciones:
    r= open('ordenado.txt','rU')
    sompi=r.readlines()            #lee lineas del archivo
    
    for line in sompi:                  #separa por columnas cada lineas
        if sta in line:
            nfo=line.split(" ")
            print line
            Freq.append(float(nfo[4]))
            Gro.append(float(nfo[6]))
            ErrG.append(float(nfo[7]))
    
    #####grafica con pylab######
    
    plot(Freq,Gro,'o')
    errorbar(Freq,Gro, ErrG, xerr=None, fmt=None, ecolor='blue')
    xlabel('f (Hz)')
    ylabel('g (Hz)')
    title(sta, fontsize=26)
    
    savefig("../graficas/fvsg"+sta+".png",dpi=80)
    savefig("../graficas/fvsg"+sta+".pdf",dpi=72)
    show()
    Freq, Gro, ErrG=[], [], []