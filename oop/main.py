from book_class import Book

my_book = Book("1984", "George Orwell", 1949)

print(my_book)        # __str__
print(repr(my_book))  # __repr__

del my_book           # __del__
