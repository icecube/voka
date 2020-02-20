
class NormChiSq(object):
    r"""Compare sequences v1, v2 with a Chi^2 test.
        Assumes they have the same binning.
        Output:
        chisq : float
            A Chi^2 sum over all bins.
    """
    
    def __call__(self, v1, v2):

        assert(len(v1) == len(v2))
        
        # calculate the \chi^2 test statistic
        terms = [(u - v)**2/(u + v) \
                 for u,v in zip(h1['bin_values'], h2['bin_values'])\
                 if u > 0 and v > 0]
        T = sum(terms)
        return T
    
    
class ShapeChiSq(object):
    r"""Compare sequences v1, v2 with a Chi^2 test after normalizing them.
    Assumes they have the same binning.
    Output:
        chisq : float
            A Chi^2 sum over all bins.            
    """

    def __call__(self, v1, v2):
        
        assert(len(v1) == len(v2))
        
        n1 = sum(v1)
        n2 = sum(v2)
        try:
            n1sq = n1**2
            n2sq = n2**2
            terms = [(u/n1 - v/n2)**2/(u/n1sq + v/n2sq) \
                     for u,v in zip(h1['bin_values'], h2['bin_values']) \
                     if u > 0 and v > 0 ]             
        except ZeroDivisionError:
            s = float(n1)/n2
            ssq = s**2
            terms = [(u/s - v)**2/(u/ssq + v) \
                     for u,v in zip(h1['bin_values'], h2['bin_values']) \
                     if u > 0 and v > 0 ]
            
        T = sum(terms)
        return T
    
    
