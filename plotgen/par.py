import numpy as np
from dataset2d import *

mbh_0, mdot_0, radius_0, alpha_0 = 1e8, 0.01, 10.0, 0.1

mdots = np.logspace(-2.5, -0.5, 30)
radii = np.logspace(0.5, 2.5, 40)

if __name__ == '__main__':
    for i, mdot_ in enumerate(mdots):
        for j, radius_ in enumerate(radii):
            with open('data/' + ix2fn('map1-MR', (i, j)) + '.par', 'w') as f:
                f.write(dict2cfg(mbh = 1e1, mdot = mdot_, radius = radius_, alpha = alpha_0))
            with open('data/' + ix2fn('map8-MR', (i, j)) + '.par', 'w') as f:
                f.write(dict2cfg(mbh = 1e8, mdot = mdot_, radius = radius_, alpha = alpha_0))
