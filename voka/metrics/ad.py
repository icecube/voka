'''
  The Anderson-Darling test statistic
'''

class AndersonDarling:
    '''
    Function object which calculates the Anderson-Darling
    test statistic between two sets of numbers.
    '''
    def __call__(self, vector1, vector2):
        r"""
        Calculates the AD test statistic between
        vector1 and vector2
        """
        result = 0.
        n_1 = float(sum(vector1))
        n_2 = float(sum(vector2))

        if n_1 == 0 or n_2 == 0:
            return 0.

        factor = 1./(n_1+n_2)
        sigma_j = 0.
        sigma_uj = 0.
        sigma_vj = 0.
        for v_1, v_2 in zip(vector1, vector2):

            if v_1 == 0 and v_2 == 0:
                continue
            term = v_1 + v_2

            sigma_uj += v_1
            sigma_vj += v_2
            sigma_j += term

            term1 = (1./n_1)*((n_1+n_2)*sigma_uj - n_1*sigma_j)**2
            term2 = (1./n_2)*((n_1+n_2)*sigma_vj - n_2*sigma_j)**2

            denominator = sigma_j *(n_1 + n_2 - sigma_j)
            if denominator == 0:
                continue
            result += term*(term1 + term2)/denominator

        result *= factor
        return result
