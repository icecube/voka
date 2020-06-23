#!/usr/bin/env python3
import unittest
import os

import random
from math import sqrt
from math import isnan

import numpy

import voka.model

class TestVoka(unittest.TestCase):

    def setUp(self):
        mu = 0.
        sigma = 1.

        histogram_names = ["Histogram%d" % i for i in range(100)]
        self.test_hist = dict()
        for name in histogram_names:
            dist = [random.gauss(mu, sigma) for _ in range(1000)]
            self.test_hist[name] = numpy.histogram(dist)[0]

            
        reference_names = ["ReferenceRun%d" % i for i in range(5)]
        self.reference_collection = {name:dict() for name in reference_names}
        for reference_name in reference_names:
            # For each run generate a set of histograms
            # with the same structure and names as the test histograms
            
            for name in histogram_names:
                dist = [random.gauss(mu, sigma) for _ in range(1000)]
                self.reference_collection[reference_name][name] = numpy.histogram(dist)[0]
                           
    def test_voka(self):
        vk = voka.model.Voka()
        vk.train(self.reference_collection)
        result = vk.execute(self.test_hist)
        self.assertTrue(len(result) == 100)

if __name__=='__main__':
    unittest.main()

