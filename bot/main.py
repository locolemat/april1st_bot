from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from ASS_hack.main import *
API_TOKEN = '6172233586:AAF1EdyToa0DpWc3JNgDvfDQGXnrXKkFVxw'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

Список_комманд = '''
Тут
будет
список
команд
'''

@dp.message_handler(commands=['start', 'help', 'restart'])
async def welcome(message: types.Message):
    await message.reply(
        'Привет, устроим взлом ЖЕПЫ?)'
    )
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEIZwNkJxJjU8kQVV4oulNFb2Ddwiy51wAC1AoAAuhO8Uh29Jn8lOf2ii8E')
    await bot.send_message(chat_id=message.chat.id, text=Список_комманд)


@dp.message_handler()
async def asshack(message: types.message):
    command, params = str(message.text).split(';')
    params = list(map(str, params.split('|')))
    match command:
        case 'Открыть терминал':
            pass
        case 'Выдать скриммер':
            pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
