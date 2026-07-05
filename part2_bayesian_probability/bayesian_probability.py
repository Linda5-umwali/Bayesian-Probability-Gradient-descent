import csv

total_reviews = 0
positive_reviews = 0
dataset = []

with open("IMDB Dataset.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert text to lowercase so that our keyword search is not case sensitive
        review_text = row["review"].lower()
        sentiment = row["sentiment"].lower()

        # Save to our dataset list
        dataset.append({"text": review_text, "sentiment": sentiment})

        # Increment our counters
        total_reviews += 1
        if sentiment == "positive":
            positive_reviews += 1

# We define keywords
keywords = ["excellent", "amazing", "great", "terrible", "bad", "boring"]

# Calculate Prior: P(Positive)
p_positive = positive_reviews / total_reviews
print(f"Prior P(Positive): {p_positive * 100:.2f}%\n")

# Loop througheach keyword to calculate Bayes Theorem
for keyword in keywords:
    keyword_total_count = 0
    keyword_in_positive_count = 0

    # Scan through every review in the saved dataset
    for item in dataset:
        if keyword in item["text"]:
            keyword_total_count += 1
            if item["sentiment"] == "positive":
                keyword_in_positive_count += 1
                
# Marginal: P(keyword) - Probability that ANy review has the keyword
    p_keyword = keyword_total_count / total_reviews

    # Likelihood: P(keyword | positive) - Probability a positive review has the keyword
    if positive_reviews > 0:
        p_keyword_given_positive = keyword_in_positive_count / positive_reviews
    else:
        p_keyword_given_positive = 0

