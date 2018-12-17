import par
from dataset2d import ix2fn, DPA, read2Ddataset
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
from maputils import *

lili = {
    1: (16.0, 19.25),
    8: (9.5, 12.5),
}

for series in ['d', 'x']:
    for mbhe in [1, 8]:

        ds = read2Ddataset(lambda i,j: 'data/{}/'.format(series) + ix2fn('map{}-MR'.format(mbhe), (i, j)) + '.txt', 30, 40)

        fig, ax = plt.subplots(figsize = (9,6))

        zz = np.log10(DPA(ds, 'rho_phot_nh'))
        ncont = np.int0((lili[mbhe][1] - lili[mbhe][0]) / 0.25 + 1)
        ll = np.linspace(lili[mbhe][0], lili[mbhe][1], ncont)
        c1 = ax.contourf(par.radii, par.mdots, zz, ll, cmap = 'jet')
        ax.set_xscale('log')
        ax.set_yscale('log')

        ax.set_xlabel('$R / R_{{\\rm schw}}$')
        ax.set_ylabel('$\\dot m$')
        ax.set_title('$\\log n_{{\\rm H}}$ at $\\tau = 2/3$, $M=10^{{{mm}}}$, bil = {se}'
            .format(mm = mbhe, se = 'dyfu' if series == 'd' else 'coro'))

        plt.colorbar(c1, ax = ax, label = '$\\log n_{{\\rm H}}$', format = '%.1f')

        plt.savefig('map{}{}.png'.format(mbhe, series))
        plt.close(fig)
