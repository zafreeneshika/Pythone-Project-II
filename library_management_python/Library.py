class Library:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._librarians = {}

    def add_book(self, book):
        self._books[book.book_id] = book

    def remove_book(self, book):
        if book.book_id in self._books:
            del self._books[book.book_id]

    def list_books(self):
        return self._books.values()

    def add_member(self, member):
        self._members[member.person_id] = member

    def remove_member(self, member):
        if member.person_id in self._members:
            del self._members[member.person_id]

    def list_members(self):
        return self._members.values()

    def add_librarian(self, librarian):
        self._librarians[librarian.person_id] = librarian

    def remove_librarian(self, librarian):
        if librarian.person_id in self._librarians:
            del self._librarians[librarian.person_id]

    def list_librarians(self):
        return self._librarians.values()

