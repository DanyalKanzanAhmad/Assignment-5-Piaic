class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


def add_book(books, title, author, genre):
    new_book = Book(title, author, genre)
    books.append(new_book)


def view_books(books):
    for book in books:
        print(
            f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Available: {book.is_available}"
        )


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


def borrow_book(books, users, user_name, book_title):
    user = None
    book = None
    for u in users:
        if u.name == user_name:
            user = u
            break
    for b in books:
        if b.title == book_title and b.is_available:
            book = b
            break
    if user and book:
        user.borrowed_books.append(book)
        book.is_available = False
        print(f"You have successfully borrowed '{book.title}'.")
    else:
        print("Book is not available or user not found.")


def return_book(books, users, user_name, book_title):
    user = None
    book = None
    for u in users:
        if u.name == user_name:
            user = u
            break
    for b in books:
        if b.title == book_title and not b.is_available:
            book = b
            break
    if user and book:
        user.borrowed_books.remove(book)
        book.is_available = True
        print(f"You have successfully returned '{book.title}'.")
    else:
        print("Book is not borrowed or user not found.")


def add_user(users, name):
    new_user = User(name)
    users.append(new_user)


def main():
    books = []
    users = []

    while True:
        print("1. Add book")
        print("2. View books")
        print("3. Search books")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Add user")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            add_book(books, title, author, genre)
        elif choice == 2:
            view_books(books)
        elif choice == 3:
            query = input("Enter search query: ")
            results = search_books(books, query)
            if results:
                print("Search results:")
                for book in results:
                    print(
                        f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Available: {book.is_available}"
                    )
            else:
                print("No matching books found.")
        elif choice == 4:
            user_name = input("Enter your name: ")
            book_title = input("Enter book title: ")
            borrow_book(books, users, user_name, book_title)
        elif choice == 5:
            user_name = input("Enter your name: ")
            book_title = input("Enter book title: ")
            return_book(books, users, user_name, book_title)
        elif choice == 6:
            name = input("Enter user name: ")
            add_user(users, name)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
