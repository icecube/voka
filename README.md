# voka
Sanity checks on histograms using unsupervised machine learning.

## Problem Statement
Let's say you have a large number of histograms produced by a complex system (e.g. scientific simulation chain 
for a large-scale physics experiment) and you want to compare one large set of histograms to another to determine 
differences.  When the number of histograms becomes large (>100) it can be difficult for human observers to 
efficiently scan them for subtle differences buried in statistical flucuations.  The project is a tool that
can help detect those differences.

# Dependencies

* numpy
* matplotlib
* scipy (optional)

```
   numpy (basic_example,classic_fit_example,standard_distribution_comparisons,stochastic_example,test.test_lof,test.test_metrics,test.test_voka,vanilla_gaussian,voka.lof)
    pylab (classic_fit_example,standard_distribution_comparisons,stochastic_example,vanilla_gaussian)
    scipy 
      \-optimize (classic_fit_example,standard_distribution_comparisons,stochastic_example,vanilla_gaussian)
      \-special (voka.metrics.llh)
      \-stats (standard_distribution_comparisons,stochastic_example,vanilla_gaussian)
    voka 
      \-compare (test.test_metrics)
      \-lof (test.test_lof)
      \-metrics 
      | \-ad (test.test_metrics)
      | \-bdm (test.test_metrics)
      | \-chisq (standard_distribution_comparisons,stochastic_example,test.test_metrics,vanilla_gaussian)
      | \-cvm (test.test_metrics)
      | \-ks (test.test_metrics)
      | \-llh (test.test_metrics)
      \-model (basic_example,test.test_voka)

```


# Test Coverage

As of June 23rd, 2020:
```
Name                       Stmts   Miss  Cover
----------------------------------------------
voka/__init__.py               0      0   100%
voka/compare.py               16      2    88%
voka/lof.py                   20      0   100%
voka/metrics/__init__.py       0      0   100%
voka/metrics/ad.py            29      2    93%
voka/metrics/bdm.py           13      1    92%
voka/metrics/chisq.py         21      4    81%
voka/metrics/cvm.py           19      1    95%
voka/metrics/ks.py            12      1    92%
voka/metrics/llh.py           47     10    79%
voka/model.py                 30      4    87%
----------------------------------------------
TOTAL                        207     25    88%
```

## Running Tests
```sh
$ python3 -m unittest
$ coverage run --source=voka -m unittest
$ coverage report -m
```

# Introduction
Nearly all modern HPC applications execute in a distributed system.  Whether the system is a commercial cloud, public grid, 
or private cluster, application execution represents a significant cost of time, energy, and money.  Continuous Integration 
(CI) systems have been around for a while as the first stage of code validation.  More recently Continuous Delivery (CD) 
ystems have become more popular, as a means to autonomously deliver validated software.  A new stage in this pipeline is 
emerging, called Continuous Benchmarking (CB) that attempts to look beyond traditional unit and integration tests common 
to all CI/CD systems.  The technique presented is currently being used by IceCube in a nightly CI/CD/CB/CV system to validate 
its physics codebase before release and subsequent petabyte-scale mass production.

The method described here was inspired by F. Porter's paper[1] describing various methods to test the consistency of two 
histograms and can be considered an extension, where instead of asking whether two histograms are consistent, we ask 
whether one test histogram is consistent with an ensemble of N benchmark histograms.

## Advantages
- No prior detailed knowledge of the distribution is required.
- No restrictions on the continuity of derivatives of the underlying distribution.
- No limitation on statistics.  Works the same for 0, low, and high statistics samples.
- No need to be dominated by Poissonian statistics.
- Works on distributions of naturally, human-interpretable metrics (i.e. histograms).

## Difficulty with Traditional Methods
The chi^2 distribution between two histograms doesn't follow a chi^2 distribution.  It has long tails.  Can't easily 
derive a p-value from it using standard tools.  Necessary to empirically determine the test statistic distribution for 
each physical distribution, which is impractical.  Fitting has the same problem[3].  It's impractical and often 
istributions don't easily fit analytic functions since there's no guarantee they're sampled from a function with 
continuous first derivatives.

In practice, physical distributions are not guaranteed to be Poissonian [2].  IceCube has non-Poissonian noise [?].

## Basics
The method presented here uses traditional test statistics, such as Chi^2, KS, AD, as inputs to an outlier detection 
algorithm (specifically calculating a Local Outlier Factor) to determine whether the test histogram is consistent 
with the benchmark ensemble.

### Getting Started

# References
- [1] F. Porter "Testing the Consistency of Two Histograms" (https://arxiv.org/abs/0804.0380) 
- [2] G. Cowen "Statistical Data Analysis"
- [3] The IceCube Collaboration "In-situ calibration of the single-photoelectron charge response of the IceCube photomultiplier tubes" (https://arxiv.org/abs/2002.00997)
- [4] M. Dunsch, J. Soedinggresko, A. Sandrock, M. Meier, T. Menne, W. Rhode "Recent Improvements for the Lepton Propagator PROPOSAL" (https://arxiv.org/abs/1809.07740)
