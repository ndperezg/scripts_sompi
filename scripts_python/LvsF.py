#! /usr/bin/env python
"""
    Relacion funcional entre L y f para m=2 y m=3
    
"""

import matplotlib.pyplot as plt
import numpy as np

####Calcula la longitud L####

epsilon = [0.1716,0.1129, 0.0835,0.0662,0.0547,0.0464,0.0402,0.0354]

def longitud(f,m, epsilon):
    A = 800*(m-1)
    C = 3*10e4*(1/120)*(1/5)*(1/5)
    B= 2*f*np.power(1+epsilon*C, 0.5)
    return(A/B)


F = np.arange(0.5,20,0.1)
m = np.arange(2,10,1)

fig, ax = plt.subplots(figsize=(10,6))

for i in range(len(m)):
    L = longitud(F,m[i],epsilon[i])
    ax.plot(F,L,'-', lw=5, label= 'm ='+str(m[i]))


ax.set_ylabel('L(m)', fontsize=20)
ax.set_xlabel('f(Hz)', fontsize=20)
ax.legend(loc=1,fontsize=20)
fig.savefig('../graficas/longitud.jpg', dpi=150)
plt.show()