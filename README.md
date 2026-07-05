# Probability & Gradient Descent
- Course: Mathematics for ML
- Group: 33
-  Members:
```
Patrick Tuyizere
Agnes Marie Merci Mbabazi
Innocent Tito Muvunyi
Linda Umwali
```
## Table of content
- [Part1: Probability Distributions EM Algorithm](## Part 1: Probability Distributions (EM Algorithm))
- [part2: Bayesian Probability on IMDb Reviews](## Part 2: Bayesian Probability on IMDb Reviews)
- [Part 3: Gradient Descent Manual Calculation](## Part 3: Gradient Descent( Manual calculations))
- [Part 4: Gradient Descent implementation in Code](## Part 4: Gradient Descent(Code Implementation))
- [Repository structure](## Repository structure)

## Part 1: Probability Distributions (EM Algorithm)
We modeled a Parent and Child Heights dataset selection using an expectation-maximization (EM) technique that models the data set as a combination of two Gaussians and applied the algorithm in Python.

### Dataset link: [Link to database](https://www.kaggle.com/datasets/jacopoferretti/parents-heights-vs-children-heights-galton-data)

### EM Optimization Tracking Table

| Iteration | μ₁ (Children) | μ₂ (Pros) | σ₁² | σ₂² | π₁ | π₂ | Log-Likelihood |
|---|---|---|---|---|---|---|---|
| 0 (Init) | [value] | [value] | [value] | [value] | [value] | [value] | [value] |
| 1 | [value] | [value] | [value] | [value] | [value] | [value] | [value] |
| 2 | [value] | [value] | [value] | [value] | [value] | [value] | [value] |

### Why not just split at the global mean?
...

## Part 2: Bayesian Probability on IMDb Reviews
### Chosen keywords
- Positive: [excellent], [amazing], [great]
- Negative: [terrible], [bad], [boring]
- 
- we choose to compute: P(Positive | keyword)

### Result table
...

### implementation
- Implemented in plain Python (no ML libraries) using Bayes' Theorem:
  `P(Positive|keyword) = [P(keyword|Positive) * P(Positive)] / P(keyword)`
- Code entry point: `part2_bayes/filename.py`

## Part 3: Gradient Descent( Manual calculations)

### Steps taken
1. Predicted ŷ using initial m, b (matrix form)
2. Full derivation of ∂J/∂m and ∂J/∂b from the MSE cost function
3. computed four gradient descent updates

### written discussion of the observed trend in m and b
...
See: `part3_manual_calculations/part3_manual_calculations.pdf`

## Part 4: Gradient Descent(Code Implementation)
We converted the manual code from part 3 intto working python code, using SciPy to compute derivatives automatedly rather than by hand/ manual computation.


## Repository structure
```
project-root/
├── README.md
├── part1_probability_distributions/
│   ├── em_algorithm.py
│   └── GaltonFamilies.csv
├── part2_bayesian_probability/
│   └── bayes_probability.py
├── part3_manual_calculations/
│   └── part3_manual_calculations.pdf
├── part4_grad_descent_code/
│   ├── gradient_descent.py
│   └── cost_plot.png
    └── parameters_plot.png
└── notebook/
    └── full_walkthrough.ipynb
```

## Running Part4

1. Clone the repo ``` git clone https://github.com/Linda5-umwali/Bayesian-Probability-Gradient-descent.git ```
2. Run ``` pip install -r requirements.txt ```
3. Run ``` python gradient_descent.py ```