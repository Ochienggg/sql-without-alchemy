import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

class TestMagazine:
    '''Class Magazine in magazine.py'''

    def test_has_name(self):
        '''magazine is initialized with a name'''
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.name == "Vogue"

    def test_name_is_mutable_string(self):
        '''magazine name is of type str and can change'''
        magazine = Magazine("Vogue", "Fashion")
        assert isinstance(magazine.name, str)
        
        magazine.name = "New Magazine"
        assert magazine.name == "New Magazine"

    def test_name_len_between_2_and_16(self):
        '''magazine name is between 2 and 16 characters'''
        with pytest.raises(ValueError):
            Magazine("A", "Fashion")
        with pytest.raises(ValueError):
            Magazine("This name is way too long for a magazine", "Fashion")

    def test_has_category(self):
        '''magazine is initialized with a category'''
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.category == "Fashion"

    def test_category_is_mutable_string(self):
        '''magazine category is of type str and can change'''
        magazine = Magazine("Vogue", "Fashion")
        assert isinstance(magazine.category, str)
        
        magazine.category = "Lifestyle"
        assert magazine.category == "Lifestyle"

    def test_category_len_greater_than_zero(self):
        '''magazine category has length > 0'''
        with pytest.raises(ValueError):
            Magazine("Vogue", "")

    def test_has_many_articles(self):
        '''magazine has many articles'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")
        
        assert len(magazine.articles()) == 2
        assert article_1 in magazine.articles()
        assert article_2 in magazine.articles()

    def test_articles_of_type_articles(self):
        '''magazine articles are of type Article'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(magazine.articles()[0], Article)

    def test_has_many_contributors(self):
        '''magazine has many contributors'''
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")
        
        assert author_1 in magazine.contributors()
        assert author_2 in magazine.contributors()

    def test_contributors_of_type_author(self):
        '''magazine contributors are of type Author'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(magazine.contributors()[0], Author)

    def test_contributors_are_unique(self):
        '''magazine contributors are unique'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Dating life in NYC")
        
        assert len(set(magazine.contributors())) == len(magazine.contributors())
        assert len(magazine.contributors()) == 1

    def test_article_titles(self):
        '''article_titles returns list of article titles'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Dating life in NYC")
        
        assert "How to wear a tutu with style" in magazine.article_titles()
        assert "Dating life in NYC" in magazine.article_titles()
        assert len(magazine.article_titles()) == 2

    def test_article_titles_returns_none_if_no_articles(self):
        '''article_titles returns None if magazine has no articles'''
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.article_titles() is None

    def test_contributing_authors(self):
        '''contributing_authors returns authors with more than 2 articles'''
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "Article 1")
        Article(author_1, magazine, "Article 2")
        Article(author_1, magazine, "Article 3")
        Article(author_2, magazine, "Article 4")
        
        assert author_1 in magazine.contributing_authors()
        assert author_2 not in magazine.contributing_authors()

    def test_contributing_authors_returns_none_if_no_authors(self):
        '''contributing_authors returns None if no authors with >2 articles'''
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "Article 1")
        
        assert magazine.contributing_authors() is None

    def test_top_publisher(self):
        '''top_publisher returns magazine with most articles'''
        Magazine.all_magazines.clear()
        
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author = Author("Carry Bradshaw")
        
        Article(author, magazine_1, "Article 1")
        Article(author, magazine_1, "Article 2")
        Article(author, magazine_2, "Article 3")
        
        assert Magazine.top_publisher() == magazine_1

    def test_top_publisher_returns_none_if_no_articles(self):
        '''top_publisher returns None if no articles exist'''
        Magazine.all_magazines.clear()
        Magazine("Vogue", "Fashion")
        Magazine("AD", "Architecture")
        
        assert Magazine.top_publisher() is None