---
title: "SDDP has polynomial iteration complexity in the horizon"
authors: 'V. Leclère'
collection: publications
category: preprint
permalink: /publication/2026-SDDP-Complexity
excerpt: 'SDDP has polynomial iteration complexity in the horizon'
date: 2026-10-09
venue: ''
paperurl: 'https://optimization-online.org/wp-content/uploads/2026/10/main.pdf'
citation: ''
---
Stochastic dual dynamic programming (SDDP) and its variants are run in practice with forward passes that sample the noise at random. Recent iteration-complexity results favour another choice: when the trial points are selected deterministically, for instance along the scenario with the largest gap, the number of iterations is polynomial in the horizon T, whereas every bound we know of for randomly sampled forward passes is exponential in T. We show that this is not intrinsic to random sampling, for a broad class of trajectory-following dynamic programming algorithms, which includes SDDP, stochastic dual dynamic integer programming and stochastic Lipschitz dynamic programming. With random sampling, and with Lipschitz constants, diameters and per-stage loss ranges bounded independently of the stage and of the horizon, the expected number of iterations whose policy is not Tε-optimal is O(T ε<sup>-(d+1)</sup>), where d is the state dimension: linear in T, as for deterministic selection rules. The proof needs no particular scenario to be sampled: the gap between the expected cost of the current policy and the current lower bound equals the expected sum of one-step Bellman residuals along the sampled path, and Lipschitz cuts that are tight at the visited states turn the positive residuals into permanent increases of a bounded potential. The results extend to noise without finite support, to backward passes on a sample average approximation, and to stationary and periodic infinite-horizon SDDP with geometric pass lengths.
