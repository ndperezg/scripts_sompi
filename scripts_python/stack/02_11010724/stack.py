#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
from scipy import signal
import sys
import os
import glob

#if len(sys.argv)<2:
#    print "No hay parametros de entrada"
#    sys.exit()

#sismograma = sys.argv[1]

def response_fft(sismograma):
	Wav, Head, date, hour = [], [], [], []
	r=open(sismograma, 'rU')

	counter = 0
	for linea in r:
    		counter+=1
    		if counter <= 5:
#        		print linea
        		Head.append(linea)
    		else:
       		 	Wav.append(float(linea))
	#print Head

	date.append(Head[2][0:10])
	hour.append(Head[2][11:24])
	Fs = float(Head[3][0:8])
	counts = float(Head[4][0:4])

#---prepara la senal 
	
	Wav = Wav - np.mean(Wav, dtype=np.float64)
	Wav = Wav/max(Wav)
	N = len(Wav)
	plt.subplot(311)
	plt.plot(Wav)	

#----disena filtro y filtra la senal

	b, a = signal.butter(6,0.016,'high')
	Wav = signal.lfilter(b,a,Wav)
	plt.subplot(312)
	plt.plot(Wav)
#	plt.show()

#---Espectro de amplitud

	Fk = np.absolute(fft.fft(Wav)) #Transformada de Fourier de la senal
	NFk = len(Fk)
	nu = fft.fftfreq(len(Wav),1/Fs) # Frecuencias naturales
#	F_norm = np.real(Fk)/max(np.real(Fk))
	print len(Wav), len(Fk)
	plt.subplot(313)
	plt.plot(nu,Fk)
	plt.axis([0,20,0,max(Fk)]) 
	plt.show()
	return Fk, Fs
#---Apila los espectros

prestack = []
for file in glob.glob('*.txt'):
	Fk, Fs = response_fft(file)
	prestack.append(Fk)
print 'FINAL prestack', len(prestack), len(prestack[0]), type(prestack[0]), Fs

stack = np.zeros(len(prestack[0]), dtype='float64', order='C')
print type(stack), len(stack)

for i in range(len(prestack)):
	stack+=prestack[i]

NFk = len(stack)
nu_stack = fft.fftfreq(len(stack),1/Fs)
plt.figure(2)
plt.plot(nu_stack,stack,'r')
plt.axis([0,20,0,max(stack)])
plt.title('Stack Espectral') 
plt.show()		




