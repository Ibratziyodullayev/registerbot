import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, executor, types
from btn import start_menu_btn, info_yes_or_no_btn # * ni qoyib qoysa hammasini import qiladi
from aiogram.dispatcher import FSMContext #A1

BOT_TOKEN  = '6065611149:AAHr5oguNSkgfM7JuLbLQ0CqUq0Zn8i09uQ'


logging.basicConfig(level = logging.INFO)
# bot = Bot(token=BOT_TOKEN, parse_mode='html')
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot = bot, storage=storage )

info = {
    'name' : '', #dic.
    'age' : 0,
    'adres' : ''
}

class ManingStatlarim(StatesGroup):
    ism = State()#honala
    yosh = State()
    adres = State()

@dp.message_handler(commands=['start'])# NIKNI TASHAB BERADI
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.from_user.first_name, msg.from_user.can_join_groups)

 
# @dp.callback_query_handler(text='user_id') USERni ID sini chiqarib beradi
# async def user_id_inline_callback(callback_query: types.CallbackQuery):
#     await callback_query.answer(f"Ваш ID: {callback_query.from_user.id}", True)


# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     btn = await start_menu_btn()
#     # await message.answer("<a href='t.me/winchestor_dev'>Salom</a>", disable_web_page_preview=True)
#     await message.answer('<b>Salom</b>', reply_markup=btn)
    # await message.answer("<em>Salom</em>")
    # await message.answer("<i>Salom</i>")

@dp.message_handler(text = "👤Admin bilan bog'lanish")
async def support_handler(message: types.Message):
    await message.answer('Bot admini: @ibrat_xs')

@dp.message_handler(text = "📝royhattan o'tish")
async def user_register_handler(message: types.Message):
    await message.answer('Ismingizni kiriring 👨‍⚕️')
    await ManingStatlarim.ism.set()

@dp.message_handler(state = ManingStatlarim.ism) #user kiritgan ismni ManingStatlarim,ism ga saqlidi
async def ism_state(message: types.Message):

    info['name'] = message.text #user kiridgan ismni dic. ga qoshib chiqarib beradi

    await message.answer('Yoshingizni kiriting 👨🏻‍💻')
    await ManingStatlarim.yosh.set()

@dp.message_handler(state = ManingStatlarim.yosh) #user kiritgan yoshni ManingStatlarim,yosh ga saqlidi
async def yosh_state(message: types.Message):

    info['age'] = message.text 

    await message.answer('adressingizni kiriting 👨🏻‍💻')
    await ManingStatlarim.adres.set()

@dp.message_handler(state = ManingStatlarim.adres) 
async def adres_state(message: types.Message, state: FSMContext):#FINISH QILISH yena malumod qoshvurish uchun A1

    info['adres'] = message.text 
    print(info)

    btn = await info_yes_or_no_btn()

    await message.answer(f"ISM: {info['name']}\nYOSH: {info['age']}\nMANZIL: {info['adres']}", reply_markup=btn)# user kiritgan malumotlarni user ga qaytarib tashab beradi

    await state.finish() #A1

@dp.callback_query_handler(text = 'yes') #INLAYN KNOPKA UCHUN FAQAT   
async def answer_yes_callback(call: types.CallbackQuery):
    # await call.answer('Siz rozi boldingiz!', show_alert=True)
    btn = await start_menu_btn()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('SIz royhatdan otdingiz!', reply_markup=btn)
    

async def answer_no_callback(call: types.CallbackQuery):
    btn = await start_menu_btn()
    await call.message.delete()# habarri ochiradi
    await call.message.answer('SIz royhatdan otmadingiz!', reply_markup=btn)
    # await call.answer('Siz rozi bolmadingiz!', show_alert=True)



if __name__ == '__main__':
    executor.start_polling(dp)

    #start bosganda userni ismi bilan user name sini jonatishi kere 