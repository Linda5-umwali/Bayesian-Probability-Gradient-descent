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

