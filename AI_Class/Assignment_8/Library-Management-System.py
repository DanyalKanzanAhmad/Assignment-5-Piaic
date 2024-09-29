class Book:
    def __init__(self, book_id, title, author, genre, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []


def add_book(books, book_id, title, author, genre):
    new_book = Book(book_id, title, author, genre, "Available")
    books.append(new_book)


def add_user(users, user_id, name):
    new_user = User(user_id, name)
    users.append(new_user)


def borrow_book(books, users, user_id, book_id):
    user = None
    book = None
    for u in users:
        if u.user_id == user_id:
            user = u
            break
    for b in books:
        if b.book_id == book_id and b.status == "Available":
            book = b
            break
    if user and book:
        user.borrowed_books.append(book)
        book.status = "Checked Out"
        print(f"You have successfully borrowed '{book.title}'.")
        return True
    else:
        print("Book is not available or user not found.")
        return False


def return_book(books, users, user_id, book_id):
    user = None
    book = None
    for u in users:
        if u.user_id == user_id:
            user = u
            break
    for b in books:
        if b.book_id == book_id and b.status == "Checked Out":
            book = b
            break
    if user and book:
        user.borrowed_books.remove(book)
        book.status = "Available"
        print(f"You have successfully returned '{book.title}'.")
        return True
    else:
        print("Book is not borrowed or user not found.")
        return False


def search_books(books, query):
    results = []
    for book in books:
        if (
            query.lower() in book.title.lower()
            or query.lower() in book.author.lower()
            or query.lower() in book.genre.lower()
        ):
            results.append(book)
    return results


def view_all_books(books):
    print("All Books:")
    for book in books:
        print(f"{book.book_id}. {book.title} by {book.author} ({book.status})")


def view_available_books(books):
    print("Available Books:")
    for book in books:
        if book.status == "Available":
            print(f"{book.book_id}. {book.title} by {book.author}")


def view_checked_out_books(books):
    print("Checked-Out Books:")
    for book in books:
        if book.status == "Checked Out":
            print(f"{book.book_id}. {book.title} by {book.author}")


def main():
    books = []
    users = []

    while True:
        print("Library Management System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            view_all_books(books)
        elif choice == 2:
            query = input("Enter the book title or author: ")
            results = search_books(books, query)
            if results:
                print("Search results:")
                for book in results:
                    print(
                        f"{book.book_id}. {book.title} by {book.author} ({book.status})"
                    )
            else:
                print("No matching books found.")
        elif choice == 3:
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to borrow: "))
            if borrow_book(books, users, user_id, book_id):
                print("You have successfully borrowed the book.")
            else:
                print("Sorry, the book is currently checked out.")
        elif choice == 4:
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to return: "))
            if return_book(books, users, user_id, book_id):
                print("You have returned the book. Thanks")
            else:
                print("Book is not borrowed or user not found.")
        elif choice == 5:
            print("You Don't have admin Access.")
        elif choice == 6:
            print("Exiting the library system...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
