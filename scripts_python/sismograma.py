#!/usr/bin/env python
"""
    Hace grafica de sismograma. Input: archivo ascii de ovs
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

sismograma = sys.argv[1]

Wav, Head, date, hour = [], [], [], []
r=open(sismograma, 'rU')

counter = 0
for linea in r:
    counter+=1
    if counter <= 5:
        print linea
        Head.append(linea.strip())
    else:
        Wav.append(float(linea))


date.append(Head[2][0:10])
hour.append(Head[2][11:24])
Fs = float(Head[3][0:8])
counts = float(Head[4][0:4])

#print date, hour, str(Fs), str(counts)
Fs=100.0
NFFT=256
print len(Wav), len(Wav)/Fs,1/Fs
X= np.arange(0,len(Wav)/Fs,1/Fs)

Wav = np.array(Wav)
Wav = Wav - np.mean(Wav, dtype=np.float64)
#Wav = Wav/max(Wav)

x = X.tolist()
w = Wav.tolist()

#print len(X[x.index(35),x.index(90)])
#print len(Wav[x.index(35),x.index(90)])

fig, ax = plt.subplots(figsize=(15,7))
ax.plot(X,Wav,'k')
ax.axvline(x=25, ymin=min(Wav),ymax=max(Wav),linewidth= 4, color='red')
ax.axvline(x=120, ymin=min(Wav),ymax=max(Wav),linewidth= 4, color='red')
sub = fig.add_subplot(111)
sub.plot(X[x.index(25):x.index(120)],Wav[x.index(25):x.index(120)])
ax.set_ylabel('Amplitud (cuentas)', fontsize = 15)
ax.set_xlabel('t(s)', fontsize = 15)
fig.suptitle(Head[1]+"-"+Head[2], fontsize=25)
plt.show()
fig.savefig("sismograma"+Head[1]+".jpg",dpi=80)