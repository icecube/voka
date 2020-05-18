#!/usr/bin/env python

import numpy
import pylab
import scipy.optimize

# Histogram the arrival time, expected to be gaussian, of the charge
# sampled from a gaussian.
data = list()
pe_time_dist = numpy.random.normal(size=1000)
for time in pe_time_dist:
    # for each time the charge is sampled from
    # another distribution
    charge = numpy.random.normal(loc=5.0, scale=0.25)
    for c in range(int(charge)):
        data.append(time)

def gauss(x, *p):
    A, mu, sigma = p
    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))

hist, bin_edges = numpy.histogram(data)
bin_centers = (bin_edges[:-1] + bin_edges[1:])/2
p0 = [1000., 0., 1.]
p1 = [1000., 0., 1.]
print(hist)
print(bin_centers)
coeff, var_matrix = scipy.optimize.curve_fit(gauss, bin_centers, hist, p0=p1)

print('Fitted amplitude = %f' % coeff[0])
print('Fitted mean = %f' % coeff[1])
print('Fitted standard deviation = %f' % coeff[2])

hist_fit = gauss(bin_centers, *coeff)
pylab.hist(data)
pylab.plot(bin_centers, gauss(bin_centers, *p0), label='Initial')
pylab.plot(bin_centers, hist_fit, label='Fitted data')

pylab.show()
    
