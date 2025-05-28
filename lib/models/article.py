from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (self.title, self.author_id, self.magazine_id)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                (self.title, self.author_id, self.magazine_id, self.id)
            )
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row["id"], title=row["title"], author_id=row["author_id"], magazine_id=row["magazine_id"])
        return None

    def author(self):
        from lib.models.author import Author  # Import here to avoid circular import
        return Author.find_by_id(self.author_id)

    def magazine(self):
        from lib.models.magazine import Magazine  # Import here to avoid circular import
        return Magazine.find_by_id(self.magazine_id)

    def __repr__(self):
        return f"<Article id={self.id} title='{self.title}'>"