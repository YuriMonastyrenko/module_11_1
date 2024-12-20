# requests — это библиотека для отправки HTTP-запросов, которая упрощает взаимодействие с веб-ресурсами.
import requests

# 1. GET-запросы используются для получения данных с сервера.
# Пример:

response = requests.get('https://api.github.com/events')
print(response.status_code)  # Выводит код состояния ответа
print(response.text)  # Выводит содержимое ответа

# 2. POST-запросы используются для отправки данных на сервер.
# Пример:

data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())  # Выводит ответ в формате JSON

# 3.Можно передавать параметры в URL, используя словарь.
# Пример:

params = {'key': 'API_KEY', 'text': 'Hello', 'lang': 'en-es'}
response = requests.get('https://api.example.com/translate', params=params)
print(response.text)  # Выводит текст ответа

# 4. Можно добавлять и изменять заголовки запроса:
# Пример:

headers = {'Authorization': 'Bearer YOUR_TOKEN'}
response = requests.get('https://api.example.com/data', headers=headers)
print(response.headers)  # Выводит заголовки ответа

# 5.Requests позволяет обрабатывать ошибки, возникающие при выполнении запросов:
# Пример:

try:
    response = requests.get('https://api.github.com/invalid-url')
    response.raise_for_status()  # Вызывает ошибку для статусов 4xx и 5xx
except requests.exceptions.HTTPError as err:
    print(f'Ошибка: {err}')