import book_management
import user_management
import checkout_management

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Checkin Book")
    print("6. List Checked Out Books by User")
    print("7. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_management.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            book_management.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_management.add_user(user_id, name)
            print("User added.")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_management.checkout_book(user_id, isbn)
        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            checkout_management.checkin_book(user_id, isbn)
        elif choice == '6':
            user_id = input("Enter user ID: ")
            user = checkout_management.get_user(user_id)
            print(f"Books checked out by user '{user.name}': {user.checked_out_books}")
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
