import json


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'available': self.available
        }

    @staticmethod
    def from_dict(data):
        book = Book(data['title'], data['author'], data['isbn'])
        book.available = data['available']
        return book


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.checked_out_books = []

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'checked_out_books': self.checked_out_books
        }

    @staticmethod
    def from_dict(data):
        user = User(data['user_id'], data['name'])
        user.checked_out_books = data.get('checked_out_books', [])
        return user


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
