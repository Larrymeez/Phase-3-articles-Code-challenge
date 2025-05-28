from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def interactive():
    print("Welcome to the debug console.")
    print("Try fetching authors, magazines, and articles.")
    # Simple test interaction:
    a = Author.find_by_name('Donald')
    print(f"Author {a.name} has written these articles:")
    for art in a.articles():
        print(f" - {art.title}")

if __name__ == "__main__":
    interactive()
