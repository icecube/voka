'''
This module contains the compare function.
'''
import voka.metrics.chisq
import voka.metrics.bdm
import voka.metrics.ks
import voka.metrics.llh
import voka.metrics.cvm
import voka.metrics.ad

ALL_METRICS = [voka.metrics.chisq.NormChiSq(),
               voka.metrics.chisq.ShapeChiSq(),
               voka.metrics.bdm.BDM(),
               voka.metrics.ks.KolmogorovSmirnof(),
               voka.metrics.llh.LLHRatio(),
               voka.metrics.llh.LLHValue(),
               voka.metrics.cvm.CramerVonMises(),
               voka.metrics.ad.AndersonDarling()]

DEFAULT_METRICS = [voka.metrics.chisq.ShapeChiSq(),
                   voka.metrics.ad.AndersonDarling()]

def compare(values1, values2, metrics=None):
    r'''
    To use all metrics set metrics to 'all_metrics'
    Output:
        result : dict
            test name : value of test statistic
            Will be empty if no tests enabled, or histograms inconsistent.
    '''

    result = {}
    if len(values1) != len(values2):
        print("ERROR : sequences are inconsistent.")
        return result

    _metrics = metrics if metrics else DEFAULT_METRICS

    for metric in _metrics:
        result[metric.__class__.__name__] = metric(values1, values2)

    return result
