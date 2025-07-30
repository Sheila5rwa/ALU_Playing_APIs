#!/usr/bin/env python3

import os
import secrets
from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session
from collections import defaultdict
from get_book import get_books  # Make sure this function returns a tuple of 8 lists

app = Flask(__name__)

# Set up a temporary folder to store session files
os.makedirs("temp_session", exist_ok=True)

app.secret_key = secrets.token_hex(16)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.abspath("temp_session")
app.config['SESSION_PERMANENT'] = False

# Enable server-side sessions
Session(app)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        user_search = request.form.get("query")
        books_data = get_books(domain=user_search)
        session["book_data"] = books_data
        return redirect(url_for("results"))
    return render_template("index.html")


@app.route("/results", methods=["GET"])
def results():
    book_data = session.get("book_data", None)
    
    # Ensure the data is valid
    if not book_data or not isinstance(book_data, (tuple, list)) or len(book_data) != 8:
        title, author_names, publisher, description, publishedDate, average_rating, language, preview_link = [], [], [], [], [], [], [], []
    else:
        title, author_names, publisher, description, publishedDate, average_rating, language, preview_link = book_data

    # Grouping books by their title (key) and all associated metadata (value)
    grouped_info = defaultdict(list)
    for t, an, pub, desc, pdate, a_rating, lang, preview in zip(
        title, author_names, publisher, description, publishedDate, average_rating, language, preview_link
    ):
        grouped_info[t].append({
            "author": an,
            "publisher": pub,
            "description": desc,
            "publishedDate": pdate,
            "average_rating": a_rating,
            "language": lang,
            "preview_link": preview
        })
        print(grouped_info)

    return render_template("test.html", grouped_info=grouped_info)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
