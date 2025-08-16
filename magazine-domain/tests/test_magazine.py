import pytest
from author import Author
from magazine import Magazine
from article import Article

class TestMagazine:
    def test_init(self):
        mag = Magazine("Tech Today", "Technology")
        assert mag.name == "Tech Today"
        assert mag.category == "Technology"
    
    def test_name_validation(self):
        with pytest.raises(ValueError):
            Magazine(123, "Tech")
        with pytest.raises(ValueError):
            Magazine("A", "Tech")
    
    def test_articles(self):
        mag = Magazine("Tech", "Tech")
        author = Author("John")
        article = Article(author, mag, "Python")
        assert article in mag.articles()
    
    def test_contributors(self):
        mag = Magazine("Tech", "Tech")
        author1 = Author("John")
        author2 = Author("Jane")
        Article(author1, mag, "Python")
        Article(author2, mag, "Ruby")
        assert len(mag.contributors()) == 2