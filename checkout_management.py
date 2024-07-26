import book_management
import user_management


def checkout_book(user_id, isbn):
    user = get_user(user_id)
    book = get_book(isbn)
    if book.available:
        book.available = False
        user.checked_out_books.append(isbn)
        book_management.save_books()
        user_management.save_users()
        print(f"Book '{book.title}' checked out to user '{user.name}'.")
    else:
        print("Book is not available for checkout.")


def checkin_book(user_id, isbn):
    user = get_user(user_id)
    book = get_book(isbn)
    if not book.available and isbn in user.checked_out_books:
        book.available = True
        user.checked_out_books.remove(isbn)
        book_management.save_books()
        user_management.save_users()
        print(f"Book '{book.title}' checked in from user '{user.name}'.")
    else:
        print("Book is either already available or not checked out by this user.")


def get_book(isbn):
    for book in book_management.books:
        if book.isbn == isbn:
            return book
    raise ValueError("Book not found")


def get_user(user_id):
    for user in user_management.users:
        if user.user_id == user_id:
            return user
    raise ValueError("User not found")
