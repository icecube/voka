#!/usr/bin/env python

import collections

import numpy
import pylab
import scipy.optimize
import scipy.stats

import voka.metrics.chisq

# This example illustrates the failure of traditional statistical
# comparisons, such as chi^2, for weighted histograms from
# stochastic processes.  Can't rely on the p-value calculated
# from standard tools such as scipy even in this simple example.

# Histogram the arrival time, expected to be gaussian, of the charge
# sampled from a gaussian.

histograms = dict()
n_histograms = 1000
bins=50
size=1000
for i in range(n_histograms):
    data = numpy.random.uniform(low=-5, high=5, size=size)
    histograms['Uniform%d' % i] = numpy.histogram(data, bins=bins)

    data = numpy.random.chisquare(df=5, size=size)
    histograms['ChiSq5%d' % i] = numpy.histogram(data, bins=bins)
    
    data = numpy.random.normal(size=size)
    histograms['Gaussian%d' % i] = numpy.histogram(data, bins=bins)
    
    data = numpy.random.normal(size=int(size/2), loc=-1, scale = 0.25) + numpy.random.normal(size=int(size/2), loc=1, scale = 0.25)
    histograms['BiGaussian%d' % i] = numpy.histogram(data, bins=bins)
    
    data = numpy.random.exponential(scale=10, size=1000)
    histograms['Exponential%d' % i] = numpy.histogram(data, bins=bins)    

T_dist = collections.defaultdict(list)
test_stat = voka.metrics.chisq.NormChiSq()
for i in range(n_histograms):
    for j in range(i+1, n_histograms):
        h1 = histograms["Uniform%d" % i][0]
        h2 = histograms["Uniform%d" % j][0]        
        T_dist['uniform'].append(test_stat(h1, h2))

        h1 = histograms["ChiSq5%d" % i][0]
        h2 = histograms["ChiSq5%d" % j][0]        
        T_dist['chisq'].append(test_stat(h1, h2))
        
        h1 = histograms["Exponential%d" % i][0]
        h2 = histograms["Exponential%d" % j][0]        
        T_dist['exponential'].append(test_stat(h1, h2))
        
        h1 = histograms["Gaussian%d" % i][0]
        h2 = histograms["Gaussian%d" % j][0]        
        T_dist['gaussian'].append(test_stat(h1, h2))

        h1 = histograms["BiGaussian%d" % i][0]
        h2 = histograms["BiGaussian%d" % j][0]        
        T_dist['bigaussian'].append(test_stat(h1, h2))
        
pylab.figure(1)
pylab.subplot(231)
pylab.title(r'$\chi^{2}$ Test Statistic Distribution - Uniform')
pylab.xlabel(r'$\chi^{2}$')
pylab.ylabel('Probability Density')
bin_values, bin_edges, patches = pylab.hist(T_dist['uniform'], density=True, range=(0,200), bins=100)
x = range(0, int(bin_edges[-1]))
for ndof in range(10, 60, 10):
    rv = scipy.stats.chi2(ndof)
    pylab.plot(x, rv.pdf(x), label='NDOF=%d' % ndof)    
pylab.legend()

pylab.subplot(232)
pylab.title(r'$\chi^{2}$ Test Statistic Distribution - ChiSq')
pylab.xlabel(r'$\chi^{2}$')
pylab.ylabel('Probability Density')
bin_values, bin_edges, patches = pylab.hist(T_dist['chisq'], density=True, range=(0,200), bins=100)
x = range(0, int(bin_edges[-1]))
for ndof in range(10, 60, 10):
    rv = scipy.stats.chi2(ndof)
    pylab.plot(x, rv.pdf(x), label='NDOF=%d' % ndof)    
pylab.legend()

pylab.subplot(233)
pylab.title(r'$\chi^{2}$ Test Statistic Distribution - Gaussian')
pylab.xlabel(r'$\chi^{2}$')
pylab.ylabel('Probability Density')
bin_values, bin_edges, patches = pylab.hist(T_dist['gaussian'], density=True, range=(0,200), bins=100)
x = range(0, int(bin_edges[-1]))
for ndof in range(10, 60, 10):
    rv = scipy.stats.chi2(ndof)
    pylab.plot(x, rv.pdf(x), label='NDOF=%d' % ndof)    
pylab.legend()

pylab.subplot(234)
pylab.title(r'$\chi^{2}$ Test Statistic Distribution - Exponential')
pylab.xlabel(r'$\chi^{2}$')
pylab.ylabel('Probability Density')
bin_values, bin_edges, patches = pylab.hist(T_dist['exponential'], density=True, range=(0,200), bins=100)
x = range(0, int(bin_edges[-1]))
for ndof in range(10, 60, 10):
    rv = scipy.stats.chi2(ndof)
    pylab.plot(x, rv.pdf(x), label='NDOF=%d' % ndof)    
pylab.legend()

pylab.subplot(235)
pylab.title(r'$\chi^{2}$ Test Statistic Distribution - BiGaussian')
pylab.xlabel(r'$\chi^{2}$')
pylab.ylabel('Probability Density')
bin_values, bin_edges, patches = pylab.hist(T_dist['bigaussian'], density=True, range=(0,200), bins=100)
x = range(0, int(bin_edges[-1]))
for ndof in range(10, 60, 10):
    rv = scipy.stats.chi2(ndof)
    pylab.plot(x, rv.pdf(x), label='NDOF=%d' % ndof)    
pylab.legend()

pylab.subplot(236)
pylab.title(r'$\chi^{2}$ Test Statistic Distributions')
pylab.xlabel(r'$\chi^{2}$')
pylab.ylabel('Probability Density')
pylab.hist(T_dist['uniform'], histtype='step', label='Uniform', density=True, range=(0,200), bins=100)
pylab.hist(T_dist['bigaussian'], histtype='step',label='BiGaussian', density=True, range=(0,200), bins=100)
pylab.hist(T_dist['gaussian'], histtype='step',label='Gaussian', density=True, range=(0,200), bins=100)
pylab.hist(T_dist['exponential'], histtype='step',label='Exponential', density=True, range=(0,200), bins=100)
pylab.hist(T_dist['chisq'], histtype='step',label='ChisSq', density=True, range=(0,200), bins=100)
pylab.legend()

pylab.show()
    
