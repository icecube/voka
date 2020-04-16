# voka
Sanity checks on sequences/histograms using unsupervised machine learning.

# Dependencies

Currently the only dependency is numpy and optionally matplotlib for rendering histograms.

# Abstract
## Continuous Benchmarking HPC Applications using Machine Learning Techniques

High level results of physics simulation chains are often difficult to test using traditional methods (i.e. unit/integration/system tests). This paper presents a technique used by the IceCube Neutrino Observatory in an autonomous system that uses traditional test statistics as inputs to a machine learning algorithm (specifically anomaly/outlier detection algorithm) to achieve broad coverage of its physics software stack, from initial event generation through detector simulation up to high levels of filtering (used to reject background and retain signal).  This paper will show that this technique offers several advantages, and often similar performance, over traditional statistical comparisons, such as Chi^2, Kolmogorov-Smirnoff, Anderson-Darling, log-likelihood, etc... in its broad and generic application.  No prior knowledge, by human observers, of distribution expectations are required.  By autonomously comparing more than 10k distributions, generated at various stages in the simulation, reconstruction, and filtering pipeline, IceCube is able to catch problems earlier and pinpoint problematic commits with minimal human intervention and monitoring.

# Introduction
Nearly all modern HPC applications execute in a distributed system.  Whether the system is a commercial cloud, public grid, or private cluster, application execution represents a significant cost of time, energy, and money.  Continuous Integration (CI) systems have been around for a while as the first stage of code validation.  More recently Continuous Delivery (CD) systems have become more popular, as a means to autonomously deliver validated software.  A new stage in this pipeline is emerging, called Continuous Benchmarking (CB) that attempts to look beyond traditional unit and integration tests common to all CI/CD systems.  No prior knowledge, by human observers, of distribution expectations are required.  Distributions are not required to be mathematically well-behaved, i.e. derived by sampling functions with continuous low-order derivatives.  Distributions are not required to adhere to Poissonian statistics.  Finally, there is no threshold on the sample statistics required.  The technique presented is currently being used by IceCube in a nightly CI/CD/CB system to validate its physics codebase before release and subsequent petabyte-scale mass production.

The method described here was inspired by F. Porter's paper describing various methods to test the consistency of two histograms (https://arxiv.org/abs/0804.0380).

## Advantages
- No prior knowledge of the distribution is required
- No limitation on statistics
- No need to be dominated by Poissonian statistics
- Works on distributions of naturally, human-interpretable metrics (i.e. histograms).

## Basics
<Back of the bar napkin diagram>
