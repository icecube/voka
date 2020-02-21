from math import log
from scipy.special import binom

class CramerVonMises(object):
    
    def __call__(self, v1, v2):
        r"""
        Compare sequences v1, v2 with the Cramer-von-Mises test.
        """
        result = 0.
        Nu = float(sum(v1))
        Nv = float(sum(v2))
        if Nu == 0 and Nv == 0:
            return 0.

        for i,uv in enumerate(zip(v1, v2)):
            u = float(uv[0])
            v = float(uv[1])        
            t = u + v
            u_ecdf = sum([bn for bn in v1[:i]])/sum(v1)
            v_ecdf = sum([bn for bn in v2[:i]])/sum(v2)        
            result += t*(u_ecdf - v_ecdf)**2
        factor = Nu*Nv/(Nu+Nv)**2
        T = factor * result
        return T
