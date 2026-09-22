# Book Scraper & Data Pipeline

A Python web-scraping project that collects book information from Books to Scrape, processes the data, and stores it in multiple formats including JSON, CSV, and SQLite.

## Features

* Scrapes 1,000 books across 50 pages
* Extracts book title, price, rating, and availability
* Handles website pagination automatically
* Cleans and converts scraped data
* Exports data to JSON and CSV
* Stores data in a SQLite database
* Performs SQL-based data analysis
* Finds the most and least expensive books
* Calculates average book price
* Counts books by rating

## Technologies

* Python
* Requests
* BeautifulSoup
* SQLite
* SQL
* JSON
* CSV

## Project Structure

```text
book-scraper-data-pipeline/
│
├── scraper.py
├── analyze_books.py
├── export_csv.py
├── database.py
├── queries.py
├── books.json
├── books.csv
├── books.db
└── README.md
```

## Data Pipeline

```text
Books to Scrape
      ↓
Requests
      ↓
BeautifulSoup
      ↓
Pagination
      ↓
Data Cleaning
      ↓
JSON / CSV
      ↓
SQLite Database
      ↓
SQL Analysis
```

## Database Analysis

The project uses SQL to:

* Count total books
* Find the 10 most expensive books
* Find the 10 cheapest books
* Count 5-star books
* Calculate the average book price

## How to Run

Install the required packages:

```bash
pip install requests beautifulsoup4
```

Run the scraper:

```bash
python scraper.py
```

Analyze the scraped data:

```bash
python analyze_books.py
```

Export the data to CSV:

```bash
python export_csv.py
```

Create the SQLite database:

```bash
python database.py
```

Run SQL queries:

```bash
python queries.py
```

## Skills Demonstrated

This project demonstrates practical experience with:

* Web scraping
* HTML parsing
* Pagination
* Data extraction and cleaning
* File handling
* JSON and CSV processing
* SQLite database management
* SQL queries
* Python automation
* Basic data analysis

## Disclaimer

This project uses the publicly available Books to Scrape website, which is designed for practicing web scraping.

