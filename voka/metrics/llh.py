from math import log
from scipy.special import binom

class LLHRatio(object):
    
    def __call__(self, v1, v2):
        r"""
        Compare sequences v1, v2 with the log likelihood ratio test.
        """
        result = 0.
        Nu = float(sum(v1))
        Nv = float(sum(v2))
        
        if Nu == 0:
            if Nv == 0:
                return 1.
            else:
                return 0.
    
        for u,v in zip(v1, v2):
            u = float(u)
            v = float(v)
            t = u + v
            if u == 0 and v == 0:
                result += 1
                continue
            if u == 0:
                result += t*log(Nu/(Nu+Nv))
                continue        
            if v == 0:
                result += t*log(Nv/(Nu+Nv))
                continue
            term1 = t*log((1+v/u)/(1+Nv/Nu))
            term2 = v*log((Nv/Nu)*(u/v))
            result += term1 + term2
            T = -2*result
            return T

class LLHValue(object):
    
    def __call__(self, v1, v2):

        r"""
        Compare histograms h1, h2 with the log likelihood value test.
        FIXME: This is currently returning inf on occasion.  It should
           never do that. Taking it out of the rotation.
        """
        result = 0.
        Nu = float(sum(v1))
        Nv = float(sum(v2))
        if Nu == 0 and Nv == 0:
            return 0.
    
        for u,v in zip(v1, v2):
            u = float(u)
            v = float(v)        
            t = u + v
            bn = binom(t,v)
            term1 = log(bn)
            term2 = t*log(Nu/(Nu + Nv))
            term3 = v*log(Nv/Nu)
            result += term1 + term2 + term3
            T = -result
            return T

