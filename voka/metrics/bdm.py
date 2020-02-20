from math import sqrt
from math import log10

class BDM(object):
    def __call__(self, v1, v2):
        r"""
        Compare histograms h1, h2 with the Bhattacharyya distance measure.
        Assumes the histograms have the same binning. 
        Treating their entries vectors, normalize, and take the dot product.
        Output:
        ts : float
            The BDM.    
        """
        assert(len(v1) == len(v2))

        if sum(v1) == 0 or sum(v2) == 0:
            return 1. # if they're both empty they're identical
        
        terms = [u*v for u,v in zip(v1, v2)]
        n1 = sum(v1)
        n2 = sum(v2)
        p = sqrt(n1*n2) # math.sqrt casts its arguments to a float
        T = sqrt(sum(terms))/p 
        return T
            
