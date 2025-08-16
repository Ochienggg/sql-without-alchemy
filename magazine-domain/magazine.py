class Magazine:
    _all_magazines = []
    
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value
    
    def articles(self):
        from article import Article  # Local import to break circular dependency
        return self._articles
    
    def contributors(self):
        from author import Author  # Local import to break circular dependency
        return list({article.author for article in self._articles})
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        from author import Author  # Local import to break circular dependency
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag.articles()), default=None)