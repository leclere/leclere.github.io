---
title: "Efficient smoothed concomitant lasso estimation for high dimensional regression"
authors:'E. Ndiaye, O. Fercoq, A. Gramfort, V. Leclère, J. Salmon'
collection: publications
category: published
permalink: /publication/2017-Lasso
excerpt: 'Safe screen rules for square-root lasso'
date: 2017-10-01
venue: 'Journal of Physics: Conference Series'
paperurl: 'https://iopscience.iop.org/article/10.1088/1742-6596/904/1/012006/pdf'
citation: 'Ndiaye, Eugene, et al. "Efficient smoothed concomitant lasso estimation for high dimensional regression." Journal of Physics: Conference Series. Vol. 904. No. 1. IOP Publishing, 2017.'
---
In high dimensional settings, sparse structures are crucial for efficiency, both in term of
memory, computation and performance. It is customary to consider `1 penalty to enforce
sparsity in such scenarios. Sparsity enforcing methods, the Lasso being a canonical example,
are popular candidates to address high dimension. For efficiency, they rely on tuning a parameter
trading data fitting versus sparsity. For the Lasso theory to hold this tuning parameter should
be proportional to the noise level, yet the latter is often unknown in practice. A possible remedy
is to jointly optimize over the regression parameter as well as over the noise level. This has been
considered under several names in the literature: Scaled-Lasso, Square-root Lasso, Concomitant
Lasso estimation for instance, and could be of interest for uncertainty quantification. In this
work, after illustrating numerical difficulties for the Concomitant Lasso formulation, we propose
a modification we coined Smoothed Concomitant Lasso, aimed at increasing numerical stability.
We propose an efficient and accurate solver leading to a computational cost no more expensive
than the one for the Lasso. We leverage on standard ingredients behind the success of fast
Lasso solvers: a coordinate descent algorithm, combined with safe screening rules to achieve
speed efficiency, by eliminating early irrelevant features.

[Download paper here](../files/papers/2017-lasso.pdf)

