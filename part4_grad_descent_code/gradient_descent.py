import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import approx_fprime


# 1. Setup and Data Initialization
# Input features (X) and Target values (Y)
X = np.array([[1, 3], [4, 10]])
Y = np.array([[5], [6]])


# Initial parameters
m = np.array([[-1.0], [2.0]])
b = np.array([[1.0], [1.0]])


# Hyperparameters matching our manual calculations
alpha = 0.01
iterations = 4


# Lists to store history for plotting later
m1_history, m2_history = [m[0,0]], [m[1,0]]
b1_history, b2_history = [b[0,0]], [b[1,0]]
cost_history = []

# 2. Derivative Function
def calculate_cost_equation(params, X, Y):
    m_temp = params[0:2].reshape(2, 1)
    b_temp = params[2:4].reshape(2, 1)
    predictions = np.dot(X, m_temp) + b_temp
    error = predictions - Y
    return 0.5 * np.sum(error**2)


def compute_derivative_scipy(equation, current_params, X, Y):
    # epsilon is the tiny step size used to estimate the slope
    epsilon = np.sqrt(np.finfo(float).eps)
    gradient = approx_fprime(current_params, equation, epsilon, X, Y)
    return gradient


# Example of the SciPy derivative in action (evaluating the initial state):
initial_params = np.array([-1.0, 2.0, 1.0, 1.0])
scipy_grad = compute_derivative_scipy(calculate_cost_equation, initial_params, X, Y)
print(f"SciPy Numerical Gradient at Step 0: {scipy_grad}\n")
print("-" * 50)
