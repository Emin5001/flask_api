from flask import url_for
from app import app

@app.route('/')
def api_root():
    return "Welcome"

@app.route('/articles')
def api_articles():
    return "List of " + url_for("api_articles")

@app.route('/articles/<articleid>')
def api_article(articleid):
    return "You are reading " + articleid
