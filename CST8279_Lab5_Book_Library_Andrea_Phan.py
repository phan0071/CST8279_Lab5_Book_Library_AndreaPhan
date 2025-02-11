class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies
    
    def display_info(self):
        print(f"Book Details:\nTitle: {self.title}; Author: {self.author}; ISBN: {self.isbn}; Available Copies: {self.available_copies}")

    def borrow_book(self, num_books):
        self.available_copies -= num_books
    
    def return_book(self, num_books):
        self.available_copies += num_books

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def find_book_by_title(self, title):
        try:
            self.books.index(title)
            print(f'{title} is in the library.')
        except:
            print(f'{title} is not in the library.')
    
    def display_all_books(self):
        print(self.books)

book1 = Book('Hello', 'Bob', 12345, 5)

book1.display_info()
book1.borrow_book(2)
book1.display_info()
book1.return_book(2)
book1.display_info()

book2 = Book('Bye', 'Rob', 54321, 10)

library1 = Library()
library1.display_all_books()
library1.add_book(book1.title)
library1.display_all_books()
library1.find_book_by_title('Hello')
library1.find_book_by_title('Bye')



