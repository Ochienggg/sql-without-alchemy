#!/usr/bin/env python3

from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def main():
    # Create sample data for testing
    print("Creating sample authors...")
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    author3 = Author("Bob Johnson")
    
    print("Creating sample magazines...")
    magazine1 = Magazine("Tech Weekly", "Technology")
    magazine2 = Magazine("Science Today", "Science")
    magazine3 = Magazine("Art Review", "Arts")
    magazine4 = Magazine("Health Digest", "Health")
    
    print("Creating sample articles...")
    # Author 1 articles
    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author1, magazine2, "Quantum Computing Breakthrough")
    article3 = Article(author1, magazine1, "Machine Learning Trends")
    
    # Author 2 articles
    article4 = Article(author2, magazine1, "Python for Data Science")
    article5 = Article(author2, magazine3, "Modern Art Movements")
    article6 = Article(author2, magazine1, "Web Development Best Practices")
    article7 = Article(author2, magazine1, "Cloud Computing Essentials")
    
    # Author 3 articles
    article8 = Article(author3, magazine4, "Healthy Eating Habits")
    article9 = Article(author3, magazine4, "Exercise for Longevity")
    
    print("\n=== Testing Author Methods ===")
    print(f"Author1 name: {author1.name}")
    print(f"Author1 articles: {[article.title for article in author1.articles()]}")
    print(f"Author1 magazines: {[mag.name for mag in author1.magazines()]}")
    print(f"Author1 topic areas: {author1.topic_areas()}")
    
    print("\n=== Testing Magazine Methods ===")
    print(f"Magazine1 name: {magazine1.name}")
    print(f"Magazine1 category: {magazine1.category}")
    print(f"Magazine1 articles count: {len(magazine1.articles())}")
    print(f"Magazine1 contributors: {[author.name for author in magazine1.contributors()]}")
    print(f"Magazine1 article titles: {magazine1.article_titles()}")
    print(f"Magazine1 contributing authors: {[author.name for author in magazine1.contributing_authors()] if magazine1.contributing_authors() else 'None'}")
    
    print("\n=== Testing Top Publisher ===")
    top_mag = Magazine.top_publisher()
    print(f"Top publisher: {top_mag.name if top_mag else 'None'}")
    
    print("\n=== Testing Article Properties ===")
    print(f"Article1 title: {article1.title}")
    print(f"Article1 author: {article1.author.name}")
    print(f"Article1 magazine: {article1.magazine.name}")
    
    print("\n=== Testing Property Validation ===")
    try:
        invalid_author = Author("")  # Should fail
    except ValueError as e:
        print(f"Author validation caught: {e}")
    
    try:
        magazine1.name = "A"  # Should fail (too short)
    except ValueError as e:
        print(f"Magazine name validation caught: {e}")
    
    print("\nSample data created successfully! Starting debug session...")

if __name__ == "__main__":
    main()
    import ipdb; ipdb.set_trace()