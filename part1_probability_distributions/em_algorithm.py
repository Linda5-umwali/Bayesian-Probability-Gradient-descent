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

print(
    "Iteration | mu1 (Children) | mu2 (Fathers) | var1 | var2 | pi1 | pi2 | Log-Likelihood"
)
print("-" * 85)

# The measure of how small a log-likelihood change counts as 'converged'
tolerance = 1e-8
# The last calculated log-likelihood
previous_log_likelihood = None
# Maximum cap to infinite loops
max_iterations = 100

# === The Algorithm Loop ===
for iteration in range(max_iterations):
    log_likelihood = 0.0

    # === The E-Step (Expectation) ===
    for i in range(N):
        x = heights[i]

        # Calculate raw probabilities using the guesses we made
        prob_is_group1 = pi1 * calculate_gaussian_prob(x, mu1, var1)
        prob_is_group2 = pi2 * calculate_gaussian_prob(x, mu2, var2)

        total_prob = prob_is_group1 + prob_is_group2

        # Calculate log-likelihood to track how well our model fits the data
        log_likelihood += math.log(total_prob)

        # Normalize so weights add up to 1 (e.g., 80% Child, 20% Pro)
        weights1[i] = prob_is_group1 / total_prob
        weights2[i] = prob_is_group2 / total_prob

    # print current state
    print(
        f"{iteration:9} | {mu1:14.2f} | {mu2:10.2f} | {var1:4.2f} | {var2:4.2f} | {pi1:3.2f} | {pi2:3.2f} | {log_likelihood:.2f}"
    )

    # === Convergence Check ===
    if previous_log_likelihood is not None:
        change = abs(log_likelihood - previous_log_likelihood)
        if change < tolerance:
            print(f"\n Converged after {iteration} iterations.")
            break
    previous_log_likelihood = log_likelihood

