#awk '{print $1 " " $2 " " $3 " " $4 " " $5 " " $6 " " $7 " " $8 " " $9 " " $10 " "}' Resultados_Sompi.txt > ordenado.txt
from pylab import *
from numpy import power
Date,Hour,Sta,Event,Freq,ErrFreq,G,ErrG,Q,ErrQ,X,Y =[],[],[],[],[],[],[],[],[],[],[],[] # crea listas
r=open('ordenado.txt','rU')
sompi=r.readlines()# lee lineas del archivo
for line in sompi:
    nfo=line.split(" ")
    Date.append(nfo[0]) # columna fecha
    Hour.append(nfo[1]) # columna hora
    Sta.append(nfo[2])  # columna estacion
    Event.append(nfo[3]) # columna tipo de evento
    Freq.append(float(nfo[4])) # columna frecuencias
    ErrFreq.append(float(nfo[5])) # error frecuencia
    G.append(float(nfo[6])) # grouth rate
    ErrG.append(float(nfo[7])) # error en g
    Q.append(float(nfo[8])) # factor de atenuacion
    ErrQ.append(float(nfo[9])) # error en Q
    if 'LARO' in line:
        print line
        Freq.append(float(nfo[4]))
        Q.append(float(nfo[8]))
        ErrQ.append(float(nfo[9]))
print Date[-1], Hour[-1], Sta[-1], Event[-1], Freq[-1], ErrFreq[-1], G[-1], ErrG[-1], Q[-1], ErrQ[-1] # imprime la ultima parte adjuntada
Q=power(Q,-1)
ErrQ=power(ErrQ,-1)
loglog(Freq,Q,'o')
errorbar(Freq,Q, ErrQ, xerr=None, fmt=None, ecolor='blue')
xlabel('F(Hz)')
ylabel('Q')

savefig("exercice_2.pdf",dpi=72)
show()