#! /usr/bin/env python

import os
import sys

if len(sys.argv)<2:
    print "No hay parametros de entrada"
    sys.exit()

txt = sys.argv[1]


depurado = open('Resultados_Sompi.txt', 'w+')

os.system("./ordena_awk_1"+" "+txt)

r = open('ordenado.txt', 'r')
texto = r.readlines()
for line in texto:
	nfo = line.split(" ")		
	if float(nfo[10]) <= 10:
		print line
		print >> depurado, line.strip()
	
os.system('rm -rf ordenado.txt')


