#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

volumen = [0.28e6,0.835e6,0.835e6,0.22e6,1.25e6,1.25e6]
dur_max = [97,200,185, 67,214, 180]
dur_av = [60,75, 80, 44, 87, 67]
erup =['16/07/92','14/01/93','23/03/93','13/04/93','07/06/93','23/09/94']
num_erup =np.arange(0,len(erup))
num_ev = [9,20,74,6,103,31]
wid = 0.1

fig, ax = plt.subplots(figsize = (12,8))

ax.grid(True)
ax.plot(num_erup,dur_max, 'o-', color = 'k', markersize=15, label = 'Duracion max.')
ax.plot(num_erup,dur_av,'o-', color ='lime', markersize=15, label = 'Duracion prom.')
rects = ax.bar(num_erup , num_ev, align= 'center', width = wid, color='b', label ='No. de eventos')
ax.set_xlim(-1,7)
ax.set_xticks(num_erup)
ax.set_xticklabels(erup, rotation= 30, fontsize = 13)
ax.set_ylim([1,300])
ax1 = ax.twinx()

for num in range(len(num_erup)):
    if num != 2 and num != 5:
        ax1.plot(num_erup[num],volumen[num], '*',color= 'r', markersize=20, label = 'Volumen emitido')

ax1.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))

for label in ax1.get_yticklabels():
    label.set_color("red")
ax1.set_ylabel('Volumen emitido (m$^3$)', fontsize = 18, color = 'r')

for label in ax.get_yticklabels():
    label.set_color("k")
ax.set_ylabel('Duracion de los sismos (s)', fontsize = 18, color = 'k')
ax.legend(loc=2)

plt.show()
fig.savefig('galeras.png', dpi=80)