from Person import Person


class Librarian(Person):
    def __init__(self, name, librarian_id):
        super().__init__(name, librarian_id)

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book):
        library.remove_book(book)

    def register_member(self, library, member):
        library.add_member(member)

    def unregister_member(self, library, member):
        library.remove_member(member)

