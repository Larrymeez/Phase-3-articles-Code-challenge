from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def interactive():
    print("Welcome to the debug console.")
    print("Try fetching authors, magazines, and articles.")
    
    a = Author.find_by_name('William')
    if a is None:
        print("Author 'William' not found.")
        return
    
    print(f"Author {a.name} has written these articles:")
    articles = a.articles()
    if not articles:
        print("No articles found for this author.")
    else:
        for art in articles:
            print(f" - {art.title}")

if __name__ == "__main__":
    interactive()

