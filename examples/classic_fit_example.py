#!/usr/bin/env python

'''
Example illustrating the classic method, meaning fitting by hand.
'''

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
    '''
    The gaussian distribution.
    '''
    amplitude, mean, sigma = p
    return amplitude*numpy.exp(-(x-mean)**2/(2.*sigma**2))

hist, bin_edges = numpy.histogram(data)
bin_centers = (bin_edges[:-1] + bin_edges[1:])/2
p0 = [1000., 0., 1.]
p1 = [1000., 0., 1.]
print(hist)
print(bin_centers)

result = scipy.optimize.curve_fit(gauss, bin_centers, hist, p0=p1)
fitted_amplitude = result[0]
fitted_mean = result[1]
fitted_std_dev = result[2]

print('Fitted amplitude = %f' % fitted_amplitude)
print('Fitted mean = %f' % fitted_mean)
print('Fitted standard deviation = %f' % fitted_std_dev)

coeff = tuple(result[:3])
hist_fit = gauss(bin_centers, *coeff)
pylab.hist(data)
pylab.plot(bin_centers, gauss(bin_centers, *p0), label='Initial')
pylab.plot(bin_centers, hist_fit, label='Fitted data')

pylab.show()
