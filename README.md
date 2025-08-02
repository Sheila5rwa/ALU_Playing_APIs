 Book Reader Web App

This is a Flask-based web application that allows users to search for books by subject using the Google Books API. Results are displayed in a user-friendly directory with book details and preview links.

 Features

- Search for books by subject/domain
- Displays book title, author, publisher, description, published date, language, and average rating
- Preview books via Google Books
- Session-based storage for user queries
- Docker support for easy deployment

Getting Started

 Prerequisites

- Python 3.9+
- Docker (optional, for containerized deployment)

 Installation

1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your Google Books API key in `config.env`:
   ```
   GOOGLE_BOOK_API=your_api_key_here
   ```

 Running Locally

```sh
python main.py
```
The app will be available at [http://localhost:8080](http://localhost:8080).

 Running with Docker

Build and run the Docker container:
```sh
docker build -t book-reader .
docker run -p 8080:8080 --env-file config.env book-reader
```

Project Structure

- `main.py` - Main Flask application
- `get_book.py` - Fetches book data from Google Books API
- `templates/` - HTML templates for the web interface
- `static/` - Static files (CSS, JS,
