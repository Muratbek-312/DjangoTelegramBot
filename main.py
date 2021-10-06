import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

TOKEN = '2014568631:AAGeIOKDxyLbnBv0qNO1QyWkoKKDrHtZRV4'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

activation_code = []

@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    a = requests.post('http://127.0.0.1:8000/account/register/', data={
        'email': f'{message.chat.username}@gmail.com',
        'password': '741852963',
        'password_confirm' : '741852963',
        'name': f'{message.chat.first_name}'
    })
    activation_code.append(a.text)


@dp.message_handler(commands=['activate',])
async def send_welcome(message: types.Message):
    requests.post('http://127.0.0.1:8000/account/activate/', data={
        'email': f'{message.chat.username}@gmail.com',
        'code': activation_code[0][1:-1],
    })

token = {}
@dp.message_handler(commands=['login',])
async def send_welcome(message: types.Message):
    a = requests.post('http://127.0.0.1:8000/account/login/', data={
        'email': f'{message.chat.username}@gmail.com',
        'password': '741852963',
    })
    token['token'] = a.text.split('"')[3]
    print(token)

@dp.message_handler(commands=['create',])
async def send_welcome(message: types.Message):
    requests.post('http://127.0.0.1:8000/publications/', data={
        'title': 'Mongo',
        'text': 'Addushi',
        'user': f'{message.chat.username}@gmail.com',
    }, headers={"Authorization": f'Token {token.get("token")}'})

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)