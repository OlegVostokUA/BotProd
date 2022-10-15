from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text
from database import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class FSMAdmin(StatesGroup):
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
    avinegar = State()
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

ID = None


async def make_changes_cmd(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Hello Boss!', reply_markup=admin_kb.button_case_admin)
    await message.delete()



async def cm_start(message: types.Message):
    await FSMAdmin.name_div.set()
    await message.answer('Введіть назву підрозділу')


async def input_aname_div(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name_div'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть кількість о/с які перебувають на харчуванні(чол.)')

# @dp.message_handler(state=FSMClient.goods)
async def input_aall_sm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['all_sm'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть кількість строковиків які перебувають на харчуванні(чол.)')

# @dp.message_handler(state=FSMClient.address)
async def input_asolders_sm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['solders_sm'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть кількість о/с які харчуються на обід(чол.)')

async def input_asm_for_lunch(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['sm_for_lunch'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть кількість сл. собак які перебувають на харчуванні(гол.)')

async def input_adogs(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dogs'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть середню (за день) кількість корму, яка використовуєтся для харч сл. собак(кг.)')

async def input_adogs_food_norm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dogs_food_norm'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть кількість наявного продовольства: м’ясо (тущі, напівтущі, чверть)(кг.)')

async def input_ameat_carc(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['meat_carc'] = message.text
    await FSMAdmin.next()
    await message.answer('М’ясні блоки (кг.)')

async def input_ameat_blocks(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['meat_blocks'] = message.text
    await FSMAdmin.next()
    await message.answer('М’ясо птиці (кг.)')

async def input_ameat_chicken(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['meat_chicken'] = message.text
    await FSMAdmin.next()
    await message.answer('Сосиски, сардельки (кг.)')

async def input_asausage(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['sausage'] = message.text
    await FSMAdmin.next()
    await message.answer('Печінка (кг.)')

async def input_aliver(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['liver'] = message.text
    await FSMAdmin.next()
    await message.answer('Консерви м’ясні (кг.)')

async def input_acons_meat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_meat'] = message.text
    await FSMAdmin.next()
    await message.answer('Консерви м’ясорослинні (кг.)')

async def input_acons_meat_veg(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_meat_veg'] = message.text
    await FSMAdmin.next()
    await message.answer('Риба: Хек (кг.)')

async def input_afish_hake(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_hake'] = message.text
    await FSMAdmin.next()
    await message.answer('Сайда (кг.)')

async def input_afish_pike(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_pike'] = message.text
    await FSMAdmin.next()
    await message.answer('Минтай (кг.)')

async def input_afish_pollock(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_pollock'] = message.text
    await FSMAdmin.next()
    await message.answer('Риба копчена, вялена (кг.)')

async def input_afish_smoked(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fish_smoked'] = message.text
    await FSMAdmin.next()
    await message.answer('Консерви рибні (кг.)')

async def input_acons_fish(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_fish'] = message.text
    await FSMAdmin.next()
    await message.answer('Сало (кг.)')

async def input_afat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fat'] = message.text
    await FSMAdmin.next()
    await message.answer('Мед (кг.)')

async def input_ahoney(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['honey'] = message.text
    await FSMAdmin.next()
    await message.answer('Джем (кг.)')

async def input_ajam(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['jam'] = message.text
    await FSMAdmin.next()
    await message.answer('Масло вершкове (кг.)')

async def input_abutter(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['butter'] = message.text
    await FSMAdmin.next()
    await message.answer('Олія (кг.)')

async def input_aoil(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['oil'] = message.text
    await FSMAdmin.next()
    await message.answer('Маргарин (кг.)')

async def input_amarg_fat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['marg_fat'] = message.text
    await FSMAdmin.next()
    await message.answer('Сир (кг.)')

async def input_acheese(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cheese'] = message.text
    await FSMAdmin.next()
    await message.answer('Цукор (кг.)')

async def input_asugar(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['sugar'] = message.text
    await FSMAdmin.next()
    await message.answer('Яйце (шт.)')

async def input_aegg(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['egg'] = message.text
    await FSMAdmin.next()
    await message.answer('Крупи: Рис (кг.)')

async def input_arice(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['rice'] = message.text
    await FSMAdmin.next()
    await message.answer('Гречана (кг.)')

async def input_abuckwheat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['buckwheat'] = message.text
    await FSMAdmin.next()
    await message.answer('Пшоно (кг.)')

async def input_amillet(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['millet'] = message.text
    await FSMAdmin.next()
    await message.answer('Горох (кг.)')

async def input_apears(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pears'] = message.text
    await FSMAdmin.next()
    await message.answer('Ячнева (кг.)')

async def input_abarley(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['barley'] = message.text
    await FSMAdmin.next()
    await message.answer('Перлова (кг.)')

async def input_apearl(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pearl'] = message.text
    await FSMAdmin.next()
    await message.answer('Пшенична (кг.)')

async def input_awheat(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['wheat'] = message.text
    await FSMAdmin.next()
    await message.answer('Кукурудзяна (кг.)')

async def input_acorn(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['corn'] = message.text
    await FSMAdmin.next()
    await message.answer('Булгур (кг.)')

async def input_abulgur(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['bulgur'] = message.text
    await FSMAdmin.next()
    await message.answer('Макаронні вироби (кг.)')

async def input_apasta(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pasta'] = message.text
    await FSMAdmin.next()
    await message.answer('Борошно пшен І гат. (кг.)')

async def input_awheat_fl_first(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['wheat_fl_first'] = message.text
    await FSMAdmin.next()
    await message.answer('Чай (кг.)')

async def input_atea(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['tea'] = message.text
    await FSMAdmin.next()
    await message.answer('Сіль (кг.)')

async def input_asalt(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['salt'] = message.text
    await FSMAdmin.next()
    await message.answer('Перець (кг.)')

async def input_apepper(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['pepper'] = message.text
    await FSMAdmin.next()
    await message.answer('Лавр. лист (кг.)')

async def input_al_list(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['l_list'] = message.text
    await FSMAdmin.next()
    await message.answer('Гірч. порошок (кг.)')

async def input_ag_porokh(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['g_porokh'] = message.text
    await FSMAdmin.next()
    await message.answer('Оцет (кг.)')

async def input_avinegar(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['vinegar'] = message.text
    await FSMAdmin.next()
    await message.answer('Томат паста (кг.)')

async def input_atomat_pasta(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['tomat_pasta'] = message.text
    await FSMAdmin.next()
    await message.answer('Сухофрукти (кг.)')

async def input_adried_fruits(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dried_fruits'] = message.text
    await FSMAdmin.next()
    await message.answer('Соки плодово-ягідні (кг.)')

async def input_ajuice(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['juice'] = message.text
    await FSMAdmin.next()
    await message.answer('Фрукти свіжі (кг.)')

async def input_afresh_fruits(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fresh_fruits'] = message.text
    await FSMAdmin.next()
    await message.answer('Картопля (кг.)')

async def input_apotato(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['potato'] = message.text
    await FSMAdmin.next()
    await message.answer('Капуста свіжа (кг.)')

async def input_acabbage_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cabbage_fr'] = message.text
    await FSMAdmin.next()
    await message.answer('Капуста маринована (кг.)')

async def input_acabbage_ferm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cabbage_ferm'] = message.text
    await FSMAdmin.next()
    await message.answer('Капуста конс. (кг.)')

async def input_acabbage_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cabbage_cons'] = message.text
    await FSMAdmin.next()
    await message.answer('Морква свіжа (кг.)')

async def input_acarrot_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['carrot_fr'] = message.text
    await FSMAdmin.next()
    await message.answer('Морква конс. (кг.)')

async def input_acarrot_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['carrot_cons'] = message.text
    await FSMAdmin.next()
    await message.answer('Буряк свіжий (кг.)')

async def input_abeet_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['beet_fr'] = message.text
    await FSMAdmin.next()
    await message.answer('Буряк конс. (кг.)')

async def input_abeet_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['beet_cons'] = message.text
    await FSMAdmin.next()
    await message.answer('Цибуля ріпчаста (кг.)')

async def input_aonion_on(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['onion_on'] = message.text
    await FSMAdmin.next()
    await message.answer('Цибуля (перо) (кг.)')

async def input_aonion_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['onion_fr'] = message.text
    await FSMAdmin.next()
    await message.answer('Огірки свіжі (кг.)')

async def input_acucumbers_fr(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cucumbers_fr'] = message.text
    await FSMAdmin.next()
    await message.answer('Огірки марин. (кг.)')

async def input_acucumbers_ferm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cucumbers_ferm'] = message.text
    await FSMAdmin.next()
    await message.answer('Огірки конс. (кг.)')

async def input_acucumbers_cons(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cucumbers_cons'] = message.text
    await FSMAdmin.next()
    await message.answer('Консерв. горошок, квасоля (кг.)')

async def input_acons_peas(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['cons_peas'] = message.text
    await FSMAdmin.next()
    await message.answer('Салати овочеві (кг.)')

async def input_aveg_salads(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['veg_salads'] = message.text
    await FSMAdmin.next()
    await message.answer('Дріжджі (кг.)')

async def input_ayeast(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['yeast'] = message.text
    await FSMAdmin.next()
    await message.answer('Вода (л.)')

async def input_awater(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['water'] = message.text
    await FSMAdmin.next()
    await message.answer('Гексавіт (драже)')

async def input_agecsav(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['gecsav'] = message.text
    await FSMAdmin.next()
    await message.answer('Молоко сухе (кг.)')

async def input_adry_milk(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dry_milk'] = message.text
    await FSMAdmin.next()
    await message.answer('Печиво (кг.)')

async def input_abiscuit(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['biscuit'] = message.text
    await FSMAdmin.next()
    await message.answer('ПНСП (норма 10) (к-т.)')

async def input_aDSP_10(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['DSP_10'] = message.text
    await FSMAdmin.next()
    await message.answer('ПНСП (норма 15) (к-т.)')

async def input_aDSP_15(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['DSP_15'] = message.text
    await FSMAdmin.next()
    await message.answer('Корм для сл. собак (кг.)')

async def input_adog_food(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['dog_food'] = message.text
    await FSMAdmin.next()
    await message.answer('Миючий засіб (кг.)')

async def input_adetergent(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['detergent'] = message.text
    await sqlite_db.sql_add_command(state)
    await state.finish()
    await message.answer('Дякую. Залишки подані')


async def del_order_callback_run(callback_order_querry: types.CallbackQuery):
    await sqlite_db.sql_cl_r_delete_command(callback_order_querry.data.replace('odrdel ', ''))
    await callback_order_querry.answer(text=f'{callback_order_querry.data.replace("odrdel ", "")} видалена.', show_alert=True)


async def delete_order_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_cl_r_read2()
        for ret in read:
            await bot.send_message(message.from_user.id, f'Підрозділ:{ret[0]}\nХто подав: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Видалити_заявку {ret[0]}', callback_data=f'odrdel {ret[0]}')))


async def leftovers_command(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.sql_cl_read(message)


async def orders_command(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.sql_read_r(message)


async def parse_to_files_command(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.sql_parse_to_exel(message)

async def clear_db(message: types.Message):
    if message.from_user.id == ID:
        await sqlite_db.sql_clear_command(message)

# @dp.message_handler(state='*', commands='stop')
# @dp.message_handler(Text(equals='stop', ignore_case=True), state='*')
async def cancel_cmd(message: types.Message, state=FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands='УПЗ_Залишки', state=None)
    dp.register_message_handler(input_aname_div, state=FSMAdmin.name_div)
    dp.register_message_handler(input_aall_sm, state=FSMAdmin.all_sm)
    dp.register_message_handler(input_asolders_sm, state=FSMAdmin.solders_sm)
    dp.register_message_handler(input_asm_for_lunch, state=FSMAdmin.sm_for_lunch)
    dp.register_message_handler(input_adogs, state=FSMAdmin.dogs)
    dp.register_message_handler(input_adogs_food_norm, state=FSMAdmin.dogs_food_norm)
    dp.register_message_handler(input_ameat_carc, state=FSMAdmin.meat_carc)
    dp.register_message_handler(input_ameat_blocks, state=FSMAdmin.meat_blocks)
    dp.register_message_handler(input_ameat_chicken, state=FSMAdmin.meat_chicken)
    dp.register_message_handler(input_asausage, state=FSMAdmin.sausage)
    dp.register_message_handler(input_aliver, state=FSMAdmin.liver)
    dp.register_message_handler(input_acons_meat, state=FSMAdmin.cons_meat)
    dp.register_message_handler(input_acons_meat_veg, state=FSMAdmin.cons_meat_veg)
    dp.register_message_handler(input_afish_hake, state=FSMAdmin.fish_hake)
    dp.register_message_handler(input_afish_pike, state=FSMAdmin.fish_pike)
    dp.register_message_handler(input_afish_pollock, state=FSMAdmin.fish_pollock)
    dp.register_message_handler(input_afish_smoked, state=FSMAdmin.fish_smoked)
    dp.register_message_handler(input_acons_fish, state=FSMAdmin.cons_fish)
    dp.register_message_handler(input_afat, state=FSMAdmin.fat)
    dp.register_message_handler(input_ahoney, state=FSMAdmin.honey)
    dp.register_message_handler(input_ajam, state=FSMAdmin.jam)
    dp.register_message_handler(input_abutter, state=FSMAdmin.butter)
    dp.register_message_handler(input_aoil, state=FSMAdmin.oil)
    dp.register_message_handler(input_amarg_fat, state=FSMAdmin.marg_fat)
    dp.register_message_handler(input_acheese, state=FSMAdmin.cheese)
    dp.register_message_handler(input_asugar, state=FSMAdmin.sugar)
    dp.register_message_handler(input_aegg, state=FSMAdmin.egg)
    dp.register_message_handler(input_arice, state=FSMAdmin.rice)
    dp.register_message_handler(input_abuckwheat, state=FSMAdmin.buckwheat)
    dp.register_message_handler(input_amillet, state=FSMAdmin.millet)
    dp.register_message_handler(input_apears, state=FSMAdmin.pears)
    dp.register_message_handler(input_abarley, state=FSMAdmin.barley)
    dp.register_message_handler(input_apearl, state=FSMAdmin.pearl)
    dp.register_message_handler(input_awheat, state=FSMAdmin.wheat)
    dp.register_message_handler(input_acorn, state=FSMAdmin.corn)
    dp.register_message_handler(input_abulgur, state=FSMAdmin.bulgur)
    dp.register_message_handler(input_apasta, state=FSMAdmin.pasta)
    dp.register_message_handler(input_awheat_fl_first, state=FSMAdmin.wheat_fl_first)
    dp.register_message_handler(input_atea, state=FSMAdmin.tea)
    dp.register_message_handler(input_asalt, state=FSMAdmin.salt)
    dp.register_message_handler(input_apepper, state=FSMAdmin.pepper)
    dp.register_message_handler(input_al_list, state=FSMAdmin.l_list)
    dp.register_message_handler(input_ag_porokh, state=FSMAdmin.g_porokh)
    dp.register_message_handler(input_avinegar, state=FSMAdmin.avinegar)
    dp.register_message_handler(input_atomat_pasta, state=FSMAdmin.tomat_pasta)
    dp.register_message_handler(input_adried_fruits, state=FSMAdmin.dried_fruits)
    dp.register_message_handler(input_ajuice, state=FSMAdmin.juice)
    dp.register_message_handler(input_afresh_fruits, state=FSMAdmin.fresh_fruits)
    dp.register_message_handler(input_apotato, state=FSMAdmin.potato)
    dp.register_message_handler(input_acabbage_fr, state=FSMAdmin.cabbage_fr)
    dp.register_message_handler(input_acabbage_ferm, state=FSMAdmin.cabbage_ferm)
    dp.register_message_handler(input_acabbage_cons, state=FSMAdmin.cabbage_cons)
    dp.register_message_handler(input_acarrot_fr, state=FSMAdmin.carrot_fr)
    dp.register_message_handler(input_acarrot_cons, state=FSMAdmin.carrot_cons)
    dp.register_message_handler(input_abeet_fr, state=FSMAdmin.beet_fr)
    dp.register_message_handler(input_abeet_cons, state=FSMAdmin.beet_cons)
    dp.register_message_handler(input_aonion_on, state=FSMAdmin.onion_on)
    dp.register_message_handler(input_aonion_fr, state=FSMAdmin.onion_fr)
    dp.register_message_handler(input_acucumbers_fr, state=FSMAdmin.cucumbers_fr)
    dp.register_message_handler(input_acucumbers_ferm, state=FSMAdmin.cucumbers_ferm)
    dp.register_message_handler(input_acucumbers_cons, state=FSMAdmin.cucumbers_cons)
    dp.register_message_handler(input_acons_peas, state=FSMAdmin.cons_peas)
    dp.register_message_handler(input_aveg_salads, state=FSMAdmin.veg_salads)
    dp.register_message_handler(input_ayeast, state=FSMAdmin.yeast)
    dp.register_message_handler(input_awater, state=FSMAdmin.water)
    dp.register_message_handler(input_agecsav, state=FSMAdmin.gecsav)
    dp.register_message_handler(input_adry_milk, state=FSMAdmin.dry_milk)
    dp.register_message_handler(input_abiscuit, state=FSMAdmin.biscuit)
    dp.register_message_handler(input_aDSP_10, state=FSMAdmin.DSP_10)
    dp.register_message_handler(input_aDSP_15, state=FSMAdmin.DSP_15)
    dp.register_message_handler(input_adog_food, state=FSMAdmin.dog_food)
    dp.register_message_handler(input_adetergent, state=FSMAdmin.detergent)
    dp.register_message_handler(cancel_cmd, state='*', commands='stop')
    dp.register_message_handler(cancel_cmd, Text(equals='stop', ignore_case=True), state='*')
    dp.register_message_handler(make_changes_cmd, commands=['moder'], is_chat_admin = True)

    dp.register_message_handler(leftovers_command, commands='Подані_залишки')
    dp.register_message_handler(orders_command, commands='Прод_заявки')
    dp.register_callback_query_handler(del_order_callback_run, Text(startswith=('odrdel ')))
    dp.register_message_handler(delete_order_item, commands='Видалити_заявку')
    dp.register_message_handler(parse_to_files_command, commands='Сформувати_файл')
    dp.register_message_handler(clear_db, commands='Очистити_БД')


