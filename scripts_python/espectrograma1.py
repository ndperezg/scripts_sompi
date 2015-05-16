#!/usr/bin/env python
"""
    Hace grafica de sismograma y espectrograma. Input: archivo ascii de ovs
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
Wav = Wav/max(Wav)

fig = plt.figure(figsize=(15,10))
ax1 = plt.subplot(211)
ax1.plot(X,Wav)
ax1.axis([min(X),100,min(Wav),max(Wav)])
ax1.set_ylabel('Amplitud',fontsize=23)
ax1.tick_params(labelsize=22)
ax1.set_xlabel('t(s)',fontsize=22)
ax1.text(58, 0.85, Head[1]+"-"+Head[2], fontsize=23)
ax2 = plt.subplot(212)
Pxx, freqs, bins, im = plt.specgram(Wav, NFFT=NFFT, Fs=Fs,noverlap=128)
ax2.axis([min(X),100,min(freqs),max(freqs)])
ax2.set_xlabel('t(s)',fontsize=23)
ax2.set_ylabel('Frecuencia (Hz)',fontsize=23)
ax2.tick_params(labelsize=22)
#plt.suptitle(Head[1]+"-"+Head[2], fontsize=25)
plt.show()
fig.savefig(Head[1]+".jpg",dpi=80)

