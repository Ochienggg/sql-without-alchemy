import pytest
from author import Author
from magazine import Magazine
from article import Article

class TestAuthor:
    def test_init(self):
        author = Author("John Doe")
        assert author.name == "John Doe"
    
    def test_name_validation(self):
        with pytest.raises(ValueError):
            Author(123)
        with pytest.raises(ValueError):
            Author("")
    
    def test_articles(self):
        author = Author("John Doe")
        mag = Magazine("Tech", "Tech")
        article = author.add_article(mag, "Python")
        assert article in author.articles()
    
    def test_magazines(self):
        author = Author("John Doe")
        mag1 = Magazine("Tech", "Tech")
        mag2 = Magazine("Science", "Science")
        author.add_article(mag1, "Python")
        author.add_article(mag2, "Physics")
        assert len(author.magazines()) == 2