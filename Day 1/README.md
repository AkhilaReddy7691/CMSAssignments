###DOCKER

##BOOK SCRAPER & HTTP SERVER (Dockerized)

This project scrapes book data from books.toscrape.com, saves it into a CSV file, and serves the output via a simple HTTP server — all containerized using Docker.

---

##PROJECT STRUCTURE

├── Dockerfile
├── README.md
├── webscrapping.py
├── scraped_books.csv (generated after running)

---

##FEATURES

Scrapes title, price, and availability of books.

Saves data into scraped_books.csv.

Starts a simple HTTP server to serve the files.

Fully containerized with Docker.

---

##Prerequisites

Before you begin, ensure you have Docker installed:
Download Docker

---

##How to Build and Run

1.Clone the repository / place files in a directory:

2.Build the Docker image:

docker build -t book-scraper .

3.Run the container:

docker run -p 8000:8000 book-scraper

Access the results:

Open your browser and go to: http://localhost:8000/scraped_books.csv

---

##Inside the Script (webscrapping.py)

Scrapes the first page of books.

Extracts:
Title
Price
Availability

Saves the result as scraped_books.csv.

Starts a local HTTP server to expose the file.

---

##Dockerfile Summary

The Dockerfile:

Uses Python 3 base image.

Installs necessary libraries (requests, beautifulsoup4, pandas).

Copies the script and runs it.

Starts an HTTP server on port 8000.


