import pytest
from author import Author
from magazine import Magazine
from article import Article

class TestRelationships:
    def test_author_article_relationship(self):
        author = Author("John")
        mag = Magazine("Tech", "Tech")
        article = Article(author, mag, "Python")
        assert article in author.articles()
        assert article in mag.articles()
    
    def test_magazine_contributors(self):
        author1 = Author("John")
        author2 = Author("Jane")
        mag = Magazine("Tech", "Tech")
        Article(author1, mag, "Python")
        Article(author2, mag, "Ruby")
        assert author1 in mag.contributors()
        assert author2 in mag.contributors()
    
    def test_author_magazines(self):
        author = Author("John")
        mag1 = Magazine("Tech", "Tech")
        mag2 = Magazine("Science", "Science")
        Article(author, mag1, "Python")
        Article(author, mag2, "Physics")
        assert mag1 in author.magazines()
        assert mag2 in author.magazines()