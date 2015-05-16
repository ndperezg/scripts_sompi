#!/usr/bin/env python
"""
    calcula movimiento de particula con respuesta instrumental y para una banda
    de frecuencia fmin, fmax y comienzo de la senal en segundos
"""
from obspy.core import read
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

wave = sys.argv[1]
station = sys.argv[2]
f1= float(sys.argv[3])
f2= float(sys.argv[4])
starttime = float(sys.argv[5])

paz_guralp_z = {'poles': [-0.0740159 - 0.0740159j, -0.0740159 + 0.0740159j, -0.0113097 + 0j,
              -0.0015310 + 0j, -0.0502655 + 0j],
              'zeros': [0+0j, 0+0j, 0j],
              'gain': 3122073.057,
              'sensitivity': 5906000.0}

wave = read(wave)
st = wave.select(station= station)
t = st[0].stats.starttime + starttime
st.simulate(paz_remove=paz_guralp_z, remove_sensitivity=False)
st.filter('bandpass', freqmin = f1, freqmax = f2)
st.plot()

tr1=st.select(channel='*N*')[0]
tr2=st.select(channel='*E*')[0]
T = np.arange(0, tr1.stats.npts / tr1.stats.sampling_rate, tr1.stats.delta)
time = np.arange(0,30,5)
print time

ncols = 3
nrows = 2

fig = plt.figure()
axes = [fig.add_subplot(nrows, ncols, r * ncols + c) for r in range(0, nrows) for c in range(0, ncols)]
for i, ax in zip(range(len(time)),axes):
    N=tr1.copy().trim(t+time[i],t+time[i]+5)
    E=tr2.copy().trim(t+time[i],t+time[i]+5)
    ax.plot(E.data,N.data)

    
plt.show()

"""
for i in range(len(time)):
    print t+time[i], t+time[i]+5
    n = tr1.trim(t+time[i], t+time[i]+5).data
    e = tr2.trim(t+time[i], t+time[i]+5).data
    plt.plot(e,n)
    plt.show()
    tr1=st.select(channel='*N*')[0]
    tr2=st.select(channel='*E*')[0]
"""


#ax.plot(T,N)
#ax.plot(E,N)
