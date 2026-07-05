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
- Part1: Probability Distributions EM Algorithm
- part2: Bayesian Probability on IMDb Reviews
- Part 3: Gradient Descent Manual Calculation
- Part 4: Gradient Descent implementation in Code
- Repository structure

## Part 1: Probability Distributions (EM Algorithm)
We modeled a Parent and Child Heights dataset selection using an expectation-maximization (EM) technique that models the data set as a combination of two Gaussians and applied the algorithm in Python.

- Dataset link: [Link to database](https://www.kaggle.com/datasets/jacopoferretti/parents-heights-vs-children-heights-galton-data)

### Why not just split at the global mean?
...

## Part 2: Bayesian Probability on IMDb Reviews
- Database link: [linkto Database](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
### Chosen keywords
- Positive: [excellent], [amazing], [great]
- Negative: [terrible], [bad], [boring]
- we choose to compute: P(Positive | keyword)

### Result table
...

### implementation
- Implemented in plain Python (no ML libraries) using Bayes' Theorem:
  `P(Positive|keyword) = [P(keyword|Positive) * P(Positive)] / P(keyword)`
- Code entry point: `part2_bayesian_probability/bayesian_probability.py`

## Part 3: Gradient Descent( Manual calculations)

### Steps taken
1. Predicted ŷ using initial m, b (matrix form)
2. Full derivation of ∂J/∂m and ∂J/∂b from the MSE cost function
3. computed four gradient descent updates

### written discussion of the observed trend in m and b
Through all iterations, the cost function went down very rapidly from 61.0 to 2.16, however, the decreasing speed became slower at each stage(from 6.5 to 2.5 to 2.16). This demonstrates that gradient descent worked correctly(large, fast improvement early on when far from the minimum, followed by smaller refinements as the model gets closer to the optimal parameters). The bias b increased steadily and smoothly during all the iterations, which means it tended to reach its optimal value straightly. The behaviour of m1 and m2 was different. While m1 converged almost immediately, m2 first reached a larger than optimal value at iteration 1, then oscillated and started converging slowly after this point. This indicates that the learning rate is adequate for these parameters but is not tuned well enough.
The values are still showing convergence and not divergence trends as the error keeps reducing each time.

See: [manual calculations pdf](https://github.com/Linda5-umwali/Bayesian-Probability-Gradient-descent/blob/main/part3_grad_descent_manual_calculation/Part3%20G33.pdf)

## Part 4: Gradient Descent(Code Implementation)
We converted the manual code from part 3 into working python code, using SciPy to compute derivatives automatedly rather than by hand/ manual computation.


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
