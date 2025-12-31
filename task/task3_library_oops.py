class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def mark_borrowed(self):
        if self.available == True:
            self.available = False
            return True
        else:
            return False
        
    def mark_returned(self):
        self.available = True



class Library:
    def __init__(self):
        self.books = []


  # # Add a new book to the library
    def add_book(self, book):
        
        existing_book = self.find_book(book.isbn)  # # Check if book already exists
        if existing_book != None:
            print(f"Error: Book with ISBN {book.isbn} already exists!")
            return False
        
        self.books.append(book)
        print(f"Book added successfully: {book.title}")
        return True


    # Remove a book from library
    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book == None:
            print(f"Error: Book with ISBN {isbn} not found")
            return False
        
        if book.available == False:  # Check if book is borrowed
            print(f"Error: Cannot remove '{book.title}' - currently borrowed")
            return False
        
        self.books.remove(book)
        print(f"Book removed: {book.title}")
        return True

   # Find book by isbn
    def find_book(self, isbn):
        for book in self.books:  # Loop through all books
            if book.isbn == isbn:
                return book
        return None  # book not found
    
    # borrow a book from library
    def borrow_book(self, isbn):
        book = self.find_book(isbn)
        if book == None:
            print(f"Error: Book with ISBN {isbn} not found")
            return False
        
        if book.mark_borrowed():
            print(f"You have borrowed: {book.title}")
            return True
        else:
            print(f"Error: '{book.title}' is currently unavailable")
            return False
        
    # return a book to library
    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book == None:
            print(f"Error: Book with ISBN {isbn} not found")
            return False
        
        book.mark_returned()
        print(f"You have returned: {book.title}")
        return True
    
    # list all books in library
    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        
        print("Books in Library:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"- {book.title} by {book.author} (ISBN: {book.isbn}) - {status}")


    
def main():

         # Create library instance
        library = Library()

            # Add sample books
        book1 = Book("Python Pgm", "John", "1")
        library.add_book(book1)

        book2 = Book("Learn Java", "Doe", "2")
        library.add_book(book2)

        book3 = Book("Data Science", "Smith", "3")
        library.add_book(book3)

        # add duplicate book
        duplicate_book = Book("Python Pgm", "John", "1")
        library.add_book(duplicate_book)

        # display all books
        library.list_books()

        # borrow a book
        library.borrow_book("1")
        library.borrow_book("2")

        # try to borrow already borrowed book
        library.borrow_book("1")  

        # display all books
        library.list_books()

        # return a book
        library.return_book("1")

        # try to remove a borrowed book
        library.remove_book("2")

        # remove a book
        library.remove_book("3")

        # display all books
        library.list_books()

        # try to remove non-existing book
        library.remove_book("5")


if __name__ == "__main__":
    main()