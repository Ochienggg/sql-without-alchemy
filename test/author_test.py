import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

class TestAuthor:
    '''Class Author in author.py'''

    def test_has_name(self):
        '''author is initialized with a name'''
        author = Author("Carry Bradshaw")
        assert author.name == "Carry Bradshaw"

    def test_name_is_immutable_string(self):
        '''author name is of type str and cannot change'''
        author = Author("Carry Bradshaw")
        assert isinstance(author.name, str)
        
        with pytest.raises(AttributeError):
            author.name = "New Name"

    def test_name_len_greater_than_zero(self):
        '''author name has length > 0'''
        with pytest.raises(ValueError):
            Author("")
            
    def test_has_many_articles(self):
        '''author has many articles'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")
        
        assert len(author.articles()) == 2
        assert article_1 in author.articles()
        assert article_2 in author.articles()

    def test_articles_of_type_articles(self):
        '''author articles are of type Article'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(author.articles()[0], Article)

    def test_has_many_magazines(self):
        '''author has many magazines'''
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "Dating life in NYC")
        
        assert magazine_1 in author.magazines()
        assert magazine_2 in author.magazines()

    def test_magazines_of_type_magazine(self):
        '''author magazines are of type Magazine'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(author.magazines()[0], Magazine)

    def test_magazines_are_unique(self):
        '''author magazines are unique'''
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_1, "How to be single and happy")
        Article(author, magazine_2, "Dating life in NYC")
        
        assert len(set(author.magazines())) == len(author.magazines())
        assert len(author.magazines()) == 2

    def test_add_article(self):
        '''add_article method creates a new article for the author'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "New Article")
        
        assert article in author.articles()
        assert article in magazine.articles()
        assert article.author == author
        assert article.magazine == magazine
        assert article.title == "New Article"

    def test_topic_areas(self):
        '''topic_areas returns unique category strings'''
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "Dating life in NYC")
        Article(author, magazine_3, "Summer looks")
        
        assert "Fashion" in author.topic_areas()
        assert "Architecture" in author.topic_areas()
        assert len(author.topic_areas()) == 2

    def test_topic_areas_returns_none_if_no_articles(self):
        '''topic_areas returns None if author has no articles'''
        author = Author("Carry Bradshaw")
        assert author.topic_areas() is None