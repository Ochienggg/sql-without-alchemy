# Import at the top level but use TYPE_CHECKING to avoid circular imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.author import Author
    from lib.magazine import Magazine

class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Title cannot be changed after instantiation")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # Import here to avoid circular imports
        from lib.author import Author
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Import here to avoid circular imports
        from lib.magazine import Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value

    def __repr__(self):
        return f"<Article title={self.title}, author={self.author.name}, magazine={self.magazine.name}>"