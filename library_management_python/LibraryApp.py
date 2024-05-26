import tkinter as tkk
from Book import Book
from CustomDialog import CustomDialog
from Librarian import Librarian
from Library import Library
from LibraryDatabase import LibraryDatabase
from Member import Member


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.db = LibraryDatabase()

        self.library = Library()
        self.librarian = Librarian("Admin", "L001")
        self.library.add_librarian(self.librarian)

        self.root = root
        self.root.title("Library Management System")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.main_frame = tkk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.main_frame.configure(bg="#f0f0f0")  # Set background color

        # Books Section
        self.book_frame = tkk.LabelFrame(self.main_frame, text="Books", bg="#e6e6e6", padx=20, pady=20)
        self.book_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.book_frame.grid_columnconfigure(1, weight=1)

        # Set style for labels
        label_style = {'font': ('Arial', 12), 'bg': '#e6e6e6'}

        tkk.Label(self.book_frame, text="Title:", **label_style).grid(row=0, column=0, sticky="e")
        tkk.Label(self.book_frame, text="Author:", **label_style).grid(row=1, column=0, sticky="e")
        tkk.Label(self.book_frame, text="ISBN:", **label_style).grid(row=2, column=0, sticky="e")
        tkk.Label(self.book_frame, text="Book ID:", **label_style).grid(row=3, column=0, sticky="e")

        # Increase entry width and add padding
        entry_style = {'width': 30, 'font': ('Arial', 12), 'bg': 'white', 'highlightthickness': 2, 'highlightbackground': 'black'}
        self.book_title_entry = tkk.Entry(self.book_frame, **entry_style)
        self.book_author_entry = tkk.Entry(self.book_frame, **entry_style)
        self.book_isbn_entry = tkk.Entry(self.book_frame, **entry_style)
        self.book_id_entry = tkk.Entry(self.book_frame, **entry_style)

        self.book_title_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        self.book_author_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        self.book_isbn_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)
        self.book_id_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        # Set style for buttons
        button_style = {'font': ('Arial', 12), 'bg': '#4CAF50', 'fg': 'white', 'padx': 10, 'pady': 5}

        self.add_book_button = tkk.Button(self.book_frame, text="Add Book", command=self.add_book, **button_style)
        self.add_book_button.grid(row=5, columnspan=2, pady=10)

        self.remove_book_button = tkk.Button(self.book_frame, text="Remove Book", command=self.remove_book, **button_style)
        self.remove_book_button.grid(row=6, columnspan=2, pady=10)

        self.list_books_button = tkk.Button(self.book_frame, text="List Books", command=self.list_books, **button_style)
        self.list_books_button.grid(row=7, columnspan=2, pady=10)
        
        # Member Section
        self.member_frame = tkk.LabelFrame(self.main_frame, text="Members", bg="#e6e6e6", padx=20, pady=20)
        self.member_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.member_frame.grid_columnconfigure(1, weight=1)
        
        tkk.Label(self.member_frame, text="Name:", **label_style).grid(row=0, column=0, sticky="e")
        tkk.Label(self.member_frame, text="Member ID:", **label_style).grid(row=1, column=0, sticky="e")
        
        self.member_name_entry = tkk.Entry(self.member_frame, **entry_style)
        self.member_id_entry = tkk.Entry(self.member_frame, **entry_style)
        
        self.member_name_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        self.member_id_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        
        self.add_member_button = tkk.Button(self.member_frame, text="Add Member", command=self.add_member, **button_style)
        self.add_member_button.grid(row=3, columnspan=2, pady=10)
        
        self.remove_member_button = tkk.Button(self.member_frame, text="Remove Member", command=self.remove_member, **button_style)
        self.remove_member_button.grid(row=4, columnspan=2, pady=10)
        
        self.list_members_button = tkk.Button(self.member_frame, text="List Members", command=self.list_members, **button_style)
        self.list_members_button.grid(row=5, columnspan=2, pady=10)
        
        # Borrow/Return Section
        self.borrow_frame = tkk.LabelFrame(self.main_frame, text="Borrow/Return", bg="#e6e6e6", padx=20, pady=20)
        self.borrow_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
        self.borrow_frame.grid_columnconfigure(1, weight=1)
        
        tkk.Label(self.borrow_frame, text="Member ID:", **label_style).grid(row=0, column=0, sticky="e")
        tkk.Label(self.borrow_frame, text="Book ID:", **label_style).grid(row=1, column=0, sticky="e")
        
        self.borrow_member_id_entry = tkk.Entry(self.borrow_frame, **entry_style)
        self.borrow_book_id_entry = tkk.Entry(self.borrow_frame, **entry_style)
        
        self.borrow_member_id_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        self.borrow_book_id_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        
        self.borrow_book_button = tkk.Button(self.borrow_frame, text="Borrow Book", command=self.borrow_book, **button_style)
        self.borrow_book_button.grid(row=2, column=0, pady=10)
        
        self.return_book_button = tkk.Button(self.borrow_frame, text="Return Book", command=self.return_book, **button_style)
        self.return_book_button.grid(row=2, column=1, pady=10)
        
        self.list_borrowed_books_button = tkk.Button(self.borrow_frame, text="List Borrowed Books", command=self.list_borrowed_books, **button_style)
        self.list_borrowed_books_button.grid(row=2, column=3, pady=10)
        
    def show_custom_message(self, title, message):
        root = tkk.Tk()
        root.withdraw()
        dialog = CustomDialog(root, title, message)
        root.mainloop()

    def list_borrowed_books(self):
        member_id = self.borrow_member_id_entry.get()
        if member_id:
            member = self.library._members.get(member_id)
            if member:
                borrowed_books_info = "\n".join([f"{book.title} by {book.author} (Book ID: {book.book_id})" for book in member.list_borrowed_books()])
                self.show_custom_message("Borrowed Books", f"Borrowed Books by {member.name}:\n{borrowed_books_info}")
            else:
                self.show_custom_message("Error", "Member not found.")
        else:
            self.show_custom_message("Error", "Please enter member ID.")
    
    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        isbn = self.book_isbn_entry.get()
        book_id = self.book_id_entry.get()
        if title and author and isbn and book_id:
            book = Book(title, author, isbn, book_id)
            self.librarian.add_book(self.library, book)
            self.db.add_book(title, author, isbn, book_id)
            self.show_custom_message("Success", f"Book '{title}' added successfully.")
        else:
            self.show_custom_message("Error", "Please fill all book details.")

    def remove_book(self):
        book_id = self.book_id_entry.get()
        if book_id:
            book = self.library._books.get(book_id)
            if book:
                self.librarian.remove_book(self.library, book)
                self.db.remove_book(book_id)
                self.show_custom_message("Success", f"Book '{book.title}' removed successfully.")
            else:
                self.show_custom_message("Error", "Book not found.")
        else:
            self.show_custom_message("Error", "Please enter book ID.")

    def add_member(self):
        name = self.member_name_entry.get()
        member_id = self.member_id_entry.get()
        if name and member_id:
            member = Member(name, member_id)
            self.librarian.register_member(self.library, member)
            self.db.add_member(name, member_id)
            self.show_custom_message("Success", f"Member '{name}' registered successfully.")
        else:
            self.show_custom_message("Error", "Please fill all member details.")

    def remove_member(self):
        member_id = self.member_id_entry.get()
        if member_id:
            member = self.library._members.get(member_id)
            if member:
                self.librarian.unregister_member(self.library, member)
                self.db.remove_member(member_id)
                self.show_custom_message("Success", f"Member '{member.name}' removed successfully.")
            else:
                self.show_custom_message("Error", "Member not found.")
        else:
            self.show_custom_message("Error", "Please enter member ID.")

    def borrow_book(self):
        member_id = self.borrow_member_id_entry.get()
        book_id = self.borrow_book_id_entry.get()
        if member_id and book_id:
            member = self.library._members.get(member_id)
            book = self.library._books.get(book_id)
            if member and book:
                if member.borrow_book(book):
                    self.db.borrow_book(member_id, book_id)
                    self.show_custom_message("Success", f"Book '{book.title}' borrowed successfully by {member.name}.")
                else:
                    self.show_custom_message("Error", f"Book '{book.title}' is already borrowed.")
            else:
                self.show_custom_message("Error", "Invalid member ID or book ID.")
        else:
            self.show_custom_message("Error", "Please fill both member ID and book ID.")

    def return_book(self):
        member_id = self.borrow_member_id_entry.get()
        book_id = self.borrow_book_id_entry.get()
        if member_id and book_id:
            member = self.library._members.get(member_id)
            book = self.library._books.get(book_id)
            if member and book:
                if member.return_book(book):
                    self.db.return_book(member_id, book_id)
                    self.show_custom_message("Success", f"Book '{book.title}' returned successfully by {member.name}.")
                else:
                    self.show_custom_message("Error", f"Book '{book.title}' was not borrowed by {member.name}.")
            else:
                self.show_custom_message("Error", "Invalid member ID or book ID.")
        else:
            self.show_custom_message("Error", "Please fill both member ID and book ID.")

    def list_books(self):
        books = self.db.list_books()
        books_info = "\n".join([f"{book.title} by {book.author} (Member ID: {book.book_id})" for book in self.library.list_books()])
        self.show_custom_message("Books", books_info)

    def list_members(self):
        member = self.db.list_members()
        members_info = "\n".join([f"{member.name} (Member ID: {member.person_id})" for member in self.library.list_members()])
        self.show_custom_message("Members", members_info)
        


def main():
    root = tkk.Tk()
    app = LibraryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

