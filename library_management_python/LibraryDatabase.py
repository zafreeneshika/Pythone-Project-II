import tkinter as tk
import mysql.connector
from CustomDialog import CustomDialog

class LibraryDatabase:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        self.create_tables()
        

    def create_tables(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            book_id INT AUTO_INCREMENT PRIMARY KEY,
                            title VARCHAR(255) NOT NULL,
                            author VARCHAR(255) NOT NULL,
                            isbn VARCHAR(255) NOT NULL UNIQUE)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                            member_id VARCHAR(255) PRIMARY KEY,
                            name VARCHAR(255) NOT NULL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS borrowings (
                            borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
                            member_id VARCHAR(255) NOT NULL,
                            book_id INT NOT NULL,
                            FOREIGN KEY(member_id) REFERENCES members(member_id),
                            FOREIGN KEY(book_id) REFERENCES books(book_id))''')
        self.db_connection.commit()

    def add_book(self, title, author, isbn, book_id):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute("INSERT INTO books (book_id, title, author, isbn) VALUES (%s, %s, %s, %s)", (book_id, title, author, isbn))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def add_member(self, name, member_id):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute("INSERT INTO members (member_id, name) VALUES (%s, %s)", (member_id, name))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
        
    def remove_book(self, book_id):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id))
            self.db.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
    
    def remove_member(self, member_id):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id))
            self.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def list_books(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        return books  

    def list_members(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()
        return members 

    def borrow_book(self, member_id, book_id):
        cursor = self.db_connection.cursor()
        try:
            # Check if the member exists
            cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
            member = cursor.fetchone()
            if not member:
                self.show_custom_message("Error", "Member not found.")
                return

            # Check if the book is available
            cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()
            if not book:
                self.show_custom_message("Error", "Book not found.")
                return

            # Check if the book is already borrowed
            cursor.execute("SELECT * FROM borrowings WHERE book_id = %s", (book_id,))
            borrowing = cursor.fetchone()
            if borrowing:
                self.show_custom_message("Error", "Book is already borrowed.")
                return

            # Record the borrowing
            cursor.execute("INSERT INTO borrowings (member_id, book_id) VALUES (%s, %s)", (member_id, book_id))
            self.db_connection.commit()
            self.show_custom_message("Success", "Book borrowed successfully.")
        except mysql.connector.Error as err:
            self.show_custom_message("Error", f"An error occurred: {err}")

    def return_book(self, member_id, book_id):
        cursor = self.db_connection.cursor()
        try:
            # Check if the borrowing exists
            cursor.execute("SELECT * FROM borrowings WHERE member_id = %s AND book_id = %s", (member_id, book_id))
            borrowing = cursor.fetchone()
            if not borrowing:
                self.show_custom_message("Error", "No active borrowing found.")
                return

            # Update the borrowing to mark the book as returned
            cursor.execute("Delete borrowings WHERE member_id = %s AND book_id = %s", (member_id, book_id))
            self.db_connection.commit()
            self.show_custom_message("Success", "Book returned successfully.")
        except mysql.connector.Error as err:
            self.show_custom_message("Error", f"An error occurred: {err}")

    def close_connection(self):
        if self.db_connection:
            self.db_connection.close()
    
    def show_custom_message(self, title, message):
        root = tk.Tk()
        root.withdraw()
        dialog = CustomDialog(root, title, message)
        root.mainloop()