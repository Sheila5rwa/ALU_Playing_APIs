#!/usr/bin/env python3

import os
from flask import Flask, request, render_template
from get_book import get_books

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        user_search = request.form.get("query")
        books_data = get_books(domain=user_search)

        print(user_search)
        print(books_data)
        return render_template("results.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
