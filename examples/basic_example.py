#!/usr/bin/env python

import numpy
import pylab

import voka.voight_kampff

# This represents a collection of histograms
collection_template = {'Gaussian': None,
                       'Poisson': None}

test_data = {'Gaussian': numpy.random.normal(size=100),
             'Uniform': numpy.random.uniform(size=100)}

n_benchmark_collections = 5
benchmark_names = ['Benchmark_%d' % i for i in range(n_benchmark_collections)]
benchmark_data = dict()
for benchmark_name in benchmark_names:
    benchmark_data[benchmark_name] = {'Gaussian': numpy.random.normal(size=100),
                                      'Uniform': numpy.random.uniform(size=100)}


# histogram the data
test_histograms = {name:numpy.histogram(data)[0] for name, data in test_data.items()}
benchmark_histograms = dict()
for name, bm_data in benchmark_data.items():
    benchmark_histograms[name] = {n:numpy.histogram(data)[0]
                                  for n, data in bm_data.items()}

voka_test = voka.voight_kampff.VoightKampff()
voka_test.determine_parameters(benchmark_histograms)
test_result = voka_test.go(test_histograms)
print(test_result)
print(voka_test.calculate_results(test_result))
