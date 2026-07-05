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
