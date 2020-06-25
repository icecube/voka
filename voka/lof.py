'''
  Module that contains the function that calculates a Local Outlier Factor.
  https://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf
'''
import numpy

def distance(vector1, vector2):
    '''
    Euclidean distance.
    '''
    array1 = numpy.array(vector1)
    array2 = numpy.array(vector2)
    return numpy.linalg.norm(array1-array2)

def reach(p, k, o, D):

    '''
    k-distance of object p is defined as the distance d(p,o) between
    p and an object o in D such that:
        i)  For at least k objects o' in D/{p} d(p,o') <= d(p,o)
        ii) For at most k-1 objects o' in D/{p} d(p,o') < d(p,o)
    '''
    distances = list()
    for op in D:
        d = distance(p, op)
        if d > 0:
            distances.append(d)
    distances.sort()
    kdistance = max(distances[:k]) if distances[:k] else 0.
    return max([kdistance, distance(p, o)])

def local_reachability_density(p, k, D):
    '''
    Local Reachability Density
    '''
    denominator = sum([reach(p, k, op, D) for op in D])
    return len(D)/denominator if denominator else 0.

def LOF(p, k, D):
    '''
    p - Test point.
    k - k-distance.
    D - Reference/benchmark cluster

    return the LocalOutlierFactor for point 'p' compared
    to collection of reference points in 'D', using k-distance 'k'.
    '''
    ratios = list()
    for op in D:
        numerator = local_reachability_density(op, k, D)
        denominator = local_reachability_density(p, k, D)
        if denominator:
            ratios.append(numerator/denominator)

    result = sum(ratios)/float(len(ratios)) if ratios else 0.
            
    return result
