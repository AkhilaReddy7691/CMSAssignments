import requests
import pandas as pd
from bs4 import BeautifulSoup
import http.server
import socketserver
import os

def scrape_books():
    print("Starting book scraping...")
    url = "http://books.toscrape.com"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    books_data = []
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()

        books_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    df = pd.DataFrame(books_data)
    df.to_csv("scraped_books.csv", index=False)
    print("Scraping completed! Data saved to scraped_books.csv")

# Scrape the books
scrape_books()

# Serve the directory via HTTP
PORT = 8000
os.chdir(".")
Handler = http.server.SimpleHTTPRequestHandler

print("Starting HTTP server on port 8000...")
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
