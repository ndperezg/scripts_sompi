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

def amplitud(sismograma):

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
    X= np.arange(0,len(Wav)/Fs,1/Fs)
#    plt.subplot(212)
#    plt.plot(Wav)
#    plt.show()

#---Espectro de amplitud
    fig = plt.figure(1)
#ax1 = plt.axes(frameon=True)
#ax1.axes.get_yaxis().set_visible(False)
#ax1.axes.get_xaxis().set_visible(False)
    Fk = np.absolute(fft.fft(Wav))#Transformada de Fourier de la senal
    Fk = Fk/max(Fk)
    NFk = len(Fk)
    freq = fft.fftfreq(len(Wav), 1/Fs)
    print len(Wav), len(Fk)

    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot(2,1,1)
    ax2 = plt.subplot(2,1,2)
    ax1.plot(X,Wav)
    ax1.axis(xmin=0,xmax=max(X))
    ax1.set_xlabel('t(s)')
    ax1.set_ylabel('Amplitud normalizada')
    ax2.plot(freq,Fk,'k',linewidth=2)
    ax2.axis([0,20,0,max(Fk)])
    ax2.set_xlabel('F (Hz)')
    ax2.set_ylabel('Amplitud normalizada')
    fig.suptitle(Head[1]+"-"+Head[2], fontsize=25)
    fig.savefig("amp_"+Head[1]+"_1.jpg",dpi=180)
    plt.show()
    return(True)

amplitud(sismograma)