---
title: "Solver-Free Decision-Focused Learning via Barrier Coordinate Cost Prediction"
authors: 'J. Hornewall, V. Leclère'
collection: publications
category: proceeding
permalink: /publication/2026-NeurIPS-SolverFreeDFL
excerpt: 'Solver-Free Decision-Focused Learning via Barrier Coordinate Cost Prediction'
date: 2026-12-01
venue: 'NeurIPS 2026 MLxOR workshop'
paperurl: 'https://openreview.net/pdf?id=TUCwq9yjCm'
citation: ''
---
Decision-focused learning (DFL) trains predictions for the quality of the decisions they induce, but leading methods repeatedly invoke an optimizer during training. We introduce barrier cost recovery (BCR), a novel, ultra-fast, solver-free method for decision-focused cost prediction based on log-barrier gradient transforms, and demonstrate its performance on a broad family of benchmarks. A neural network learns an interior policy for a log-barrier-smoothed LP through a fast feasibility chart from constrained machine learning. The negative barrier gradient then transforms that policy into a decision-focused cost prediction, which an exact solve of the original LP or MIP deploys as a hard decision. For every positive barrier weight, BCR is decision Fisher consistent, and its excess surrogate risk is exactly a scaled barrier Bregman divergence. A closed-form prediction correction combines this decision coordinate with an MSE head to produce a physical-cost forecast without changing any hard decision. Across the tested LP and MIP benchmarks, BCR achieves materially lower regret than SPO+ and MSE on most instances, together with an order-of-magnitude mean training-time speedup over PyEPO SPO+ across the recorded instances.

[OpenReview](https://openreview.net/pdf?id=TUCwq9yjCm)
