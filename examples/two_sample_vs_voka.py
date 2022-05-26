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
import collections

import numpy
import pylab
import scipy.stats
import pylab

import voka.tools.samples
import voka.model
import voka.tools.render

def voka_2sample(sample1, sample2):
    print(sample1, sample2)
    
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
locs = [l+0.1 for l in numpy.arange(-2.0, 2.0, 0.1)]
test_samples = list()

def gaussian_sample(loc=0.0, size=1000):
    RANGE = (-5,5)
    SCALE = 1.0
    return numpy.histogram(numpy.random.normal(size=size, scale=SCALE, loc=loc),
                           range=RANGE)[0]

test_samples = [gaussian_sample(loc=loc) for loc in locs]
test_samples_low = [gaussian_sample(loc=loc, size=100) for loc in locs]
benchmark_samples = [gaussian_sample(size=100) for _ in range(10)]                     
reference_collection = {"Benchmark%d" % idx : {"Gaussian":s}
                        for idx, s in enumerate(benchmark_samples)}
model = voka.model.Voka()
model.train(reference_collection)

results = collections.defaultdict(list)
for idx, test_sample in enumerate(test_samples):

    print("loc = %.2f" % locs[idx])
    benchmark_sample = gaussian_sample()
    voka_2samp_result = voka_2sample(test_sample, benchmark_sample)
    for name, result in voka_2samp_result.items():
        if 'pvalue' in result:
            #print("  %s p-value = %.4f" % (name, result['pvalue']))
            results[name].append(result['pvalue'])
    
    voka_ksamp_result = model.execute({"Gaussian" : test_samples_low[idx]})
    r = model.results(voka_ksamp_result)['Gaussian']
    print("%s lof = %.2f threshold = %.2f" % (r['pass'], r['lof'], r['threshold']))
    results['voka'].append(r['lof'])
    #pylab.figure()
    #voka.tools.render.draw_comparisons(test_sample, benchmark_samples)
    #pylab.show()


pylab.figure()
for name, result in results.items():
    pylab.plot(locs, result, label=name)

pylab.legend()
pylab.show()
    
