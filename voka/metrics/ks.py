from math import fabs

class KolmogorovSmirnof(object):
    def __call__(self, v1, v2):
        r"""Calculate the Kolmogorov-Smirnof test statistic for two sequences
        which are assumed to have the same binning. The binning needs to be small
        compared to important features of the histograms.
        Output:
        T : float
            Maximum distance between the cumulative distributions.            
        """
        assert(len(v1) == len(v2))
        
        nbins = len(v1)
        s1 = sum(v1)
        s2 = sum(v2)
        
        if s1 == 0 and s2 == 0:
            return 0.

        cdf_diffs = [fabs(sum(v1[:i])/s1 - sum(v2[:i])/s2)
                     for i in range(nbins)]
        T = max(cdf_diffs)    
        return T
        
    
