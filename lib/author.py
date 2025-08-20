class Author:
    all_authors = []

    def __init__(self, name):
        self._name = None
        self.name = name
        self._articles = []
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) <= 0:
            raise ValueError("Name must be longer than 0 characters")
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Import here to avoid circular imports
        from lib.article import Article
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))

    def __repr__(self):
        return f"<Author name={self.name}>"