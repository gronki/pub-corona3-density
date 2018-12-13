import par
from dataset2d import ix2fn, DPA, read2Ddataset
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
from maputils import *

ds = read2Ddataset(lambda i,j: 'data/x/' + ix2fn('map1-MR', (i, j)) + '.txt', 30, 40)

fig, ax = plt.subplots(figsize = (8,5))

zz = DPA(ds, 'rho_phot_nh')
c1 = ax.contourf(par.radii, par.mdots, zz, levels = LogLvl(zz,9), norm = LogNorm())
ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel('$R / R_{{\\rm schw}}$')
ax.set_ylabel('$\\dot m$')
ax.set_title('$n_{{\\rm H}}$ at $\\tau = 2/3$')

plt.colorbar(c1, ax = ax)

plt.show()
