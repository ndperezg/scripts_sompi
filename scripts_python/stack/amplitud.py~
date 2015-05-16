#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
from scipy import signal
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
        Head.append(linea.strip())
    else:
        Wav.append(float(linea))


date.append(Head[2][0:10])
hour.append(Head[2][11:24])
Fs = float(Head[3][0:8])
counts = float(Head[4][0:4])

#---prepara la senal 

Wav = Wav - np.mean(Wav, dtype=np.float64)
Wav = Wav/max(Wav)
N = len(Wav)
plt.subplot(211)
plt.plot(Wav)	

#----disena filtro y filtra la senal

b, a = signal.butter(6,0.016,'high')
Wav = signal.lfilter(b,a,Wav)
plt.subplot(212)
plt.plot(Wav)
plt.show()

#---Espectro de amplitud
fig = plt.figure(1)
ax1 = plt.axes(frameon=True)
ax1.axes.get_yaxis().set_visible(False)
ax1.axes.get_xaxis().set_visible(False)
Fk = np.absolute(fft.fft(Wav)) #Transformada de Fourier de la senal
NFk = len(Fk)
freq = fft.fftfreq(len(Wav), 1/Fs)
print len(Wav), len(Fk)

plt.plot(freq,Fk,'k',linewidth=2)
plt.axis([0,20,0,max(Fk)])
plt.savefig("amp_"+Head[1]+".jpg",dpi=80)
plt.show()
