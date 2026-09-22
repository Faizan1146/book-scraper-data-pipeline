import json

with open("books.json","r")as f:
    data = json.load(f)


print(f"Total number of books: {len(data)}")


total= sum(item["price"] for item in data)
avg = total/len(data)
print(f"Avg : {avg:.2f}")


most_expensive = max(data , key=lambda item: item["price"])
print("Most expensive : ",most_expensive['title'], end=" : ")
print(most_expensive['price'],"")


least_expensive = min(data , key=lambda item: item["price"])
print("Least expensive : ",least_expensive['title'], end=" : ")
print(least_expensive['price'],"")

rating = sum(item["rating"] for item in data)
avg_rating= rating/len(data)
print(f"Avg Rating : {avg_rating:.2f}")
