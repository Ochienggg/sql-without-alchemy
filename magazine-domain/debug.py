from author import Author
from magazine import Magazine
from article import Article

# Sample data for testing
author1 = Author("John Doe")
author2 = Author("Jane Smith")
mag1 = Magazine("Tech Today", "Technology")
mag2 = Magazine("Fashion Weekly", "Fashion")

article1 = Article(author1, mag1, "The Future of AI")
article2 = Article(author1, mag2, "Tech in Fashion")
article3 = Article(author2, mag1, "Python for Beginners")
article4 = Article(author1, mag1, "Machine Learning Trends")

print("Debug console ready. You can interact with:")
print("- author1, author2")
print("- mag1, mag2")
print("- article1, article2, article3, article4")

# Start debug session
import ipdb; ipdb.set_trace()