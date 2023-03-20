---
title: "Operation Research and transport"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/ROT
venue: "Ecole des Ponts, 1A"
date: 2022-01-01
location: "ENPC, France"
lesson: 2
---

This is a 3rd year course about the use of Operation Research in Transport problem.
The subject being incredibly vast we actually focus on traffic assignement problem : knowing where people want to go, how is everybody going to choose its path, the traffic equilibrate and finally how much traffic jam are we going to observe.

To do so we explore the incredibly simple and somewhat mind bungling Braess's Paradox : in some case suppressing a road actually diminish the travel time for everybody !

On the way we discuss basic game theory (Nash Equilibrium, Prisonner's dilemna, Pareto efficiency), shortest path problem and algorithms (Djikstra's, Bellman's, A*), Wardrop Equilibrium and numerical method to find it (Conditional gradient method a.k.a Franck Wolfe methods).
The course is topped-up by a practical work and various intervention showcasing other transport related operation research problems.

[Handout notes](../files/teaching/ROT/ROT_poly.pdf) [Youtube Playlist](https://www.youtube.com/playlist?list=PLWbSa0uhIdsbox7eHDOVDN1MoUi5TRacG)

### 31/01/23 Urban transportation transport analysis and introduction to game theory

[slides](../files/teaching/ROT/ROT-1.pdf)

- We present the urban transport analysis framework
- We recall the Braess's paradox
- We give essential game theory definitions

### 7/02/23 Shortest Path algorithms

[slides](../files/teaching/ROT/ROT-2.pdf)

- We give essential graph definitions, and define the shortest path problem
- We present three algorithms:
  - Djikstra
  - Bellman
  - A*

### 14/02/23 Wardrop equilibrium and price of anarchy

[slides](../files/teaching/ROT/ROT-3.pdf)

- We recall some optimization background (Convexity, KKT's conditions)
- We introduce the notion of Wardrop user equilibrium
- We show that the user equilibrium can be found as the minimum of a convex optimization problem
- We define and bound the price of anarchy

### 21/02/23 Numerical methods for finding user equilibrium and social optimum

[slides](../files/teaching/ROT/ROT-4.pdf)

We have shown that finding the user equilibrium (or the social optimum) is equivalent to solving a convex optimization problem under polyhedral constraints.
Thus, in this course we study numerical methods to find it.

- Numerical methods for univariate optimization
- Conditional gradient (a.k.a Franck-Wolfe) algorithm
- Application to equilibrium computation and comparison to known heuristics

### 7/03/23 Practical work

[TP](https://gdalle.github.io/ROT-TP/)

### 14/03/23 Other transport related operation research problems

### 04/04/23 Exam
[Exam 2017](../files/teaching/ROT/DS_2017.pdf)
[Exam 2018](../files/teaching/ROT/DS_2018.pdf)
[Exam 2019](../files/teaching/ROT/DS_2019.pdf)
[Exam 2021](../files/teaching/ROT/DS_2021.pdf)