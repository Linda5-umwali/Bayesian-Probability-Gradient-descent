# Probability Distributions, Bayesian Probability, and Gradient Descent Implementation
### Course: Mathematics for ML
### Group: 33
### Members:
```
```
## Table of content
- Part1: Probability Distributions EM Algorithm
- part2: Bayesian Probability on IMDb Reviews
- Part 3: Gradient Descent Manual Calculation
- Part 4: Gradient Descent implementation in Code

## Part 1: Probability Distributions (EM Algorithm)
We modeled a Parent and Child Heights dataset selection using an expectation-maximization (EM) technique that models the data set as a combination of two Gaussians and applied the algorithm in Python.

### Dataset link: [https://www.kaggle.com/datasets/jacopoferretti/parents-heights-vs-children-heights-galton-data]

### EM Optimization Tracking Table

| Iteration | μ₁ (Children) | μ₂ (Pros) | σ₁² | σ₂² | π₁ | π₂ | Log-Likelihood |
|---|---|---|---|---|---|---|---|
| 0 (Init) | [value] | [value] | [value] | [value] | [value] | [value] | [value] |
| 1 | [value] | [value] | [value] | [value] | [value] | [value] | [value] |
| 2 | [value] | [value] | [value] | [value] | [value] | [value] | [value] |

### Why not just split at the global mean?
