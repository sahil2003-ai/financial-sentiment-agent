import csv
import os

FILE_NAME = "data.csv"

def save_result(text, sentiment, confidence):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["text", "sentiment", "confidence"])

        writer.writerow([text, sentiment, confidence])