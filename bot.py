from googletrans import Translator
from committ import *
import sqlite3

import logging
from button import *
from aiogram.types import CallbackQuery
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
tr = Translator()
Admin = ""

###### foydalanuvchilar sonini tekshirish
@dp.message_handler(commands=['alluser'],user_id="")
async def send_welcome(message: types.Message):
    connection = sqlite3.connect("users_info1.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT COUNT(id) FROM user ")
    data = cursor.fetchall()
    for i in data:
       x = i[0]
    await message.reply(f"Foydalanuvchilar soni {x} ta")    


######## adminga habar berish 
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    connection = sqlite3.connect("users_info1.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user(
        id INTEGER
    )""")
    connection.commit()

    tekshirish = message.chat.id
    cursor.execute(f"SELECT id FROM user WHERE id = {tekshirish}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]

        cursor.execute("INSERT INTO user VALUES (?)",user_id)
        connection.commit()
        await message.reply("Assalomu aleykum!😊\n\nSo'z kiriting")
        await bot.send_message(Admin,f"✅Ro'yxatga qo'shildi: \nusername: @{message.from_user.username}\nid: {message.from_user.id}\nYozayotgan xabari: {message.text}")
    else:
        await message.reply("Siz ro'yxatdan o'tgansiz")    

@dp.message_handler(commands=['delete'])
async def send_welcome(message: types.Message):
    connection = sqlite3.connect("users_info1.db")
    cursor = connection.cursor()

    tekshirish = message.chat.id
    cursor.execute(f"SELECT id FROM user WHERE id = {tekshirish}")
    data = cursor.fetchone()
    if data is None:
        pass
    else:
        Uchirish = message.chat.id
        cursor.execute(f"DELETE from user WHERE id = {Uchirish}")
        connection.commit()
        await message.reply("Siz ro'yxatdan o'chirildingiz!")
        await bot.send_message(Admin,f"✅Ro'yxatdan o'chirildingiz: \nusername: @{message.from_user.username}\nid: {message.from_user.id}")


@dp.message_handler()
async def echo(message: types.Message):
    global t
    t = message.text
    await message.reply("Tilni tanlang",  reply_markup = tillar)


########### rus til 
@dp.callback_query_handler(text = "ru")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "ru")
    await call.message.reply(f"Rus tilida 🇷🇺: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()

############ english til 
@dp.callback_query_handler(text = "en")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "en")
    await call.message.reply(f"Inglis tilida 🇺🇸: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()

########## uzb til 
@dp.callback_query_handler(text = "uz")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "uz")
    await call.message.reply(f"Uzbek tilida 🇺🇿: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()

########## turk til 
@dp.callback_query_handler(text = "tr")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "tr")
    await call.message.reply(f"Turk tilida 🇹🇷: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()

########## arab til 
@dp.callback_query_handler(text = "ar")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "ar")
    await call.message.reply(f"Arab tilida 🇦🇪: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()

########## azarbayjan til 
@dp.callback_query_handler(text = "az")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "az")
    await call.message.reply(f"Azarbayjon tilida 🇦🇿: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


########## Qozoq til 
@dp.callback_query_handler(text = "tg")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "tg")
    await call.message.reply(f"Qozoq tilida 🇰🇿: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


########## ispan til 
@dp.callback_query_handler(text = "es")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "es")
    await call.message.reply(f"Ispan tilida 🇪🇸: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


########## xitoy til 
@dp.callback_query_handler(text = "zh-tw")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "zh-tw")
    await call.message.reply(f"Xitoy tilida 🇨🇳: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


########## armiyan tili  til 
@dp.callback_query_handler(text = "hy")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "hy")
    await call.message.reply(f"Arman tilida 🇦🇲: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### fransiya tili 
@dp.callback_query_handler(text = "fr")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "fr")
    await call.message.reply(f"Fransiya tilida 🇫🇷: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()



###### germaniya tili 
@dp.callback_query_handler(text = "de")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "de")
    await call.message.reply(f"Germaniya tilida 🇩🇪: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### hind tili 
@dp.callback_query_handler(text = "hi")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "hi")
    await call.message.reply(f"Hind tilida 🇮🇳: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### yaponiya tili 
@dp.callback_query_handler(text = "ja")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "ja")
    await call.message.reply(f"Yaponiya tilida 🇯🇵: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### Canada tili 
@dp.callback_query_handler(text = "kn")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "kn")
    await call.message.reply(f"Canada tilida 🇨🇦: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### kareya tili 
@dp.callback_query_handler(text = "ko")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "ko")
    await call.message.reply(f"Kareya tilida 🇰🇷: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### serbiya tili 
@dp.callback_query_handler(text = "sr")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "sr")
    await call.message.reply(f"Serbiya tilida 🇷🇸: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()

###### slovekia  tili 
@dp.callback_query_handler(text = "sl")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "sl")
    await call.message.reply(f"Slovekiya tilida 🇸🇰: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### italia   tili 
@dp.callback_query_handler(text = "it")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "it")
    await call.message.reply(f"Italiya tilida 🇮🇹: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()


###### qirgiziston  tili 
@dp.callback_query_handler(text = "ky")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "ky")
    await call.message.reply(f"Qirg'iz tilida 🇰🇬: \n{tarjima.text}", reply_markup=tillar)
    await call.message.delete()

 
###### belarusian  tili 
@dp.callback_query_handler(text = "be")
async def fo(call: CallbackQuery):
    tarjima = tr.translate(t, dest = "be")
    await call.message.reply(f"Belarus tilida 🇧🇾: \n{tarjima.text}", reply_markup=tillar) 
    await call.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




