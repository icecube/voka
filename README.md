# voka
Sanity checks on sequences/histograms using unsupervised machine learning.

# Dependencies

Currently the only dependency is numpy and optionally matplotlib for rendering histograms.

# Abstract
## Continuous Benchmarking HPC Applications using Machine Learning Techniques

High level results of physics simulation chains are often difficult to test using traditional methods (i.e. unit/integration/system tests). This paper presents a technique used by the IceCube Neutrino Observatory in an autonomous system that uses traditional test statistics as inputs to a machine learning algorithm (specifically anomaly/outlier detection algorithm) to achieve broad coverage of its physics software stack, from initial event generation through detector simulation up to high levels of filtering (used to reject background and retain signal).  This paper will show that this technique offers several advantages, and often similar performance, over traditional statistical comparisons, such as $\chi^{2}$, Kolmogorov-Smirnoff, Anderson-Darling, log-likelihood, etc... in its broad and generic application.  No prior knowledge, by human observers, of distribution expectations are required.  By autonomously comparing more than 10k distributions, generated at various stages in the simulation, reconstruction, and filtering pipeline, IceCube is able to catch problems earlier and pinpoint problematic commits with minimal human intervention and monitoring.

# Introduction
Nearly all modern HPC applications execute in a distributed system.  Whether the system is a commercial cloud, public grid, or private cluster, application execution represents a significant cost of time, energy, and money.  Continuous Integration (CI) systems have been around for a while as the first stage of code validation.  More recently Continuous Delivery (CD) systems have become more popular, as a means to autonomously deliver validated software.  A new stage in this pipeline is emerging, called Continuous Benchmarking (CB) that attempts to look beyond traditional unit and integration tests common to all CI/CD systems.  No prior knowledge, by human observers, of distribution expectations are required.  Distributions are not required to be mathematically well-behaved, i.e. derived by sampling functions with continuous low-order derivatives.  Distributions are not required to adhere to Poissonian statistics.  Finally, there is no threshold on the sample statistics required.  The technique presented is currently being used by IceCube in a nightly CI/CD/CB system to validate its physics codebase before release and subsequent petabyte-scale mass production.

The method described here was inspired by F. Porter's paper[1] describing various methods to test the consistency of two histograms and can be considered an extension, where instead of asking whether two histograms are consistent, we ask whether one test histogram is consistent with an ensemble of N benchmark histograms.

## Advantages
- No prior detailed knowledge of the distribution is required.
- No restrictions on the continuity of derivatives of the underlying distribution.
- No limitation on statistics.  Works the same for 0, low, and high statistics samples.
- No need to be dominated by Poissonian statistics.
- Works on distributions of naturally, human-interpretable metrics (i.e. histograms).

## Difficulty with Traditional Methods
The chi^2 distribution between two histograms doesn't follow a chi^2 distribution.  It has long tails.  Can't easily derive a p-value from it using standard tools.  Necessary to empirically determine the test statistic distribution for each physical distribution, which is impractical.  Fitting has the same problem[3].  It's impractical and often distributions don't easily fit analytic functions since there's no guarantee they're sampled from a function with continuous first derivatives.

In practice, physical distributions are not guaranteed to be Poissonian [2].  IceCube has non-Poissonian noise [?].

## Basics
The method presented here uses traditional test statistics, such as Chi^2, KS, AD, as inputs to an outlier detection algorithm (specifically calculating a Local Outlier Factor) to determine whether the test histogram is consistent with the benchmark ensemble.

## Results

## Conclusion

# References
[1] F. Porter "Testing the Consistency of Two Histograms" (https://arxiv.org/abs/0804.0380) 
[2] G. Cowen "Statistical Data Analysis"
[3] The IceCube Collaboration "In-situ calibration of the single-photoelectron charge response of the IceCube photomultiplier tubes" (https://arxiv.org/abs/2002.00997)
[4] M. Dunsch, J. Soedinggresko, A. Sandrock, M. Meier, T. Menne, W. Rhode "Recent Improvements for the Lepton Propagator PROPOSAL" (https://arxiv.org/abs/1809.07740)
