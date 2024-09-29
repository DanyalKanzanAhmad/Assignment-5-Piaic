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
    else:
        print("Book is not available or user not found.")


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
    else:
        print("Book is not borrowed or user not found.")


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
        print(
            f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Status: {book.status}"
        )


def view_available_books(books):
    print("Available Books:")
    for book in books:
        if book.status == "Available":
            print(
                f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}"
            )


def view_checked_out_books(books):
    print("Checked-Out Books:")
    for book in books:
        if book.status == "Checked Out":
            print(
                f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}"
            )


def main():
    books = []
    users = []

    while True:
        print("1. Add book")
        print("2. Add user")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Search books")
        print("6. View all books")
        print("7. View available books")
        print("8. View checked-out books")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            add_book(books, book_id, title, author, genre)
        elif choice == 2:
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            add_user(users, user_id, name)
        elif choice == 3:
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_book(books, users, user_id, book_id)
        elif choice == 4:
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter book ID: "))
            return_book(books, users, user_id, book_id)
        elif choice == 5:
            query = input("Enter search query: ")
            results = search_books(books, query)
            if results:
                print("Search results:")
                for book in results:
                    print(
                        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Status: {book.status}"
                    )
            else:
                print("No matching books found.")
        elif choice == 6:
            view_all_books(books)
        elif choice == 7:
            view_available_books(books)
        elif choice == 8:
            view_checked_out_books(books)
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
