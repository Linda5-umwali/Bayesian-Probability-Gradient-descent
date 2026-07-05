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

