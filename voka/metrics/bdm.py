'''
  The Bhattacharyya Distance Measure.
'''

from math import sqrt

class BDM:
    '''
    Function object which calculates the BDM
    test statistic between two sets of numbers.
    '''
    def __call__(self, vector1, vector2):
        r"""
        Compare numerical set vector1 and vector2
        using the Bhattacharyya distance measure.
        Treating their entries vectors, normalize, and take the dot product.
        Output:
        ts : float
            The BDM test statistic
        """
        assert len(vector1) == len(vector2)

        if sum(vector1) == 0 or sum(vector2) == 0:
            return 1. # if they're both empty they're identical

        terms = [u*v for u, v in zip(vector1, vector2)]
        sum1 = sum(vector1)
        sum2 = sum(vector2)
        denominator = sqrt(sum1*sum2)
        result = sqrt(sum(terms))/denominator\
            if denominator else 0.
        return result
