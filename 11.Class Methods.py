# 11. Class Methods
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0 

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print("Total books:", cls.total_books)

# Example usage:
b1 = Book("1984")
b2 = Book("To Kill a Mockingbird")
b3 = Book("The Great Gatsby")
b4 = Book("The Angle Book")


Book.display_total_books()
