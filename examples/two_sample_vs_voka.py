#!/usr/bin/env python3

'''
This example exercises the two sample statistical tests
available from scipy:
* scipy.stats.ttest_ind
* scipy.stats.ks_2samp
* scipy.stats.anderson_ksamp
* scipy.stats.epps_singleton_2samp
* scipy.stats.mannwhitneyu
* scipy.stats.ranksums
* scipy.stats.wilcoxon
* scipy.stats.kruskal
* scipy.stats.friedmanchisquare
* scipy.stats.brunnermunzel
'''

import os
import pickle

import numpy
import pylab
import scipy.stats
import pylab

import voka.tools.samples
import voka.model
import voka.tools.render

def voka_2sample(sample1, sample2):
    # Checkout OnlineL2_SplitTime2_SPE2itFitEnergy
    # hiccup #1 (AD) ValueError: anderson_ksamp needs more than one distinct observation
    # hiccup #2 (ES) numpy.linalg.LinAlgError: SVD did not converge
    # hiccup #3 (TT) Ttest_indResult(statistic=nan, pvalue=nan)
    # hiccup #4 (MW) ValueError: All numbers are identical in mannwhitneyu
    # hiccup #5 (WP) ValueError: zero_method 'wilcox' and 'pratt' do not work if x - y is zero for all elements
    # hiccup #6 (FC) ValueError: Less than 3 levels.  Friedman test not appropriate.

    result = dict()

    r = scipy.stats.ttest_ind(sample1, sample2)
    result['TTest'] = {
        'statistic': r.statistic,
        'pvalue': r.pvalue
    }
    
    r = scipy.stats.ks_2samp(sample1, sample2)
    result['KolmogorovSmirnov'] = {
        'statistic': r.statistic,
        'pvalue': r.pvalue
    }
    
    try:
        r = scipy.stats.anderson_ksamp([sample1, sample2])
        result['AndersonDarling'] = {
            'statistic': r.statistic,
            'significance_level': r.significance_level
        }
    except ValueError:
        #print("    skipping anderson_ksamp")
        pass
        
    try:
        r = scipy.stats.epps_singleton_2samp(sample1, sample2)
        result['EppsSingleton'] = {
            'statistic': r.statistic,
            'pvalue': r.pvalue
        }
    except numpy.linalg.LinAlgError:
        #print("    skipping epps_singleton_2samp")
        pass

    try:
        r = scipy.stats.mannwhitneyu(sample1, sample2)
        result['MannWhitneyU'] = {
            'statistic': r.statistic,
            'pvalue': r.pvalue
        }
    except ValueError:
        #print("    skipping mannwhitneyu")
        pass
        
    r = scipy.stats.ranksums(sample1, sample2)
    result['Ranksums'] = {
        'statistic': r.statistic,
        'pvalue': r.pvalue
    }

    try:
        r = scipy.stats.wilcoxon(sample1, sample2)
        result['Wilcoxon'] = {
            'statistic': r.statistic,
            'pvalue': r.pvalue
        }
    except ValueError:
        #print("    skipping wilcoxon")
        pass

    try:
        r = scipy.stats.kruskal(sample1, sample2)
        result['Kruskal'] = {
            'statistic': r.statistic,
            'pvalue': r.pvalue
        }        
    except:
        #print("    skipping kruskal")
        pass

    try:
        r = scipy.stats.friedmanchisquare(sample1, sample2)
        result['FriedmanChiSquare'] = {
            'statistic': r.statistic,
            'pvalue': r.pvalue
        }        
    except ValueError:
        #print("    skipping friedmanchisquare")
        pass
        
    r = scipy.stats.brunnermunzel(sample1, sample2)
    result['BrunnerMunzel'] = {
        'statistic': r.statistic,
        'pvalue': r.pvalue
    }        

    return result

# make two samples containing
# 'standard' numpy distributions
_range = (-5,5)
widths = [w+0.1 for w in numpy.arange(0.1, 2.0, 0.1)]
locs = [l+0.1 for l in numpy.arange(-.5, 0.5, 0.1)]
size = 100
test_samples_low = list()
test_samples_high = list()
#test_samples = [numpy.histogram(
#                for w in widths]
#for w in widths:
#    d = numpy.random.normal(size=1000, scale=w)
#    # need to make sure the binning is the same
#    h = numpy.histogram(d, range=_range)
#    test_samples.append(h[0])
    
for l in locs:
    d_low = numpy.random.normal(size=100, loc=l)
    d_high = numpy.random.normal(size=1000, loc=l)
    # need to make sure the binning is the same
    h_low = numpy.histogram(d_low, range=_range)
    h_high = numpy.histogram(d_high, range=_range)
    test_samples_low.append(h_low[0])
    test_samples_high.append(h_high[0])
    
benchmark_samples = [numpy.histogram(numpy.random.normal(size=size, scale=1.0),
                                     range=_range)[0]
                     for _ in range(10)]

model = voka.model.Voka()
reference_collection = {"Benchmark%d" % idx : {"Gaussian":s}
                        for idx, s in enumerate(benchmark_samples)}
model.train(reference_collection)

for idx, (test_sample_low, test_sample_high) \
    in enumerate(zip(test_samples_low, test_samples_high)):
    print(test_sample_low)
    print(test_sample_high)
    print(80*"-")
    #print("width = %.2f" % widths[idx])
    print("loc = %.2f" % locs[idx])
    benchmark_sample = numpy.histogram(numpy.random.normal(size=1000, scale=1.0))[0]
    voka_2samp_result = voka_2sample(test_sample_high, benchmark_sample)
    for name, result in voka_2samp_result.items():
        if 'pvalue' in result:
            print("  %s p-value = %.4f" % (name, result['pvalue']))
    
    # I need to fix this.
    # The test labels and the benchmark labels need to match exactly.
    voka_ksamp_result = model.execute({"Gaussian" : test_sample_low})
    r = model.results(voka_ksamp_result)['Gaussian']
    print("%s lof = %.2f threshold = %.2f" % (r['pass'], r['lof'], r['threshold']))
    voka.tools.render.draw_comparisons(test_sample_low, benchmark_samples)
    pylab.show()
    
