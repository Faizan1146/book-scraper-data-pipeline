import json
import csv


with open("books.json","r")as f:
    data = json.load(f)

headers = ["title","price","rating","availability"]
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print(f"Exported {len(data)} books to books.csv")