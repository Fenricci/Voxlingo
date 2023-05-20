from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('5905383196:AAFq39l4sYtgFNvo_mMFRrZd7crbKIrvdzg')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб приложение', web_app=WebAppInfo(url='https://fenricci.github.io/Voxlingo/')))
    await message.answer('Привет!', reply_markup=markup)

executor.start_polling(dp)
