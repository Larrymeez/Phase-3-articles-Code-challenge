import sys
import os

# ✅ Add project root to Python import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

# Example function: show all authors
def show_authors():
    authors = Author.all()
    print("\n📚 Authors:")
    for author in authors:
        print(f"{author.id}: {author.name}")

# Example function: show all magazines
def show_magazines():
    magazines = Magazine.all()
    print("\n📰 Magazines:")
    for mag in magazines:
        print(f"{mag.id}: {mag.name} ({mag.category})")

# Example function: show all articles
def show_articles():
    articles = Article.all()
    print("\n📝 Articles:")
    for article in articles:
        print(f"{article.id}: '{article.title}' by Author #{article.author_id} in Magazine #{article.magazine_id}")

if __name__ == "__main__":
    show_authors()
    show_magazines()
    show_articles()
