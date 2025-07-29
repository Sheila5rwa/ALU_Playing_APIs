#!/usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

load_dotenv("config.env")

api_key = os.getenv("GOOGLE_BOOK_API")

def get_books(domain):
    """Fetches book information from Google Books API based on the given domain."""
    
    api_url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{domain}&key={api_key}"
    response = requests.get(url=api_url, timeout=10)

    if response.status_code != 200:
        print(response.status_code, response.text)

    data = response.json()["items"]
    title = [item["volumeInfo"].get("title", "No title") for item in data]
    author_names = [item["volumeInfo"].get("authors", ["Unknown Author"]) for item in data]
    publisher = [item["volumeInfo"].get("publisher", "Unknown Publisher") for item in data]
    description = [item["volumeInfo"].get("description", "No description") for item in data]
    publishedDate = [item["volumeInfo"].get("publishedDate", "Unknown Date") for item in data]
    average_rating = [item["volumeInfo"].get("averageRating", "No rating") for item in data]
    language = [item["volumeInfo"].get("language", "Unknown") for item in data]
    preview_link = [item["volumeInfo"].get("previewLink", "#") for item in data]

    return data, title, author_names, publisher, description, publishedDate, average_rating, language, preview_link

if __name__ == "__main__":
    get_books()
