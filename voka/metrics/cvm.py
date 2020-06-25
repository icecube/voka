'''
Module contains a function object that calculates
the Cramer-von-Mises test statistic between two sets.
'''

class CramerVonMises:
    '''
    Function object that calculates
    the Cramer-von-Mises test statistic between two sets.
    '''

    def __call__(self, vector1, vector2):
        r"""
        Compare sequences vector1, vector2 with the Cramer-von-Mises test.
        """
        result = 0.
        if not any(vector1) and not any(vector2):
            return result

        Nu = float(sum(vector1))
        Nv = float(sum(vector2))

        for i, uv in enumerate(zip(vector1, vector2)):
            u = float(uv[0])
            v = float(uv[1])
            t = u + v
            u_ecdf = sum([bn for bn in vector1[:i]])/sum(vector1)
            v_ecdf = sum([bn for bn in vector2[:i]])/sum(vector2)
            result += t*(u_ecdf - v_ecdf)**2
        factor = Nu*Nv/(Nu+Nv)**2
        result = factor * result
        return result
