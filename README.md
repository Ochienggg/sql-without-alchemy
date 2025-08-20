# Magazine Domain

A Python implementation of a magazine publishing domain with Authors, Articles, and Magazines.

## Domain Model

- **Author**: Has many Articles, has many Magazines through Articles
- **Article**: Belongs to both Author and Magazine
- **Magazine**: Has many Articles, has many Authors through Articles

## Setup

1. Install dependencies:
```bash
pipenv install
Enter the virtual environment:

bash
pipenv shell
Testing
Run all tests:

bash
pytest
Run specific test files:

bash
pytest test/author_test.py
pytest test/magazine_test.py
pytest test/article_test.py
Interactive Debugging
Start an interactive session with sample data:

bash
python lib/debug.py
Features
Property validation with proper error handling

Object relationship management

Aggregate methods for data analysis

Comprehensive test suite

Interactive debugging capabilities

Class Documentation
See individual class files for detailed method documentation and usage examples.

text

This complete implementation includes:

1. **All three models** with proper relationships
2. **Full property validation** with error handling
3. **All required methods** from the deliverables
4. **Comprehensive test suite** covering all functionality
5. **Interactive debug script** for manual testing
6. **Proper project structure** with imports and dependencies

To use this project:

1. Run `pipenv install` to set up the environment
2. Run `pipenv shell` to enter the virtual environment
3. Run `pytest` to verify all tests pass
4. Run `python lib/debug.py` for interactive testing

The implementation follows object-oriented principles, maintains proper relationships between classes, and includes all the required functionality as specified in the deliverables.