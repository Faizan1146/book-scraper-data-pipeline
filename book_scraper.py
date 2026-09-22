import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com"
books_data = []
while url:
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    # with open('page.html' , 'w')as f:
    #     f.write(response.text)
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    

    books = soup.find_all('article' , class_="product_pod")
    for book in books:
        h3 = book.find('h3')
        title = h3.find('a')
        price = book.find("p", class_="price_color")
        rating = book.find("p", class_="star-rating")
        rating_value = rating_map[rating["class"][1]]
        availability = book.find("p", class_="instock availability")
        # print(title.text)
        # print(price.text)
        # print(rating_value)
        # print(availability.text.strip(),"\n")
        price = float(price.text.strip().replace("£", ""))

        book_data = {
            "title": title.text.strip(),
            "price": price,
            "rating": rating_value,
            "availability": availability.text.strip()
            }

    
        books_data.append(book_data)
        next_page = soup.find('li',class_='next')
    if next_page:
            href = next_page.find("a")["href"]
            url = urljoin(url, href)
    else:
            url = None
        
        
    # for b in books_data:
    #   print(b)

    
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books_data, f, indent=4)

print(f"Total books scraped: {len(books_data)}")

