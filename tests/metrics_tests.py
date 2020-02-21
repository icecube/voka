#!/usr/bin/env python
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import random
from math import sqrt
from math import isnan

import numpy

import voka.compare
import voka.metrics.chisq 
import voka.metrics.ad
import voka.metrics.ks
import voka.metrics.cvm
import voka.metrics.bdm
import voka.metrics.llh
import voka.compare

class TestMetrics(unittest.TestCase):

    def setUp(self):
        mu = 0.
        sigma = 1.

        h1 = numpy.histogram([random.gauss(mu, sigma) for _ in range(1000)])
        h2 = numpy.histogram([random.gauss(mu, sigma) for _ in range(1000)])
        
        self.gaussian1 = h1[0]
        self.gaussian2 = h2[0]
        
    def test_all(self):
        for m in voka.compare.all_metrics:
            result = m(self.gaussian1, self.gaussian2)
            self.assertFalse(isnan(result))

    def test_default_compare(self):
        result = voka.compare.compare(self.gaussian1, self.gaussian2)
        self.assertEqual(len(result), 2)
        self.assertTrue('AndersonDarling' in result)
        self.assertTrue('ShapeChiSq' in result)
        
unittest.main()

