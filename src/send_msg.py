import requests
import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')


while True:
    requests.get(
        'http://127.0.0.1:5000/SendMessage',
        json={'username': username, 'password': password, 'text': input('Введите свое сообщение: ')})
