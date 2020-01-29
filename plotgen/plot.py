#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import par
from dataset2d import ix2fn, DPA, read2Ddataset
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
from maputils import *

for bhe in [1,8]:
    for war in ['d','x','a0','a1']:

        ds = read2Ddataset(lambda i,j: 'data/map/'+war+'/' + ix2fn('map{}-MR'.format(bhe), (i, j)) + '.txt', 30, 40)

        fig, ax = plt.subplots(figsize = (8,5))

        zz = DPA(ds, 'rho_phot_nh')
        c1 = ax.contourf(par.radii, par.mdots, zz, levels = LogLvl(zz,9), norm = LogNorm())
        ax.set_xscale('log')
        ax.set_yscale('log')

        ax.set_xlabel('$R / R_{{\\rm schw}}$')
        ax.set_ylabel('$\\dot m$')
        ax.set_title('$n_{{\\rm H}}$ at $\\tau = 2/3$')

        plt.colorbar(c1, ax = ax)

        plt.savefig('map-M{}-{}.png'.format(bhe,war))
