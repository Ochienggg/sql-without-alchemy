import pytest
from author import Author
from magazine import Magazine
from article import Article

class TestArticle:
    def test_init(self):
        author = Author("John Doe")
        mag = Magazine("Tech", "Tech")
        article = Article(author, mag, "Python")
        assert article.title == "Python"
        assert article.author == author
        assert article.magazine == mag
    
    def test_title_validation(self):
        author = Author("John")
        mag = Magazine("Tech", "Tech")
        with pytest.raises(ValueError):
            Article(author, mag, 123)
        with pytest.raises(ValueError):
            Article(author, mag, "A")
    
    def test_author_validation(self):
        mag = Magazine("Tech", "Tech")
        with pytest.raises(ValueError):
            Article("Not an author", mag, "Python")
    
    def test_magazine_validation(self):
        author = Author("John")
        with pytest.raises(ValueError):
            Article(author, "Not a magazine", "Python")