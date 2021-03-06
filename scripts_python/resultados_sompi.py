#! /usr/bin/env python
"""
    Hace graficas de elementos de onda para una estacion
    junto con espectro de amplitud normalizado
"""

import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
from numpy import fft
from scipy import signal
import os
import sys

####Prepara datos para grafica de espectro

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

#----disena filtro y filtra la senal

b, a = signal.butter(6,0.016,'high')
Wav = signal.lfilter(b,a,Wav)

#---Espectro de amplitud

Fk = np.absolute(fft.fft(Wav)) #Transformada de Fourier de la senal
NFk = len(Fk)
Fk = Fk/max(Fk)
freq = fft.fftfreq(Wav.shape[-1], 1/Fs)



##### Prepara datos para grafica de wave-elements
f=open('ff.txt')
g=open('gg.txt')

F, G = [], []

for line in f:
    F.append(100*float(line))
for line in g:
    G.append(100*float(line))


f = np.arange(0,50,1)
Q = np.arange(1,900,50)
invQ = 1./(2*Q)

print len(Fk), len(Wav), type(Fs), freq[-1]


###GRAFICA######
fig = plt.figure(figsize=(20,20))
gs = gridspec.GridSpec(2, 1, height_ratios=[4,1])
ax = fig.add_subplot(gs[0])
for i in range(0,len(Q)):
	g = -f*invQ[i]
	ax.plot(f,g, 'k',linewidth=2)
	ax.grid('on')
ax.set_title(Head[1]+" "+date[0]+" "+hour[0], fontsize =25)
ax.axis([0,15,-0.05,0])
ax.text(5, -0.048, 'Q = 50', fontsize = 20)
ax.text(8.01, -0.039, 'Q = 100', fontsize = 20)
ax.text(12.01, -0.039, 'Q = 150', fontsize = 20)
ax.text(12.01, -0.006, 'Q = 900', fontsize = 20)
ax.set_ylabel('Growth rate ($10^{-2}$ Hz)', fontsize=20)
ax.scatter(F,G,s=320,facecolors='none', edgecolors='k')
ax1 = fig.add_subplot(gs[1])
ax1.plot(freq,Fk, 'k',linewidth=2)
ax1.axis([0,15,0,max(Fk)])
#ax1.set_aspect(aspect=2.5)
ax1.set_xlabel('Frequency (Hz)', fontsize=20)
plt.show()
fig.savefig('resultado'+Head[1]+'_1.jpg', dpi=90)



