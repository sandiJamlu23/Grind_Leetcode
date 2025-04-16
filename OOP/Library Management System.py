class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return "Book is not available"
        
        self.is_borrowed = True
        return f"You have successfully borrowed Book {self.book_id}"

    def return_book(self):
        self.is_borrowed = False
        return f"Book {self.book_id} is now available"

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.borrowed_books:
            return f"You already borrowed Book {book.book_id}"
        if book.is_borrowed:
            return "Book is not available"

        self.borrowed_books.append(book)
        return book.borrow()

    def return_book(self, book):
        if book not in self.borrowed_books:
            return f"You didn't borrow Book {book.book_id}"

        self.borrowed_books.remove(book)
        return book.return_book()


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, book_id, user_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not book:
            return f"Book {book_id} not found"
        if not user:
            return f"User {user_id} not found"

        return user.borrow_book(book)

    def return_book(self, book_id, user_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if not book:
            return f"Book {book_id} not found"
        if not user:
            return f"User {user_id} not found"

        return user.return_book(book)

    def show_all_books(self):
        return "\n".join(str(book) for book in self.books)

    def show_user_borrowed_books(self, user_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            return f"User {user_id} not found"
        
        if not user.borrowed_books:
            return f"{user.name} has not borrowed any books"

        return "\n".join(str(book) for book in user.borrowed_books)


if __name__ == "__main__":
    # Initialize Library
    my_library = Library()

    # Create books
    book1 = Book("1984", "George Orwell", "B1")
    book2 = Book("The Hobbit", "J.R.R. Tolkien", "B2")
    book3 = Book("The Alchemist", "Paulo Coelho", "B3")

    # Add books to library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Create users
    user1 = User("U1", "Sandi")
    user2 = User("U2", "Aloy")

    # Register users
    my_library.register_user(user1)
    my_library.register_user(user2)

    # Borrow and return books
    print(my_library.borrow_book("B1", "U1"))
    print(my_library.borrow_book("B1", "U2"))
    print(my_library.return_book("B1", "U1"))
    print(my_library.borrow_book("B1", "U2"))

    # Display books and user borrowings
    print("\nAll Books:")
    print(my_library.show_all_books())

    print("\nSandi's Borrowed Books:")
    print(my_library.show_user_borrowed_books("U1"))

    print("\nAloy's Borrowed Books:")
    print(my_library.show_user_borrowed_books("U2"))
