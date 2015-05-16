#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


dict = {'COND':[(2002,3), (2005,7)],'PURA':[(1994,6)],'MINA':[(1999,7),(2006,6)],'CURI':[(1994,17),(2011,1)],'CHAG':[(1994,10)],'SNRF':[(1994,18)],'MACH':[(1998,6)],'AGBL':[(2007,5)],'SHAKA':[(2006,6)],'LARO':[(2006,6)],'COC':[(2010,2)]}

dict_color = {'COND':['lime', 'darkgreen'],'PURA':'lime','MINA':['lime','darkgreen'],'CURI':['lime','blue'],'CHAG':'lime','SNRF':'lime','MACH':'lime','AGBL':'lime','SHAKA':'lime','LARO':'lime','COC':'blue'}

ylabels = dict.keys()
yticks = range(0,len(dict))
xticks = np.arange(1992,2014,1)
wid= 0.30

fig, ax = plt.subplots()
for i,(sta,color) in enumerate(zip(dict,dict_color)):
    ax.broken_barh(dict[sta], (i-wid/2,wid),facecolors=dict_color[color])
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels,fontsize=15)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,rotation=70,fontsize=12)
fig.suptitle('Funcionamiento de las estaciones del volcan Purace', fontsize=20)
plt.show()
fig.savefig('funcionamiento_purace.jpg', dpi=150)

