
# https://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf

import numpy

def _distance(v1, v2):
    '''
    Euclidean distance.
    '''
    a1 = numpy.array(v1)
    a2 = numpy.array(v2)
    return numpy.linalg.norm(a1-a2)
                                
def _reach(p, k, o, D):

    '''
    k-distance of object p is defined as the distance d(p,o) between
    p and an object o in D such that:
        
    i)  For at least k objects o' in D/{p} d(p,o') <= d(p,o)
    ii) For at most k-1 objects o' in D/{p} d(p,o') < d(p,o)
    '''
    distances = [_distance(p, op) for op in D if p != op]
    distances.sort()
    kdistance = max(distances[:k]) if distances[:k] else 0.
    return max([kdistance, _distance(p, o)])

def _lrd(p, k, D):
    '''
    Local Reachability Density
    '''
    denominator = sum([_reach(p, k, op, D) for op in D])
    return len(D)/denominator if denominator else 0.

def LOF(p, k, D):
    '''
    p - Test point.
    k - k-distance.
    D - Reference/benchmark cluster

    return the LocalOutlierFactor for point 'p' compared
    to collection of reference points in 'D', using k-distance 'k'.
    '''
    ratios = [_lrd(op, k, D)/_lrd(p, k, D)
              for op in D
              if _lrd(p, k, D)]
    
    return sum(ratios)/float(len(ratios)) if ratios else 0.
