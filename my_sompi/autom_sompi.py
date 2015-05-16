#!/usr/bin/env python
"""
    Script basico para automatizar el metodo sompi
    basado en Kumazawa 1989
    
"""
import os
import sys
import numpy as np
import pymatlab
from glob import glob
from datetime import datetime
#-- revisa si hay archivo de entrada
#if len(sys.argv)<2:
#    print "No hay parametros de entrada"
#    sys.exit()

#---lee parametros de entrada

#sismograma = sys.argv[1]
#mmin = 15.
#mmax = 60.
#cellfrec = 50.
#cellgrow = 40.
#anchban = 0.2

files = sorted(glob('senales/*'))
log_file=open('log.out','w+')

session = pymatlab.session_factory()

for sismograma in files:
	
	
	try:
	 print sismograma
	 session.putvalue('inp',sismograma)
	 session.run('importar(inp)')
	 session.run('sompik')
	 session.run('clear')
		
	except:
	  print >> log_file, 'error en la senal '+sismograma 
	pass

	 
#del session
log_file.close()
os.system('cat log.out')
print datetime.now()

