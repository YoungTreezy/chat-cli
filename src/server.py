import json
import time
from datetime import datetime

from bson import ObjectId, json_util
from flask import Flask, request
from pymongo import MongoClient


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def connect_to_mongodb():
    client = MongoClient('mongodb://localhost:27017/', username='mongoAdmin', password='12345')
    return client.chat_db


def check_error(username, pwd):
    if username == '' or pwd == '':
        return False
    return True


app = Flask(__name__)
start_time = datetime.now().strftime('%H:%M:%S %d.%m.%Y')


@app.route('/')
def hello():
    return 'Hello, user! Это мессенджер.'


# отправка сообщений
@app.route("/SendMessage")
def SendMessage():
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']
    db = connect_to_mongodb()
    usr = db.users
    msg = db.messages

    if check_error(username, password):
        if usr.find_one({"username": username}):
            if not usr.find_one({"username": username, "password": password}):
                return False
        else:
            usr.insert_one({"username": username, "password": password})
        msg.insert_one({'username': username, 'text': text, 'timestamp': time.time()})

    return {'ok': True}


# получение сообщений
@app.route('/GetMessage')
def GetMessage():
    db = connect_to_mongodb()
    messages = db.messages
    after = float(request.args['after'])
    result = []
    for message in messages.find():
        # msg = loads(dumps(message))
        if message['timestamp'] > after:
            result.append(message)

    return {
        'messages': json.loads(json_util.dumps(result))
    }


app.run()
