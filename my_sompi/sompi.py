#!/usr/bin/env python
"""
    Algoritmo basico para el metodo sompi
    basado en Kumazawa 1989
    
"""
import os
import sys
import numpy as np

#-- revisa si hay archivo de entrada
if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

#---lee parametros de entrada

sismograma = sys.argv[1]
mmin = int(sys.argv[2])
mmax = int(sys.argv[3])

x, Head = [], []

r=open(sismograma,'rU')
for i, linea in enumerate(r):
    if i < 5:
        print linea
        Head.append(linea)
    else:
        x.append(float(linea))

X = np.array(x)
N = len(X)

for m in np.arange(mmin,mmax):
    c = 1. / (N - m)
    for k in np.arange(0.,m):
        for l in np.arange(0.,m):
            Po = np.zeros((k,l))
            for t in np.arange(m,N-1):
                Po[k,l] = X[t-k]*X[t-l]+Po[k,l]
    P = c*Po
print P