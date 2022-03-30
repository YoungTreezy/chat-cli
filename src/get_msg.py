import time
from datetime import datetime

import requests


def GetMessage(message):
    dt = datetime.fromtimestamp(message['timestamp'])
    dt = dt.strftime('%H:%M:%S')
    print(f'{str(dt)} {message["username"]}\n{message["text"]}\n')


after = 0

while True:
    response = requests.get('http://127.0.0.1:5000/GetMessage', params={'after': after})
    messages = response.json()['messages']
    if messages:
        for msg in messages:
            GetMessage(msg)
        after = messages[-1]['timestamp']

