class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._checked_out = False  # Private attribute for availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._checked_out:
            self._checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._checked_out:
            self._checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._checked_out

    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a library containing multiple books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """Print all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)

