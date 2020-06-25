'''
Module contains two functions objects that calculate
a ChiSq for both cases where two sets are assumed
to have the same normalization and not.
'''

class NormChiSq:
    r"""Compare sequences vector1, vector2 with a Chi^2 test.
        Assumes they have the same binning.
        Output:
        chisq : float
            A Chi^2 sum over all bins.
    """

    def __call__(self, vector1, vector2):
        '''
        Calculate the ChiSq
        '''

        assert len(vector1) == len(vector2)

        # calculate the \chi^2 test statistic
        terms = [(u - v)**2/(u + v) \
                 for u, v in zip(vector1, vector2)\
                 if u > 0 and v > 0]
        result = sum(terms)
        return result

class ShapeChiSq:
    r"""Compare sequences vector1, vector2 with a Chi^2 test after
    normalizing them.
    Output:
        chisq : float
            A Chi^2 sum over all bins.
    """

    def __call__(self, vector1, vector2):
        '''
        Calculate the ChiSq
        '''
        assert len(vector1) == len(vector2)

        sum1 = sum(vector1)
        sum2 = sum(vector2)
        try:
            n1sq = sum1**2
            n2sq = sum2**2
            terms = [(u/sum1 - v/sum2)**2/(u/n1sq + v/n2sq) \
                     for u, v in zip(vector1, vector2) \
                     if u > 0 and v > 0]
        except ZeroDivisionError:
            ratio = float(sum1)/sum2
            ssq = ratio**2
            terms = [(u/ratio - v)**2/(u/ssq + v) \
                     for u, v in zip(vector1, vector2) \
                     if u > 0 and v > 0]

        result = sum(terms)
        return result
