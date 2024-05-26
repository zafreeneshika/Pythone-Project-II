from Person import Person

class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self._borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self._borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books and book.return_book():
            self._borrowed_books.remove(book)
            return True
        return False

    def list_borrowed_books(self):
        return self._borrowed_books