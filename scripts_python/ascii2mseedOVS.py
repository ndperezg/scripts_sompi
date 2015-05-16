#!/usr/bin/env python

from ascii2sacOVS import ascii2sac
from glob import glob
import datetime
import sys
import os




log_file=open('log_sac.out','w+')

datos = sorted(glob('/Users/ndperezg/Documents/tesis_julio20/Datos/Purace_Tornillos_ascii/2011/*'))
for file in datos:
    events = sorted(glob(file+'/*'))
    os.system('mkdir '+file+'/formato_sac/')
    for sismograma in events:
        try:
            ascii2sac(sismograma)
        except:
            print >> log_file, 'error en la senal '+sismograma
        pass
        print sismograma
    os.system('mv '+file+'/*.sac '+file+'/formato_sac/')
    os.system('cp seisei.exp '+file+'/formato_sac/')
    os.system('cd '+file+'/formato_sac/; dirf *.sac; ./seisei.exp')
    os.system('cp '+file+'/formato_sac/*POP* ~/Documents/tesis_julio20/Proceso/LOC/')
    os.system('rm -rf '+file+'/formato_sac/'+'filenr.lis')
    os.system('rm -rf '+file+'/formato_sac/'+'seisei.exp')
#   print file

log_file.close()
os.system('cat log_sac.out')
