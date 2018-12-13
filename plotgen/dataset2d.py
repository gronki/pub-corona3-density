# Dominik Gronkiewicz (c) 2017
# this source is distributed under MIT License
# gronki@camk.edu.pl


def pyminiconf_dict(f):
    import re

    buf = f.read() + "\n"
    d = {}

    # multiline strings
    rp = r'([a-zA-Z0-9\_\-\:]+)(?:[ ]+|[ ]*\=[ ]*)\"([^\"]*)\"\s+'
    for k,v in re.findall(rp,buf):
        d[k] = v
    buf = re.sub(rp,'',buf)

    # komentarze
    buf = re.sub(r'\#[^\n]+','',buf)

    for k,v in re.findall(r'([a-zA-Z0-9\_\-\:]+)(?:[ ]+|[ ]*\=[ ]*)([\+\-]?[0-9]+)\s+',buf):
        d[k] = int(v)
    for k,v in re.findall(r'([a-zA-Z0-9\_\-\:]+)(?:[ ]+|[ ]*\=[ ]*)([\+\-]?[0-9]+\.[0-9]+)\s+',buf):
        d[k] = float(v)
    for k,v in re.findall(r'([a-zA-Z0-9\_\-\:]+)(?:[ ]+|[ ]*\=[ ]*)([\+\-]?[0-9]+\.?[0-9]*[eE][\+\-]?[0-9]+)\s+',buf):
        d[k] = float(v)

    for k,v in re.findall(r'([a-zA-Z0-9\_\-\:]+)(?:[ ]+|[ ]*\=[ ]*)([yYtT]|[fFnN])\s+',buf):
        d[k] = (v in ['T','t','Y','y'])

    for k,v in re.findall(r'([a-zA-Z0-9\_\-\:]+)(?:[ ]+|[ ]*\=[ ]*)([^0-9\-\+\s][^\s\#]+)\s+',buf):
        d[k] = v

    return d

class pyminiconf(object):
    def __init__(self,f):
        d = pyminiconf_dict(f)
        for k,v in d.items():
            setattr(self, k, v)

#------------------------------------------------------------------------------#

ix2fn = lambda s,ix: s[:-len(ix)] + ''.join([ '{}{:02d}'.format(a,i+1) for a,i in zip(s[-len(ix):],ix) ])
dict2cfg = lambda **kw: u''.join('{:9s} {}\n'.format(k,v) for k,v in kw.items())

#------------------------------------------------------------------------------#
# reads filename pattern declared by lambda expression fn and dimensions N1 and N2

def read2Ddataset(fn, N1, N2):
    from numpy import ndarray
    dset = ndarray((N1,N2), dtype = object)
    for i in range(N1):
        for j in range(N2):
            try:
                with open(fn(i,j), 'r') as f:
                    dset[i,j] = pyminiconf(f)
            except IOError:
                dset[i,j] = None
    return dset

#------------------------------------------------------------------------------#
# extracts the array of key k from dataset dset

def DPA(dset, k, mask = True):
    okay = lambda d: d != None \
        and hasattr(d,k) and type(getattr(d,k)) != str \
        and hasattr(d,'converged') and d.converged

    from numpy import vectorize, nan
    d0 = vectorize(lambda d: getattr(d,k) if okay(d) else nan)(dset)
    if not mask: return d0

    from numpy.ma import masked_where
    dm = vectorize(lambda d: not okay(d))(dset)
    return masked_where(dm, d0)
