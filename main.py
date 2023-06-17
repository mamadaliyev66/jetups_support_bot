from aiogram import types,Dispatcher,executor,Bot
import datetime
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyD6WsPelDPshTJLVgPIEQgt9BJ4wtjHRUE",
  "authDomain": "pyrebase-eb882.firebaseapp.com",
  "databaseURL": "https://pyrebase-eb882-default-rtdb.firebaseio.com",
  "projectId": "pyrebase-eb882",
  "storageBucket": "pyrebase-eb882.appspot.com",
  "messagingSenderId": "796617670331",
  "appId": "1:796617670331:web:5a40c7c0f7ca259b12339e",
  "measurementId": "G-XM2KJE6FFF"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()


bot_token="6224345380:AAEU7BPUk1f7pluZd3-jhzup7pgPPwypIUI"

bot=Bot(token=bot_token)

dp=Dispatcher(bot=bot)

# await message.answer_photo(
#     photo="https://firebasestorage.googleapis.com/v0/b/pyrebase-eb882.appspot.com/o/support-0.jpg?alt=media&token=1967f0d4-01b1-4f2f-808f-df603645f9eb",
#     caption=""),
#

english=types.InlineKeyboardButton(text='English🇺🇸',callback_data='en')
uzbek=types.InlineKeyboardButton(text='Uzbek🇺🇿',callback_data='uz')
russian=types.InlineKeyboardButton(text='Russian🇷🇺',callback_data='ru')
kb_inline=types.InlineKeyboardMarkup().add(english,uzbek,russian)


eng="Welcome to Jet Ups Support! We're here to assist you with any questions or issues you may have regarding our mini UPS for routers. Whether you need help with setup, troubleshooting, or any other concerns, our team of experts is ready to lend a hand. Just type your question, and we'll provide you with the best possible solution. How can we assist you today?"
uz="Jet Ups Support xizmatiga xush kelibsiz! Biz marshrutizatorlar uchun mini UPS bilan bog'liq har qanday savol yoki muammolar bo'yicha sizga yordam berishga tayyormiz. O‘rnatish, nosozliklarni bartaraf etish yoki boshqa muammolar bo‘yicha yordam kerak bo‘ladimi, bizning mutaxassislarimiz yordam berishga tayyor. Shunchaki savolingizni yozing va biz sizga eng yaxshi yechimni taqdim etamiz. Bugun sizga qanday yordam bera olamiz?"
ru="Добро пожаловать в службу поддержки Jet Ups! Мы здесь, чтобы помочь вам с любыми вопросами или проблемами, которые могут возникнуть в отношении нашего мини-ИБП для маршрутизаторов. Если вам нужна помощь в настройке, устранении неполадок или любых других проблемах, наша команда экспертов готова протянуть руку помощи. Просто введите свой вопрос, и мы предложим вам наилучшее решение. Как мы можем помочь вам сегодня?"

rp_eng="Thank you for reaching out to us. We appreciate your inquiry and value your time. Our team is currently reviewing your request and we will provide a response as soon as possible. Your patience is highly appreciated, and we assure you that we are working diligently to address your concerns. Thank you for choosing our support services."
rp_uz="Bizga murojaat qilganingiz uchun tashakkur. Biz sizning so'rovingizni qadrlaymiz va vaqtingizni qadrlaymiz. Jamoamiz hozirda so‘rovingizni ko‘rib chiqmoqda va imkon qadar tezroq javob beramiz. Sizning sabr-toqatingiz yuqori baholanadi va sizni ishontirib aytamizki, biz sizning tashvishlaringizni hal qilish uchun astoydil harakat qilamiz. Bizning qo'llab-quvvatlash xizmatlarini tanlaganingiz uchun tashakkur."
rp_ru="Спасибо, что связались с нами. Мы ценим ваш запрос и ценим ваше время. Наша команда в настоящее время рассматривает ваш запрос, и мы предоставим ответ как можно скорее. Мы высоко ценим ваше терпение, и мы заверяем вас, что мы усердно работаем над решением ваших проблем. Спасибо, что выбрали нашу службу поддержки."



@dp.message_handler(commands=['start'])
async def Start(message:types.Message):
        await message.answer(
            "Select Language :",reply_markup=kb_inline

        )


default=""


@dp.callback_query_handler(text=['en', 'uz', 'ru'])
async def changelang(call:types.CallbackQuery):
    global default
    global text

    if call.data=='en':
        await call.message.answer(eng)
        default="eng"

    if call.data=='uz':
        await call.message.answer(uz)
        default="uz"

    if call.data=='ru':
        await call.message.answer(ru)
        default="ru"


# print()
@dp.message_handler()
async def AnswerAll(message:types.Message):
    global default
    if default=="uz":
        await message.answer(
            rp_uz
        )
        await bot.send_message(chat_id=1234715065,text=f'User:{message.from_user.full_name}\n\nUsername: @{message.from_user.username}\n\nUser ID:{message.from_user.id}\n\nDate:{datetime.datetime.now()}\n\nText: \n\n{message.text}')
        db.child("Users").push({f"{message.from_user.full_name}": {"user": f"{message.from_user.full_name}", "user_name": f"@{message.from_user.username}", "user_id": f"{message.from_user.id}",
                                          "date": f"{datetime.datetime.now()}", "text": f"{message.text}"}})
    elif default=="eng":
        await message.answer(
            rp_eng
        )
        await bot.send_message(chat_id=1234715065,text=f'User:{message.from_user.full_name}\n\nUsername: @{message.from_user.username}\n\nUser ID:{message.from_user.id}\n\nDate:{datetime.datetime.now()}\n\nText: \n\n{message.text}')
        db.child("Users").push({f"{message.from_user.full_name}": {"user": f"{message.from_user.full_name}",
                                                                   "user_name": f"@{message.from_user.username}",
                                                                   "user_id": f"{message.from_user.id}",
                                                                   "date": f"{datetime.datetime.now()}",
                                                                   "text": f"{message.text}"}})
    elif default=="ru":
        await message.answer(
            rp_ru
        )
        await bot.send_message(chat_id=1234715065,text=f'User:{message.from_user.full_name}\n\nUsername: @{message.from_user.username}\n\nUser ID:{message.from_user.id}\n\nDate:{datetime.datetime.now()}\n\nText: \n\n{message.text}')
        db.child("Users").push({f"{message.from_user.full_name}": {"user": f"{message.from_user.full_name}",
                                                                   "user_name": f"@{message.from_user.username}",
                                                                   "user_id": f"{message.from_user.id}",
                                                                   "date": f"{datetime.datetime.now()}",
                                                                   "text": f"{message.text}"}})
    else:
        await message.answer(
            "Select Language :", reply_markup=kb_inline

        )

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False)

