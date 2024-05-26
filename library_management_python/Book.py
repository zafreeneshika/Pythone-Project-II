class Book:
    def __init__(self, title, author, isbn, book_id):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._book_id = book_id
        self._is_borrowed = False

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def book_id(self):
        return self._book_id

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False
