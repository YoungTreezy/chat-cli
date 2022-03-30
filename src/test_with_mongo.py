from pymongo import MongoClient


def connect_to_mongo():
    client = MongoClient('mongodb://localhost:27017/', username='mongoAdmin', password='12345')
    return client.chat_db


users = [
    {"username": "name1", "password": "pwd1"},
    {"username": "name2", "password": "pwd2"},
    {"username": "name3", "password": "pwd3"},
    {"username": "name4", "password": "pwd4"},
    {"username": "name5", "password": "pwd5"},
]


def add_new_user():
    db = connect_to_mongo()
    user = db.users
    user.insert_many(users)


def print_messages():
    db = connect_to_mongo()
    users = db.messages.find()
    for user in users:
        print(user['username'], user['text'])


if __name__ == '__main__':
    print_messages()
