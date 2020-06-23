#!/usr/bin/env python
import unittest
import os

import random
import numpy

import voka.lof

class TestLOF(unittest.TestCase):

    def setUp(self):
        mu = 0.
        sigma = 1.

        self.test_hist = numpy.histogram([random.gauss(mu, sigma) for _ in range(1000)])[0]        
        self.reference_collection = [numpy.histogram([random.gauss(mu, sigma)
                                                      for i in range(1000)])[0]
                                     for j in range(5)]
                
    def test_LOF(self):
        result = voka.lof.LOF(self.test_hist, 3, self.reference_collection)
        self.assertFalse(numpy.isnan(result))
        
if __name__=='__main__':
    unittest.main()

