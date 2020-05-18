#!/usr/bin/env python

import numpy
import pylab
import scipy.optimize
import scipy.stats

import voka.metrics.chisq

histograms = dict()
n_histograms = 1000
scale = 1.0
loc = 0.0
size = 1000
params = (size/(scale * numpy.sqrt(2 * numpy.pi)), loc, scale)
for i in range(n_histograms):
    data = numpy.random.normal(size=size, loc=loc, scale=scale)
    histograms['Histogram%d' % i] = numpy.histogram(data)    

def gauss(x, *p):
    A, mu, sigma = p
    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))
    
test_stat = voka.metrics.chisq.NormChiSq()
ndof = None
T_dist = list()
for i in range(n_histograms):
    h = histograms["Histogram%d" % i]
    bin_values = h[0]
    bin_edges = h[1]
    bin_centers = (bin_edges[:-1] + bin_edges[1:])/2    
    bw = bin_centers[1] - bin_centers[0]
    expectation = [gauss(x, bw*params[0], loc, scale) for x in bin_centers]
    
    if not ndof:
        ndof = len(bin_values) - 2
        
    T_dist.append(test_stat(bin_values, expectation))
        
pylab.figure(1)
pylab.hist(T_dist, bins=100)
        
pylab.figure(2)
rv = scipy.stats.chi2(ndof)
x = range(20)
pylab.plot(x, rv.pdf(x), 'k-')

pylab.figure(3)
h = histograms["Histogram0"]
bin_values = h[0]
bin_edges = h[1]
bin_centers = (bin_edges[:-1] + bin_edges[1:])/2    
bw = bin_centers[1] - bin_centers[0]
print("bw = %f" % bw)
pylab.plot(bin_centers, bin_values)
pylab.plot(bin_centers, [gauss(x, bw*params[0], loc, scale) for x in bin_centers])

pylab.show()
    
