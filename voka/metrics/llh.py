'''
Module that contains two log-likehood based metrics.
1) LLHRatio
2) LLHValue
'''

from math import log
from scipy.special import binom

class LLHRatio:
    '''
    Function object that calculates the likelihood ratio
    between two numerical sequences.
    '''
    def __call__(self, vector1, vector2):
        r"""
        Calculates the Likelihood ratio between two sequences.
        """
        result = 0.
        if not any(vector1) and not any(vector2):
            return result

        sum1 = float(sum(vector1))
        sum2 = float(sum(vector2))

        for u_1, u_2 in zip(vector1, vector2):
            sum12 = u_1 + u_2
            if u_1 == 0 and u_2 == 0:
                result += 1
                continue
            if u_1 == 0:
                result += sum12*log(sum1/(sum1+sum2))
                continue
            if u_2 == 0:
                result += sum12*log(sum2/(sum1+sum2))
                continue
            term1 = sum12*log((1+u_2/u_1)/(1+sum2/sum1))
            term2 = u_2*log((sum2/sum1)*(u_1/u_2))
            result += term1 + term2

        return -2*result

class LLHValue:
    '''
    Function object that calculates the likelihood ratio
    between two numerical sequences.
    '''
    def __call__(self, vector1, vector2):

        r"""
        Compare histograms h1, h2 with the log likelihood value test.
        FIXME: This is currently returning inf on occasion.  It should
           never do that. Taking it out of the rotation.
        """
        result = 0.
        if not any(vector1) and not any(vector2):
            return result

        sum1 = float(sum(vector1))
        sum2 = float(sum(vector2))

        for u_1, u_2 in zip(vector1, vector2):
            sum12 = u_1 + u_2
            term1 = log(binom(sum12, u_2))
            term2 = sum12*log(sum1/(sum1 + sum2))
            term3 = u_2*log(sum2/sum1)
            result += term1 + term2 + term3

        return -result
