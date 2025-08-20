import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

class TestArticle:
    '''Class Article in article.py'''

    def test_has_title(self):
        '''article is initialized with a title'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert article.title == "How to wear a tutu with style"

    def test_title_is_immutable_string(self):
        '''article title is of type str and cannot change'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(article.title, str)
        
        with pytest.raises(AttributeError):
            article.title = "New Title"

    def test_title_len_between_5_and_50(self):
        '''article title is between 5 and 50 characters'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        
        with pytest.raises(ValueError):
            Article(author, magazine, "Hi")
        with pytest.raises(ValueError):
            Article(author, magazine, "This title is way too long and should definitely exceed fifty characters")

    def test_has_an_author(self):
        '''article belongs to an author'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        assert article.author == author

    def test_author_of_type_author(self):
        '''article author is of type Author'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        assert isinstance(article.author, Author)

    def test_author_can_change(self):
        '''article author can be changed'''
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author_1, magazine, "How to wear a tutu with style")
        
        article.author = author_2
        assert article.author == author_2

    def test_has_a_magazine(self):
        '''article belongs to a magazine'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        assert article.magazine == magazine

    def test_magazine_of_type_magazine(self):
        '''article magazine is of type Magazine'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        assert isinstance(article.magazine, Magazine)

    def test_magazine_can_change(self):
        '''article magazine can be changed'''
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article = Article(author, magazine_1, "How to wear a tutu with style")
        
        article.magazine = magazine_2
        assert article.magazine == magazine_2