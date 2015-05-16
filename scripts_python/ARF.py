#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from obspy.signal.array_analysis import array_transff_wavenumber

coords = np.array([[2.3202, -76.3866, 4289.], [2.3248, -76.3938, 4294.], [2.3171, -76.4166, 4049.],
                   [2.3010,-76.4141 , 4507], [2.3108, -76.4099, 4075],[2.3771,-76.3527,3518],[2.2873,-76.3756,4445]])

#coords /= 111.2

klim = 400.
kxmin = -klim
kxmax = klim
kymin = -klim
kymax = klim
kstep = klim / 100.

transff = array_transff_wavenumber(coords, klim, kstep, coordsys='xy')

fig = plt.figure(1)
plt.pcolor(np.arange(kxmin, kxmax + kstep * 1.1, kstep) - kstep / 2.,
           np.arange(kymin, kymax + kstep * 1.1, kstep) - kstep / 2.,
           transff.T)

plt.colorbar()
plt.clim(vmin=0., vmax=1.)
plt.xlim(kxmin, kxmax)
plt.ylim(kymin, kymax)
plt.show()
fig.savefig('ARF.png', dpi=80)