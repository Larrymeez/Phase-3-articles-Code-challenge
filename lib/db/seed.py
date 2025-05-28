from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM authors;
        DELETE FROM magazines;

        INSERT INTO authors (name) VALUES
            ('Donald'), ('William'), ('Macron');

        INSERT INTO magazines (name, category) VALUES
            ('Tech Today', 'Technology'),
            ('Health Weekly', 'Health'),
            ('Travel Guide', 'Travel');

        INSERT INTO articles (title, author_id, magazine_id) VALUES
            ('AI Advances', 1, 1),
            ('New Gadgets', 2, 1),
            ('Healthy Living Tips', 3, 2),
            ('Exploring Mountains', 2, 3),
            ('Tech Innovations', 1, 1),
            ('Travel Essentials', 3, 3),
            ('Fitness Trends', 1, 2);
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
