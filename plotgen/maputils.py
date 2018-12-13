import numpy as np

contw = lambda n: np.logspace(np.log10(0.9), np.log10(1.6), n)
contw = lambda n: np.linspace(0.8, 1.1, n)

def LogLvl(z, n, vmin = None, vmax = None, margin = 0.33):
    l = np.log10(np.min(z) if not vmin else max(np.min(z), vmin))
    u = np.log10(np.max(z) if not vmax else min(np.max(z), vmax))
    w = (u - l) / n
    return np.logspace(l + margin * w, u - margin * w, n)

def GrandLogLvl(z, n, vmin = None, vmax = None):
    l = np.log10(np.min(z) if not vmin else max(np.min(z), vmin))
    u = np.log10(np.max(z) if not vmax else min(np.max(z), vmax))
    return np.logspace(np.floor(l * 3) / 3, np.ceil(u * 3) / 3, n)

def LogTicks(a, b, grading = 2, digits = 1):
    t = np.logspace(a, b, (b - a) * grading + 1)
    e = np.floor(np.log10(t))
    f = np.round(t * 10**(digits - 1) / 10**e) / 10**(digits - 1)
    return f * 10**e
