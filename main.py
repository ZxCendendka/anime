import logging, asyncio, nekos, random, os, configure
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import Throttled
from datetime import datetime, timedelta
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
#from configure import TOKEN, sticker
storage = MemoryStorage()

bot = Bot(token=configure.TOKEN)
dp = Dispatcher(bot, storage=storage)
logchat = -2191103294

keyboard = types.InlineKeyboardMarkup(row_width=3)
keyboard.add(types.InlineKeyboardButton(text='🐱 неко', callback_data='neko'), types.InlineKeyboardButton(text='💋 цем', callback_data='kiss'))
keyboard.add(types.InlineKeyboardButton(text='🐱 неко (Gif)', callback_data='neko_gif'), types.InlineKeyboardButton(text='🤗 обнимашки (Gif)', callback_data='hug_gif'))
keyboard.add(types.InlineKeyboardButton(text='🌌 обои', callback_data='wallpaper'), types.InlineKeyboardButton(text='🎆 аватарка', callback_data='avatar'))
types.InlineKeyboardMarkup(row_width=3)

async def anti_flood(*args, **kwargs):
    m = args[0]
    return

@dp.message_handler(commands=['ping'])
@dp.throttled(rate=2)
async def send_ping(message: types.Message):
    a = 5
    r = message.get_args()
    if r and r[0].isdigit():
        a = int(r[0])
    ping_msg = []
    ping_data = []
    for _ in range(a):
        start = datetime.now()
        msg = await bot.send_message(logchat, "ping")
        end = datetime.now()
        duration = (end - start).microseconds / 1000
        ping_data.append(duration)
        ping_msg.append(msg)
    ping = sum(ping_data) / len(ping_data)
    await message.reply(f"🏓 Пинг: {str(ping)[0:5]} ms.")
    for i in ping_msg:
        await i.delete()

@dp.message_handler(commands=['start'])
async def command_handler(message: types.Message):
    await message.answer_sticker(sticker=configure.sticker)
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await message.answer(f"{emoji} Привет, я бот который может помочь тебе найти аниме-авы и аниме-обои! \n💻 Разработчик: @zxcendechka_off", reply_markup=keyboard, parse_mode='html')

@dp.message_handler()
async def commands(message: types.Message):
    if message.text.lower() in ["/start"]: 
       pass
    if message.text.lower() in ["Я люблю тебя", "Я тебя люблю", "я люблю тебя", "я тебя люблю"]: 
       await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEE3_hilG04X8016yn0kG_2EIexwYGE2AACMxQAAlPryUvGOIcObQL_FCQE')
       await bot.send_message(message.chat.id, "Я тебя тоже очень люблю! ❤")
       await bot.send_video(message.chat.id, 'https://media.giphy.com/media/a3SQF6Peo1aDMXnJ31/giphy.gif')

    else:
       await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEMarZmhDWX4TwNwcRdQzER1VNxvAm-cAACRVMAAuCjggfdCj_No8iXpzUE')
       await bot.send_message(message.chat.id, "Я тебя не понимаю( 😣")
       await bot.send_animation(message.chat.id, open('/home/путь/на/вдске/gif.gif', 'rb'))

@dp.callback_query_handler(lambda c: c.data == "neko")
async def neko(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_photo(callback_query.message.chat.id, nekos.img('neko'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи фоточку)")

@dp.callback_query_handler(lambda c: c.data == "summer")
async def neko(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.message.chat.id, open('/home/путь/на/вдске/gif.gif', 'rb'), reply_markup=summerboard)

@dp.callback_query_handler(lambda c: c.data == "miku")
async def miku(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    DIR = "/home/путь/на/вдске/gif.gif/Miku" 
    photo = open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    await bot.send_photo(callback_query.message.chat.id, photo, f"{photo}", reply_markup=summerboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи артик)")

@dp.callback_query_handler(lambda c: c.data == "lena")
async def lena(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    DIR = "/home/путь/на/вдске/gif.gif/Lena"  
    photo = open(os.path.join(DIR, random.choice(os.listdir(DIR))), 'rb')
    await bot.send_photo(callback_query.message.chat.id, photo, f"{photo}", reply_markup=summerboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи артик)")


@dp.callback_query_handler(lambda c: c.data == "kiss")
async def kiss(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_video(callback_query.message.chat.id, nekos.img('kiss'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи фоточку)")

@dp.callback_query_handler(lambda c: c.data == "neko_gif")
async def neko_gif(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_video(callback_query.message.chat.id, nekos.img('ngif'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи гифку)")

@dp.callback_query_handler(lambda c: c.data == "hug_gif")
async def hug_gif(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_video(callback_query.message.chat.id, nekos.img('hug'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи гифку)")

@dp.callback_query_handler(lambda c: c.data == "wallpaper")
async def wallpaper(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_photo(callback_query.message.chat.id, nekos.img('wallpaper'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи обои)")

@dp.callback_query_handler(lambda c: c.data == "avatar")
async def avatar(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_photo(callback_query.message.chat.id, nekos.img('avatar'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} Держи аватарочку)")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
