from models import Book, Storage

book_storage = Storage('books.json')
books = [Book.from_dict(book) for book in book_storage.load()]

def add_book(title, author, isbn):
    new_book = Book(title, author, isbn)
    books.append(new_book)
    save_books()

def list_books():
    for book in books:
        
        print(book.to_dict())

def save_books():
    book_storage.save([book.to_dict() for book in books])
