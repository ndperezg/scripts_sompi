#!/usr/bin/env python

from obspy.core import read, Trace, Stream, UTCDateTime
from glob import glob
import numpy as np
import datetime
import sys
import os

#if len(sys.argv)<2:
#    print "No hay parametros de entrada"
#    sys.exit()

#sismo = sys.argv[1]



def ascii2sac(sismograma):
    Wav, Head = [], []
    r=open(sismograma, 'rU')
    
    counter = 0
    for linea in r:
        counter+=1
        if counter <= 5:
            #               print linea
            Head.append(linea.strip())
        else:
            Wav.append(linea)
#print Head

    date = Head[2][0:10]
    hour = Head[2][11:19]
    Fs = float(Head[3][0:8])
    counts = float(Head[4][0:4])
    station = Head[1]
    #si la estacion es triaxial:
    channel = Head[1][3]
    esta = station[0:3]
    
    print date, hour, str(Fs), str(counts), station
    
    data = np.array(Wav, dtype=np.float32)
    #    print data
    
    if channel == 'Z':
        stats = {'network': 'OP', 'station': esta , 'location': '',
        'channel': 'BHZ', 'npts': len(data), 'sampling_rate': Fs,
        'mseed': {'dataquality': 'D'}}
    elif channel == 'N':
        stats = {'network': 'OP', 'station': esta , 'location': '',
        'channel': 'BHN', 'npts': len(data), 'sampling_rate': Fs,
        'mseed': {'dataquality': 'D'}}
    elif channel == 'E':
        stats = {'network': 'OP', 'station': esta , 'location': '',
        'channel': 'BHE', 'npts': len(data), 'sampling_rate': Fs,
        'mseed': {'dataquality': 'D'}}
    else:
        stats = {'network': 'OP', 'station': station , 'location': '',
        'channel': 'SHZ', 'npts': len(data), 'sampling_rate': Fs,
        'mseed': {'dataquality': 'D'}}

    Date = date+hour
    Date = datetime.datetime.strptime(Date, '%Y/%m/%d%H:%M:%S')
    starttime = UTCDateTime(Date)
    stats['starttime'] = starttime

    print stats
    
    st = Stream([Trace(data=data, header=stats)])
    st.write(r.name[0:-4]+'.sac', format='SAC', encoding=4)
    #    st1 = read(r.name[0:-4]+'.mseed')
    #    print st1
    #    st1.plot(color='r')
    return('traza convertida')

#ascii2sac(sismo)