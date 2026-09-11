---
title: "Decision Focused Scenario Generation for Contextual Two-Stage Stochastic Linear Programming"
authors: 'J. Hornewall, S. Delannoy-Pavy, T. Homem-de-Mello, V. Leclère'
collection: publications
category: proceeding
permalink: /publication/2025-NeurIPS-ScenarioGen
excerpt: 'Decision Focused Scenario Generation for Contextual Two-Stage Stochastic Linear Programming'
date: 2025-12-01
venue: 'NeurIPS 2025 MLxOR workshop'
paperurl: 'https://openreview.net/forum?id=j8BVbta5lg'
citation: ''
---
We present a framework for scenario generation in contextual two-stage stochastic linear programs. A neural network generates scenario sets from context inputs. Rather than learning conditional distributions explicitly, the approach computes first-stage decisions through a log-barrier regularized formulation with efficiently computable derivatives via implicit differentiation. Training minimizes actual downstream costs on observed data without relying on value-function surrogates or differentiation through standard LP solvers. The method learns multi-scenario representations while avoiding high-dimensional density estimation requirements. We detail the mathematical formulation and demonstrate competitive performance with existing approaches, even when trained on small amounts of training data.

[OpenReview](https://openreview.net/forum?id=j8BVbta5lg)
