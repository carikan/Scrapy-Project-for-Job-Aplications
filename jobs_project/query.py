# query.py

import os
import sys
import csv


print("Starting query.py...")

# Add the project root path to be able to import from infra/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from infra.mongodb_connector import MongoDBConnector  # ✅ Make sure this file exists and is correct

def export_to_csv(filename="final_jobs.csv"):
    print("📦 Fetching documents from MongoDB...")

    mongo = MongoDBConnector()

    documents = mongo.find_all()  # ✅ This method must exist in your MongoDBConnector

    if not documents:
        print("⚠️ No documents found.")
        return

    rows = [doc.get("data", {}) for doc in documents]

    # Collect all unique keys across all documents to use as CSV headers
    fieldnames = sorted({key for row in rows for key in row.keys()})

    # Save data to CSV file
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Exported {len(rows)} jobs to {filename}")

if __name__ == "__main__":
    export_to_csv()
