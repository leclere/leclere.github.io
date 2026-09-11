---
title: "Primal-dual algorithm for contextual stochastic combinatorial optimization"
authors: 'L. Bouvier, T. Prunet, V. Leclère, A. Parmentier'
collection: publications
category: preprint
permalink: /publication/2025-ContextualCombOpt
excerpt: 'Primal-dual algorithm for contextual stochastic combinatorial optimization'
date: 2025-05-08
venue: ''
paperurl: 'https://arxiv.org/abs/2505.04757'
citation: ''
---
This paper introduces a novel approach to contextual stochastic optimization, integrating operations research and machine learning to address decision-making under uncertainty. Traditional methods often fail to leverage contextual information, which underscores the necessity for new algorithms. In this study, we utilize neural networks with combinatorial optimization layers to encode policies. Our goal is to minimize the empirical cost, which is estimated from past data on uncertain parameters and contexts. To that end, we present a surrogate learning problem and a generic primal-dual algorithm that is applicable to various combinatorial settings in stochastic optimization. Our approach extends classic Fenchel-Young loss results and introduces a new regularization method using sparse perturbations on the distribution simplex. This allows for tractable updates in the original space and can accommodate diverse objective functions. We establish sublinear convergence for the exact linear-parametric version and provide a bound on the non-optimality of the resulting policy in terms of the empirical cost. Experiments on three contextual stochastic optimization problems show that our algorithm is efficient and scalable, achieving performance comparable to state-of-the-art baselines with significantly reduced computational requirements.

[arXiv:2505.04757](https://arxiv.org/abs/2505.04757)
