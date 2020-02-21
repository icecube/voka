
import voka.metrics.chisq
import voka.metrics.bdm 
import voka.metrics.ks
import voka.metrics.llh
import voka.metrics.cvm
import voka.metrics.ad

all_metrics = [voka.metrics.chisq.NormChiSq(),
               voka.metrics.chisq.ShapeChiSq(),
               voka.metrics.bdm.BDM(),
               voka.metrics.ks.KolmogorovSmirnof(),
               voka.metrics.llh.LLHRatio(),
               voka.metrics.llh.LLHValue(),
               voka.metrics.cvm.CramerVonMises(),
               voka.metrics.ad.AndersonDarling()]

default_metrics = [voka.metrics.chisq.ShapeChiSq(),                   
                   voka.metrics.ad.AndersonDarling()]

def compare(v1, v2, _metrics = default_metrics):
    r'''For all enabled test_{name}, compare hist1 and hist2.
    Output:
        result : dict 
            test name : value of test statistic 
            Will be empty if no tests enabled, or histograms inconsistent.    

            llh_value often returns -inf for histograms with moderate bin contents.
            Taking it out of the rotation for now. 
    '''

    result = {}
    if len(v1) != len(v2):
        print("ERROR : sequences are inconsistent.")
        return result

    for m in _metrics:
        result[m.__class__.__name__] = m(v1, v2)
    
    return result
    
    
