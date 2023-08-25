from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO) 

direction_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('объекты'),
    types.KeyboardButton('Контакты')
]
direction_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*direction_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f'Здраствуйте {message.from_user.full_name}!\nВыберите одно из кнопок', reply_markup=direction_keyboard)
                         
@dp.message_handler(text='О нас')
async def about_Us(message:types.Message):
    await message.reply("""Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в объектах расположенных во всех
наиболее привлекательных районах городов Ош и Джалал-Абад. У нас максимально выгодные условия, гибкий (индивидуальный) подход при реализации
жилой и коммерческой недвижимости. Мы занимаем лидирующие позиции по количеству объектов по югу Кыргызстана. Наша миссия: Мы обеспечиваем население
удобным жильем для всей семьи, проявляя лояльность и индивидуальный подход и обеспечивая высокий уровень обслуживания.
Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и опыт профессионалов своего дела.""")
    
@dp.message_handler(text='объекты')
async def objects(message:types.Message):
    await message.reply("""ЖК «Фрунзе»
г.Ош, Ленина 170

ЖК «Черемушки»
г.Ош, ул. Урицкого 15Б

ЖК «Томирис»
г. Ош, ул. Аматова 1 (ориентир - Драм. театр)

ЖК «Малина-Лайф»
г.Ош, ул Монуева 19""")
    
@dp.message_handler(text='Контакты')
async def contacts(message:types.Message):
    await message.reply("""г.Ош, ул.Аматова 1, Бизнес центр Томирис

contact@vg-stroy.com
+996 709 620088
+996 772 620088
+996 550 620088""")
    
executor.start_polling(dp)