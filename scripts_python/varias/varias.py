#!/usr/bin/env python2.7

import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from glob import glob

y_offset = 2.0
fig1 = plt.figure(facecolor='white',figsize=(20,20))
ax1 = plt.axes(frameon=True)
ax1.get_xaxis().tick_bottom() 
ax1.axes.get_yaxis().set_visible(False) # Hide y axis
#ax1.axes.get_xaxis().set_visible(False)
#ax1.set_frame_on(False)     # Alternate way to turn frame off


sismogramas = sorted(glob('*PTO*'))

for i in range(len(sismogramas)):

	Wav, Head, date, hour = [], [], [], []
	r=open(sismogramas[i], 'rU')
	
	counter = 0
	for linea in r:
    		counter+=1
    		if counter <= 5:
        		print linea
        		Head.append(linea.strip())
    		else:
        		Wav.append(float(linea))
	print Head
	

	date.append(Head[2][0:10])
	hour.append(Head[2][11:24])
	Fs = float(Head[3][0:8])
	counts = float(Head[4][0:4])
	X= np.arange(0,len(Wav)/Fs,1/Fs)
	Wav = np.array(Wav)
	Wav = Wav - np.mean(Wav, dtype=np.float64)
	Wav = Wav/max(Wav)
	ax1.plot(X,Wav + i*y_offset,'k')
	plt.text(23,0.5 + i*y_offset,Head[1]+" "+date[0]+" "+hour[0], fontsize=25)

plt.tick_params(labelsize=25)
plt.xlabel('t (s)',fontsize=25)
plt.xlim(right=40)	
plt.show()
fig1.savefig('varias_'+str(len(sismogramas))+'.jpg',dpi=80)
	

