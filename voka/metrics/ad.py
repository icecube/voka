from math import log

class AndersonDarling(object):
    
    def __call__(self, v1, v2):
        r"""
        Compare sequences v1, v2 with the Anderson-Darling test.
        """
        result = 0.
        Nu = float(sum(v1))
        Nv = float(sum(v2))
        
        if Nu == 0 or Nv == 0:
            return 0.
    
        factor = 1./(Nu+Nv)
        sigma_j = 0.
        sigma_uj = 0.
        sigma_vj = 0.
        for i,uv in enumerate(zip(v1, v2)):
            u = float(uv[0])
            v = float(uv[1])
            if u == 0 and v == 0:
                continue
            t = u + v

            sigma_uj += u
            sigma_vj += v
            sigma_j += t
            
            term1 = (1./Nu)*((Nu+Nv)*sigma_uj - Nu*sigma_j)**2
            term2 = (1./Nv)*((Nu+Nv)*sigma_vj - Nv*sigma_j)**2

            denom = sigma_j *(Nu + Nv - sigma_j)
            if denom == 0 :
                continue
            result += t*(term1 + term2)/denom

        T = factor * result
        return T
