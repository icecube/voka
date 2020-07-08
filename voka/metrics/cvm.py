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

        sum1 = float(sum(vector1))
        sum2 = float(sum(vector2))

        for i, u_v in enumerate(zip(vector1, vector2)):
            u_ecdf = sum(vector1[:i])/sum1
            v_ecdf = sum(vector2[:i])/sum2
            result += sum(u_v)*(u_ecdf - v_ecdf)**2
        factor = sum1*sum2/(sum1+sum2)**2
        result *= factor
        return result
