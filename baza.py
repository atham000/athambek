import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
 
# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    connection = sqlite3.connect("users_info1.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user(
        id varchar(15)
    )""")
    connection.commit()


    user_id = [message.chat.id]

    cursor.execute("INSERT INTO user VALUES (?)",user_id)
    connection.commit()
    await message.reply("Assalomu aelykum!😊")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





