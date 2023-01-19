from aiogram import Bot, executor, Dispatcher, types
import datetime
from bot.api import create_user
from aiogram.types.message import Contact
token = '5839626263:AAH6mCa4c72LBzF5Lj9DiRX7az3AT7SMZqs'

bot = Bot(token=token)
disp = Dispatcher(bot=bot)


@disp.message_handler()
async def record_data(msg: types.Message):
    now = datetime.date.today()
    resp = create_user(now, 'chn?', msg.from_user.id, msg.from_user.username, msg.from_user.first_name,
                       msg.from_user.last_name, 'mail@mail.com', 'mob_number?', 'link?', 'utm_src?', 'utm_camp?',
                       'utm_med?', 'utm_term?', 'utm_cont?', now)
    ms = msg.contact.first_name
    print(ms)
    await msg.answer(resp)  # ECHO


if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)
