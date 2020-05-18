#!/usr/bin/env python

import numpy

import voka.model

test_data = {
    'Gaussian': numpy.random.normal(size=100),
    'Uniform': numpy.random.uniform(size=100)
}

n_benchmark_collections = 5
benchmark_labels = ['Benchmark_%d' % i for i in range(n_benchmark_collections)]
benchmark_data = {
    benchmark_label:{'Gaussian': numpy.random.normal(size=100),
                     'Uniform': numpy.random.uniform(size=100)}
    for benchmark_label in benchmark_labels
}

# histogram the data
test_histograms = {name:numpy.histogram(data)[0] for name, data in test_data.items()}
benchmark_histograms = dict()
for name, bm_data in benchmark_data.items():
    benchmark_histograms[name] = {n:numpy.histogram(data)[0]
                                  for n, data in bm_data.items()}

voka_test = voka.model.Voka()
voka_test.train(benchmark_histograms)
result = voka_test.execute(test_histograms)
print(result)
print(voka_test.results(result))
