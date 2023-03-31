from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6172233586:AAF1EdyToa0DpWc3JNgDvfDQGXnrXKkFVxw'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', 'restart'])
async def welcome(message: types.Message):
    rq = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    rq.add(KeyboardButton('Запуск видео'))
    rq.add(KeyboardButton('Выдать скриммер'))
    await message.reply(
        'Привет, устроим взлом ЖЕПЫ?)'
    )
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEIZwNkJxJjU8kQVV4oulNFb2Ddwiy51wAC1AoAAuhO8Uh29Jn8lOf2ii8E',
                           reply_markup=rq
                           )


@dp.message_handler()
async def asshack(message: types.message):
    match message.text:
        case 'Запуск видео':
            pass
        case 'Выдать скриммер':
            pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
