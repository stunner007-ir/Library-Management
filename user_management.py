from models import User, Storage

user_storage = Storage('users.json')
users = [User.from_dict(user) for user in user_storage.load()]

def add_user(user_id, name):
    new_user = User(user_id, name)
    users.append(new_user)
    save_users()

def list_users():
    for user in users:
        print(user.to_dict())

def save_users():
    user_storage.save([user.to_dict() for user in users])
