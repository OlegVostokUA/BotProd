from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from database import sqlite_db
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

class FSMClient(StatesGroup):
    name_div = State()
    all_sm = State()
    solders_sm = State()
    sm_for_lunch = State()
    dogs = State()
    dogs_food_norm = State()
    meat_carc = State()
    meat_blocks = State()
    meat_chicken = State()
    sausage = State()
    liver = State()
    cons_meat = State()
    cons_meat_veg = State()
    fish_hake = State()
    fish_pike = State()
    fish_pollock = State()
    fish_smoked = State()
    cons_fish = State()
    fat = State()  # salo
    honey = State()
    jam = State()
    butter = State()
    oil = State()
    marg_fat = State()
    cheese = State()
    sugar = State()
    egg = State()
    rice = State()
    buckwheat = State()  # grech
    millet = State()  # pshono
    pears = State()  # goroh
    barley = State()  # yachka
    pearl = State()  # perlov
    wheat = State()  # pshenych
    corn = State()
    bulgur = State()
    pasta = State()
    wheat_fl_first = State()  # muka
    tea = State()
    salt = State()
    pepper = State()
    l_list = State()
    g_porokh = State()
    vinegar = State()
    tomat_pasta = State()
    dried_fruits = State()
    juice = State()
    fresh_fruits = State()
    potato = State()
    cabbage_fr = State()
    cabbage_ferm = State()
    cabbage_cons = State()
    carrot_fr = State()
    carrot_cons = State()
    beet_fr = State()
    beet_cons = State()
    onion_on = State()  # luk
    onion_fr = State()
    cucumbers_fr = State()
    cucumbers_ferm = State()
    cucumbers_cons = State()
    cons_peas = State()
    veg_salads = State()
    yeast = State()  # drizhzhzy
    water = State()
    gecsav = State()
    dry_milk = State()
    biscuit = State()  # pechenye
    DSP_10 = State()
    DSP_15 = State()
    dog_food = State()
    detergent = State()
    s_name = State()


class FSMRequest(StatesGroup):
    name_div_r = State()
    request_div = State()
    s_name_r = State()



async def start_request(message: types.Message):
    await FSMRequest.name_div_r.set()
    await message.answer('Введіть назву підрозділу')


async def input_name_div_r(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name_div_r'] = message.text
    await FSMRequest.next()
    await message.answer('Введіть потребу у прод. (ПРИКЛАД: м’ясо - 50кг, риба - 100кг, ...)')


async def input_reuest(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['request_div'] = message.text
    await FSMRequest.next()
    await message.answer('Введіть прізвище')

async def input_s_name_r(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['s_name_r'] = message.text
    await sqlite_db.sql_cl_add_command_r(state)
    await state.finish()
    await message.answer('Дякую. Заявка подана')
    await bot.send_message(1064924678, 'У вас нова заявка')



# @dp.message_handler(commands='Залишки', State=None)
async def start_order(message: types.Message):
    await FSMClient.name_div.set()
    await message.answer('Введіть назву підрозділу')

# @dp.message_handler(state=FSMClient.name_cl)
async def input_name_div(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name_div'] = message.text
    await FSMClient.next()
    await message.answer('Введіть кількість о/с які перебувають на харчуванні(чол.)')

# @dp.message_handler(state=FSMClient.goods)
async def input_all_sm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['all_sm'] = message.text
    await FSMClient.next()
    await message.answer('Введіть кількість строковиків які перебувають на харчуванні(чол.)')

# @dp.message_handler(state=FSMClient.address)
async def input_solders_sm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['solders_sm'] = message.text
    await FSMClient.next()
    await message.answer('Введіть кількість о/с які харчуються на обід(чол.)')

async def input_sm_for_lunch(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['sm_for_lunch'] = message.text
    await FSMClient.next()
    await message.answer('Введіть кількість сл. собак які перебувають на харчуванні(гол.)')

async def input_dogs(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dogs'] = message.text
    await FSMClient.next()
    await message.answer('Введіть середню (за день) кількість корму, яка використовуєтся для харч сл. собак(кг.)')

async def input_dogs_food_norm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dogs_food_norm'] = message.text
    await FSMClient.next()
    await message.answer('Введіть кількість наявного продовольства: м’ясо (тущі, напівтущі, чверть)(кг.)')

async def input_meat_carc(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['meat_carc'] = message.text
    await FSMClient.next()
    await message.answer('М’ясні блоки (кг.)')

async def input_meat_blocks(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['meat_blocks'] = message.text
    await FSMClient.next()
    await message.answer('М’ясо птиці (кг.)')

async def input_meat_chicken(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['meat_chicken'] = message.text
    await FSMClient.next()
    await message.answer('Сосиски, сардельки (кг.)')

async def input_sausage(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['sausage'] = message.text
    await FSMClient.next()
    await message.answer('Печінка (кг.)')

async def input_liver(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['liver'] = message.text
    await FSMClient.next()
    await message.answer('Консерви м’ясні (кг.)')

async def input_cons_meat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_meat'] = message.text
    await FSMClient.next()
    await message.answer('Консерви м’ясорослинні (кг.)')

async def input_cons_meat_veg(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_meat_veg'] = message.text
    await FSMClient.next()
    await message.answer('Риба: Хек (кг.)')

async def input_fish_hake(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_hake'] = message.text
    await FSMClient.next()
    await message.answer('Сайда (кг.)')

async def input_fish_pike(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_pike'] = message.text
    await FSMClient.next()
    await message.answer('Минтай (кг.)')

async def input_fish_pollock(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_pollock'] = message.text
    await FSMClient.next()
    await message.answer('Риба копчена, вялена (кг.)')

async def input_fish_smoked(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_smoked'] = message.text
    await FSMClient.next()
    await message.answer('Консерви рибні (кг.)')

async def input_cons_fish(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_fish'] = message.text
    await FSMClient.next()
    await message.answer('Сало (кг.)')

async def input_fat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fat'] = message.text
    await FSMClient.next()
    await message.answer('Мед (кг.)')

async def input_honey(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['honey'] = message.text
    await FSMClient.next()
    await message.answer('Джем (кг.)')

async def input_jam(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['jam'] = message.text
    await FSMClient.next()
    await message.answer('Масло вершкове (кг.)')

async def input_butter(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['butter'] = message.text
    await FSMClient.next()
    await message.answer('Олія (кг.)')

async def input_oil(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['oil'] = message.text
    await FSMClient.next()
    await message.answer('Маргарин (кг.)')

async def input_marg_fat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['marg_fat'] = message.text
    await FSMClient.next()
    await message.answer('Сир (кг.)')

async def input_cheese(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cheese'] = message.text
    await FSMClient.next()
    await message.answer('Цукор (кг.)')

async def input_sugar(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['sugar'] = message.text
    await FSMClient.next()
    await message.answer('Яйце (шт.)')

async def input_egg(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['egg'] = message.text
    await FSMClient.next()
    await message.answer('Крупи: Рис (кг.)')

async def input_rice(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['rice'] = message.text
    await FSMClient.next()
    await message.answer('Гречана (кг.)')

async def input_buckwheat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['buckwheat'] = message.text
    await FSMClient.next()
    await message.answer('Пшоно (кг.)')

async def input_millet(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['millet'] = message.text
    await FSMClient.next()
    await message.answer('Горох (кг.)')

async def input_pears(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pears'] = message.text
    await FSMClient.next()
    await message.answer('Ячнева (кг.)')

async def input_barley(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['barley'] = message.text
    await FSMClient.next()
    await message.answer('Перлова (кг.)')

async def input_pearl(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pearl'] = message.text
    await FSMClient.next()
    await message.answer('Пшенична (кг.)')

async def input_wheat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['wheat'] = message.text
    await FSMClient.next()
    await message.answer('Кукурудзяна (кг.)')

async def input_corn(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['corn'] = message.text
    await FSMClient.next()
    await message.answer('Булгур (кг.)')

async def input_bulgur(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['bulgur'] = message.text
    await FSMClient.next()
    await message.answer('Макаронні вироби (кг.)')

async def input_pasta(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pasta'] = message.text
    await FSMClient.next()
    await message.answer('Борошно пшен І гат. (кг.)')

async def input_wheat_fl_first(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['wheat_fl_first'] = message.text
    await FSMClient.next()
    await message.answer('Чай (кг.)')

async def input_tea(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['tea'] = message.text
    await FSMClient.next()
    await message.answer('Сіль (кг.)')

async def input_salt(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['salt'] = message.text
    await FSMClient.next()
    await message.answer('Перець (кг.)')

async def input_pepper(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pepper'] = message.text
    await FSMClient.next()
    await message.answer('Лавр. лист (кг.)')

async def input_l_list(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['l_list'] = message.text
    await FSMClient.next()
    await message.answer('Гірч. порошок (кг.)')

async def input_g_porokh(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['g_porokh'] = message.text
    await FSMClient.next()
    await message.answer('Оцет (кг.)')

async def input_vinegar(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['vinegar'] = message.text
    await FSMClient.next()
    await message.answer('Томат паста (кг.)')

async def input_tomat_pasta(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['tomat_pasta'] = message.text
    await FSMClient.next()
    await message.answer('Сухофрукти (кг.)')

async def input_dried_fruits(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dried_fruits'] = message.text
    await FSMClient.next()
    await message.answer('Соки плодово-ягідні (кг.)')

async def input_juice(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['juice'] = message.text
    await FSMClient.next()
    await message.answer('Фрукти свіжі (кг.)')

async def input_fresh_fruits(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fresh_fruits'] = message.text
    await FSMClient.next()
    await message.answer('Картопля (кг.)')

async def input_potato(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['potato'] = message.text
    await FSMClient.next()
    await message.answer('Капуста свіжа (кг.)')

async def input_cabbage_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cabbage_fr'] = message.text
    await FSMClient.next()
    await message.answer('Капуста маринована (кг.)')

async def input_cabbage_ferm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cabbage_ferm'] = message.text
    await FSMClient.next()
    await message.answer('Капуста конс. (кг.)')

async def input_cabbage_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cabbage_cons'] = message.text
    await FSMClient.next()
    await message.answer('Морква свіжа (кг.)')

async def input_carrot_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['carrot_fr'] = message.text
    await FSMClient.next()
    await message.answer('Морква конс. (кг.)')

async def input_carrot_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['carrot_cons'] = message.text
    await FSMClient.next()
    await message.answer('Буряк свіжий (кг.)')

async def input_beet_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['beet_fr'] = message.text
    await FSMClient.next()
    await message.answer('Буряк конс. (кг.)')

async def input_beet_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['beet_cons'] = message.text
    await FSMClient.next()
    await message.answer('Цибуля ріпчаста (кг.)')

async def input_onion_on(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['onion_on'] = message.text
    await FSMClient.next()
    await message.answer('Цибуля (перо) (кг.)')

async def input_onion_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['onion_fr'] = message.text
    await FSMClient.next()
    await message.answer('Огірки свіжі (кг.)')

async def input_cucumbers_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cucumbers_fr'] = message.text
    await FSMClient.next()
    await message.answer('Огірки марин. (кг.)')

async def input_cucumbers_ferm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cucumbers_ferm'] = message.text
    await FSMClient.next()
    await message.answer('Огірки конс. (кг.)')

async def input_cucumbers_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cucumbers_cons'] = message.text
    await FSMClient.next()
    await message.answer('Консерв. горошок, квасоля (кг.)')

async def input_cons_peas(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_peas'] = message.text
    await FSMClient.next()
    await message.answer('Салати овочеві (кг.)')

async def input_veg_salads(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['veg_salads'] = message.text
    await FSMClient.next()
    await message.answer('Дріжджі (кг.)')

async def input_yeast(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['yeast'] = message.text
    await FSMClient.next()
    await message.answer('Вода (л.)')

async def input_water(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['water'] = message.text
    await FSMClient.next()
    await message.answer('Гексавіт (драже)')

async def input_gecsav(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['gecsav'] = message.text
    await FSMClient.next()
    await message.answer('Молоко сухе (кг.)')

async def input_dry_milk(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dry_milk'] = message.text
    await FSMClient.next()
    await message.answer('Печиво (кг.)')

async def input_biscuit(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['biscuit'] = message.text
    await FSMClient.next()
    await message.answer('ПНСП (норма 10) (к-т.)')

async def input_DSP_10(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['DSP_10'] = message.text
    await FSMClient.next()
    await message.answer('ПНСП (норма 15) (к-т.)')

async def input_DSP_15(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['DSP_15'] = message.text
    await FSMClient.next()
    await message.answer('Корм для сл. собак (кг.)')

async def input_dog_food(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dog_food'] = message.text
    await FSMClient.next()
    await message.answer('Миючий засіб (кг.)')

async def input_detergent(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['detergent'] = message.text
    await FSMClient.next()
    await message.answer('Введіть прізвище')

# @dp.message_handler(state=FSMClient.telephone)
async def input_s_name(message: types.Message, state:FSMContext):

   # user

    async with state.proxy() as data:
        data['s_name'] = message.text
    await sqlite_db.sql_cl_add_command(state)
    await state.finish()
    await message.answer('Дякую. Залишки подані')
   # await bot.send_message(message.from_user.username)


# @dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, 'Слава Україні! Оберіть розділ', reply_markup=kb_client)
    await message.delete()

# @dp.message_handler(commands=['help'])
async def command_help(message:types.Message):
    await bot.send_message(message.from_user.id, 'Хочешь что то? Бот в помощь))')
    await message.delete()


async def command_shop_open(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бот доступний:\nПн-Пт-8:30-17:30,\nСб-9:30-13:30,\nНд-Вихідний')


async def assort_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'На даний час на складі УПЗ в наявності наступні види продовольства:')
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_shop_open, commands=['Робочі_години'])

    dp.register_message_handler(assort_command, commands=['Наявність_прод'])

    dp.register_message_handler(start_request, commands='Заявка_прод', State=None)
    dp.register_message_handler(input_name_div_r, state=FSMRequest.name_div_r)
    dp.register_message_handler(input_reuest, state=FSMRequest.request_div)
    dp.register_message_handler(input_s_name_r, state=FSMRequest.s_name_r)

    dp.register_message_handler(start_order, commands='Залишки', State=None)
    dp.register_message_handler(input_name_div, state=FSMClient.name_div)
    dp.register_message_handler(input_all_sm, state=FSMClient.all_sm)
    dp.register_message_handler(input_solders_sm, state=FSMClient.solders_sm)
    dp.register_message_handler(input_sm_for_lunch, state=FSMClient.sm_for_lunch)
    dp.register_message_handler(input_dogs, state=FSMClient.dogs)
    dp.register_message_handler(input_dogs_food_norm, state=FSMClient.dogs_food_norm)
    dp.register_message_handler(input_meat_carc, state=FSMClient.meat_carc)
    dp.register_message_handler(input_meat_blocks, state=FSMClient.meat_blocks)
    dp.register_message_handler(input_meat_chicken, state=FSMClient.meat_chicken)
    dp.register_message_handler(input_sausage, state=FSMClient.sausage)
    dp.register_message_handler(input_liver, state=FSMClient.liver)
    dp.register_message_handler(input_cons_meat, state=FSMClient.cons_meat)
    dp.register_message_handler(input_cons_meat_veg, state=FSMClient.cons_meat_veg)
    dp.register_message_handler(input_fish_hake, state=FSMClient.fish_hake)
    dp.register_message_handler(input_fish_pike, state=FSMClient.fish_pike)
    dp.register_message_handler(input_fish_pollock, state=FSMClient.fish_pollock)
    dp.register_message_handler(input_fish_smoked, state=FSMClient.fish_smoked)
    dp.register_message_handler(input_cons_fish, state=FSMClient.cons_fish)
    dp.register_message_handler(input_fat, state=FSMClient.fat)
    dp.register_message_handler(input_honey, state=FSMClient.honey)
    dp.register_message_handler(input_jam, state=FSMClient.jam)
    dp.register_message_handler(input_butter, state=FSMClient.butter)
    dp.register_message_handler(input_oil, state=FSMClient.oil)
    dp.register_message_handler(input_marg_fat, state=FSMClient.marg_fat)
    dp.register_message_handler(input_cheese, state=FSMClient.cheese)
    dp.register_message_handler(input_sugar, state=FSMClient.sugar)
    dp.register_message_handler(input_egg, state=FSMClient.egg)
    dp.register_message_handler(input_rice, state=FSMClient.rice)
    dp.register_message_handler(input_buckwheat, state=FSMClient.buckwheat)
    dp.register_message_handler(input_millet, state=FSMClient.millet)
    dp.register_message_handler(input_pears, state=FSMClient.pears)
    dp.register_message_handler(input_barley, state=FSMClient.barley)
    dp.register_message_handler(input_pearl, state=FSMClient.pearl)
    dp.register_message_handler(input_wheat, state=FSMClient.wheat)
    dp.register_message_handler(input_corn, state=FSMClient.corn)
    dp.register_message_handler(input_bulgur, state=FSMClient.bulgur)
    dp.register_message_handler(input_pasta, state=FSMClient.pasta)
    dp.register_message_handler(input_wheat_fl_first, state=FSMClient.wheat_fl_first)
    dp.register_message_handler(input_tea, state=FSMClient.tea)
    dp.register_message_handler(input_salt, state=FSMClient.salt)
    dp.register_message_handler(input_pepper, state=FSMClient.pepper)
    dp.register_message_handler(input_l_list, state=FSMClient.l_list)
    dp.register_message_handler(input_g_porokh, state=FSMClient.g_porokh)
    dp.register_message_handler(input_vinegar, state=FSMClient.vinegar)
    dp.register_message_handler(input_tomat_pasta, state=FSMClient.tomat_pasta)
    dp.register_message_handler(input_dried_fruits, state=FSMClient.dried_fruits)
    dp.register_message_handler(input_juice, state=FSMClient.juice)
    dp.register_message_handler(input_fresh_fruits, state=FSMClient.fresh_fruits)
    dp.register_message_handler(input_potato, state=FSMClient.potato)
    dp.register_message_handler(input_cabbage_fr, state=FSMClient.cabbage_fr)
    dp.register_message_handler(input_cabbage_ferm, state=FSMClient.cabbage_ferm)
    dp.register_message_handler(input_cabbage_cons, state=FSMClient.cabbage_cons)
    dp.register_message_handler(input_carrot_fr, state=FSMClient.carrot_fr)
    dp.register_message_handler(input_carrot_cons, state=FSMClient.carrot_cons)
    dp.register_message_handler(input_beet_fr, state=FSMClient.beet_fr)
    dp.register_message_handler(input_beet_cons, state=FSMClient.beet_cons)
    dp.register_message_handler(input_onion_on, state=FSMClient.onion_on)
    dp.register_message_handler(input_onion_fr, state=FSMClient.onion_fr)
    dp.register_message_handler(input_cucumbers_fr, state=FSMClient.cucumbers_fr)
    dp.register_message_handler(input_cucumbers_ferm, state=FSMClient.cucumbers_ferm)
    dp.register_message_handler(input_cucumbers_cons, state=FSMClient.cucumbers_cons)
    dp.register_message_handler(input_cons_peas, state=FSMClient.cons_peas)
    dp.register_message_handler(input_veg_salads, state=FSMClient.veg_salads)
    dp.register_message_handler(input_yeast, state=FSMClient.yeast)
    dp.register_message_handler(input_water, state=FSMClient.water)
    dp.register_message_handler(input_gecsav, state=FSMClient.gecsav)
    dp.register_message_handler(input_dry_milk, state=FSMClient.dry_milk)
    dp.register_message_handler(input_biscuit, state=FSMClient.biscuit)
    dp.register_message_handler(input_DSP_10, state=FSMClient.DSP_10)
    dp.register_message_handler(input_DSP_15, state=FSMClient.DSP_15)
    dp.register_message_handler(input_dog_food, state=FSMClient.dog_food)
    dp.register_message_handler(input_detergent, state=FSMClient.detergent)
    dp.register_message_handler(input_s_name, state=FSMClient.s_name)
