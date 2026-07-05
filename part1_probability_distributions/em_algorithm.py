import csv
import math

# ===Load The Dataset===
heights = []
seen_families = set()

# Read CSV file. Extracting children and fathers.
with open("GaltonFamilies.csv", "r") as file:
    reader = csv.reader(file)
    # We skip the header line
    next(reader)

    for row in reader:
        family_id = row[1]
        father_height = float(row[2])
        child_height = float(row[8])

        # Add the child's height to our dataset
        heights.append(child_height)

        # Only add the father once per family to avoid duplicates
        if family_id not in seen_families:
            heights.append(father_height)
            seen_families.add(family_id)

# Total number of peoplee
N = len(heights)

# === Gaussian Probability Function ===
def calculate_gaussian_prob(x, mean, variance):
    coefficient = 1.0 / math.sqrt(2.0 * math.pi * variance)
    exponent = math.exp(-0.5 * ((x - mean) ** 2) / variance)
    return coefficient * exponent


# === Initialization ===
# We make guesses here
mu1 = 64.0  # Guess for group 1 (children) mean
mu2 = 72.0  # Guess for group 2 (fathers) mean
var1 = 10.0  # guess for group 1 variance (spread)
var2 = 10.0  # guess for group 2 variance (spread)
pi1 = 0.5  # Guess for proportion of group 1
pi2 = 0.5  # Guess for proportion of group 2

# We track the probability of every person

weights1 = [0.0] * N
weights2 = [0.0] * N

