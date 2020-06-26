'''
  The Kolmogorov-Smirnov test statistic.
'''

from math import fabs

class KolmogorovSmirnov:
    '''
    Function object which calculates the KS
    test statistic between two sets of numbers.
    '''
    def __call__(self, vector1, vector2):
        r"""Calculate the Kolmogorov-Smirnov test statistic
        for two numerical sequences of the same length

        Output:
        T : float
            Maximum distance between the cumulative distributions.
        """
        assert len(vector1) == len(vector2)

        nbins = len(vector1)
        sum1 = sum(vector1)
        sum2 = sum(vector2)

        if sum1 == 0 and sum2 == 0:
            return 0.

        cdf_diffs = [fabs(sum(vector1[:i])/sum1 - sum(vector2[:i])/sum2)
                     for i in range(nbins)]
        result = max(cdf_diffs)
        return result
