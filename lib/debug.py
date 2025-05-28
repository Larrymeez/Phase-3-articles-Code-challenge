import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Setup
author = Author("Slatt Genius")
author.save()

magazine = Magazine("Tech Pulse", "Technology")
magazine.save()

# Create and save an article
article = Article("AI Takes Over", author.id, magazine.id)
article.save()
print("Saved Article:", article)

# Fetch the article and print related author and magazine
fetched_article = Article.find_by_id(article.id)
print("Fetched Article:", fetched_article)
print("Author:", fetched_article.author())
print("Magazine:", fetched_article.magazine())
print("Magazine Articles:", magazine.articles())
print("Magazine Contributors:", magazine.contributors())
print("Author Articles:", author.articles())
print("Author Magazines:", author.magazines())

# Test add_article and topic_areas
new_article = author.add_article(magazine, "Tech World Domination")
print("Added Article:", new_article)

print("Author's Topic Areas:", author.topic_areas())

print("Top Author:", Author.top_author())

print("Magazines with multiple authors:")

for mag in Magazine.with_multiple_authors():
    print(mag.name)

print("Authors for Magazine ID 1:")
for author in Author.for_magazine(1):
    print(author.name)

print("Article counts per magazine:")
for result in Magazine.article_counts():
    print(f"{result['magazine'].name}: {result['article_count']}")