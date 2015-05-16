#!/usr/bin/env python

from obspy.core import read, Trace, Stream, UTCDateTime
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sys
import os

if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

sismograma = sys.argv[1]

Wav, Head = [], []
r=open(sismograma, 'rU')

counter = 0
for linea in r:
    counter+=1
    if counter <= 5:
#        print linea
        Head.append(linea.strip())
    else:
        Wav.append(float(linea))
#print Head

date = Head[2][0:10]
hour = Head[2][11:19]
Fs = float(Head[3][0:8])
counts = float(Head[4][0:4])
station = Head[1]

print date, hour, str(Fs), str(counts), station

data = np.array(Wav, dtype=np.float32)
print data

stats = {'network': 'OP', 'station': station , 'location': '',
    'channel': 'SHZ', 'npts': len(data), 'sampling_rate': Fs,
    'mseed': {'dataquality': 'D'}}

Date = date+hour
Date = datetime.datetime.strptime(Date, '%Y/%m/%d%H:%M:%S')
starttime = UTCDateTime(Date)
stats['starttime'] = starttime

print stats

st = Stream([Trace(data=data, header=stats)])
st.write(r.name[0:-4]+'.mseed', format='MSEED', encoding=4)
st1 = read(r.name[0:-4]+'.mseed')
print st1
st1.plot(color='r')
