import sqlite3 as sq

from create_bot import bot
import time
import pandas as pd


def sql_start():
    # create  table for admin(zagin)
    global base, cur
    base = sq.connect('leftovers.db')
    cur = base.cursor()
    if base:
        print('Data base admin connection=Done')
    base.execute('CREATE TABLE IF NOT EXISTS leftovers_zagin('
                 'marker TEXT, '
                 'name_div TEXT, '
                 'all_sm TEXT, '
                 'solders_sm TEXT, '
                 'sm_for_lunch TEXT, '
                 'dogs TEXT, '
                 'dogs_food_norm TEXT, '
                 'meat_carc TEXT, '
                 'meat_blocks TEXT, '
                 'meat_chicken TEXT, '
                 'sausage TEXT, '
                 'liver TEXT, '
                 'cons_meat TEXT, '
                 'cons_meat_veg TEXT, '
                 'fish_hake TEXT, ' 
                 'fish_pike TEXT, ' 
                 'fish_pollock TEXT, ' 
                 'fish_smoked TEXT, '
                 'cons_fish TEXT, '
                 'fat TEXT, ' 
                 'honey TEXT, '
                 'jam TEXT, '
                 'butter TEXT, '
                 'oil TEXT, '
                 'marg_fat TEXT, '
                 'cheese TEXT, '
                 'sugar TEXT, '
                 'egg TEXT, '
                 'rice TEXT, '
                 'buckwheat TEXT, ' 
                 'millet TEXT, ' 
                 'pears TEXT, ' 
                 'barley TEXT, ' 
                 'pearl TEXT, ' 
                 'wheat TEXT, ' 
                 'corn TEXT, '
                 'bulgur TEXT, '
                 'pasta TEXT, '
                 'wheat_fl_first TEXT, ' 
                 'tea TEXT, '
                 'salt TEXT, '
                 'pepper TEXT, '
                 'l_list TEXT, '
                 'g_porokh TEXT, '
                 'vinegar TEXT, '
                 'tomat_pasta TEXT, '
                 'dried_fruits TEXT, '
                 'juice TEXT, '
                 'fresh_fruits TEXT, '
                 'potato TEXT, '
                 'cabbage_fr TEXT, '
                 'cabbage_ferm TEXT, '
                 'cabbage_cons TEXT, '
                 'carrot_fr TEXT, '
                 'carrot_cons TEXT, '
                 'beet_fr TEXT, '
                 'beet_cons TEXT, '
                 'onion_on TEXT, ' 
                 'onion_fr TEXT, '
                 'cucumbers_fr TEXT, '
                 'cucumbers_ferm TEXT, '
                 'cucumbers_cons TEXT, '
                 'cons_peas TEXT, '
                 'veg_salads TEXT, '
                 'yeast TEXT, ' 
                 'water TEXT, '
                 'gecsav TEXT, '
                 'dry_milk TEXT, '
                 'biscuit TEXT, ' 
                 'DSP_10 TEXT, '
                 'DSP_15 TEXT, '
                 'dog_food TEXT, '
                 'detergent TEXT, '
                 's_name TEXT) ')

    base.commit()


def sql_cl_start():
    # create  table for clients(pidrozdil)
    global base, cur
    base = sq.connect('leftovers.db')
    cur = base.cursor()
    if base:
        print('Data base client connection=Done')
    base.execute('CREATE TABLE IF NOT EXISTS leftovers_border('
                 'marker TEXT, '
                 'name_div TEXT, '
                 'all_sm TEXT, '
                 'solders_sm TEXT, '
                 'sm_for_lunch TEXT, '
                 'dogs TEXT, '
                 'dogs_food_norm TEXT, '
                 'meat_carc TEXT, '
                 'meat_blocks TEXT, '
                 'meat_chicken TEXT, '
                 'sausage TEXT, '
                 'liver TEXT, '
                 'cons_meat TEXT, '
                 'cons_meat_veg TEXT, '
                 'fish_hake TEXT, ' 
                 'fish_pike TEXT, ' 
                 'fish_pollock TEXT, ' 
                 'fish_smoked TEXT, '
                 'cons_fish TEXT, '
                 'fat TEXT, ' 
                 'honey TEXT, '
                 'jam TEXT, '
                 'butter TEXT, '
                 'oil TEXT, '
                 'marg_fat TEXT, '
                 'cheese TEXT, '
                 'sugar TEXT, '
                 'egg TEXT, '
                 'rice TEXT, '
                 'buckwheat TEXT, ' 
                 'millet TEXT, ' 
                 'pears TEXT, ' 
                 'barley TEXT, ' 
                 'pearl TEXT, ' 
                 'wheat TEXT, ' 
                 'corn TEXT, '
                 'bulgur TEXT, '
                 'pasta TEXT, '
                 'wheat_fl_first TEXT, ' 
                 'tea TEXT, '
                 'salt TEXT, '
                 'pepper TEXT, '
                 'l_list TEXT, '
                 'g_porokh TEXT, '
                 'vinegar TEXT, '
                 'tomat_pasta TEXT, '
                 'dried_fruits TEXT, '
                 'juice TEXT, '
                 'fresh_fruits TEXT, '
                 'potato TEXT, '
                 'cabbage_fr TEXT, '
                 'cabbage_ferm TEXT, '
                 'cabbage_cons TEXT, '
                 'carrot_fr TEXT, '
                 'carrot_cons TEXT, '
                 'beet_fr TEXT, '
                 'beet_cons TEXT, '
                 'onion_on TEXT, ' 
                 'onion_fr TEXT, '
                 'cucumbers_fr TEXT, '
                 'cucumbers_ferm TEXT, '
                 'cucumbers_cons TEXT, '
                 'cons_peas TEXT, '
                 'veg_salads TEXT, '
                 'yeast TEXT, ' 
                 'water TEXT, '
                 'gecsav TEXT, '
                 'dry_milk TEXT, '
                 'biscuit TEXT, ' 
                 'DSP_10 TEXT, '
                 'DSP_15 TEXT, '
                 'dog_food TEXT, '
                 'detergent TEXT, '
                 's_name TEXT) ')
    base.commit()


def sql_cl_r_start():
    # create table for client responses (pidrozd resp)
    global base, cur
    base = sq.connect('leftovers.db')
    cur = base.cursor()
    if base:
        print('Data base client connection=Done')
    base.execute('CREATE TABLE IF NOT EXISTS requests_border(name_div_r TEXT, request_div TEXT, s_name_r TEXT)')
    base.commit()


async def sql_add_command(state):
    # func for add information for admin (zagin add)
    async with state.proxy() as data:
        cur.execute('INSERT INTO leftovers_zagin VALUES ("zagin", ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                    '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                    '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "admin")', tuple(data.values()))
        base.commit()


async def sql_cl_add_command(state):
    # func for add information for client (pidrozdil add)
    async with state.proxy() as data:
        cur.execute('INSERT INTO leftovers_border VALUES ("pidrozdil", ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                    ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                    ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_cl_add_command_r(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO requests_border VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM leftovers_zagin').fetchall():
        await bot.send_message(message.from_user.id, f'М’ясо (тущі, напівтущі, чверть): {ret[7]} кг\n'
                                                     f'М’ясні блоки: {ret[8]} кг\nМ’ясо птиці: {ret[9]} кг\n'
                                                     f'Сосиски, сардельки: {ret[10]} кг\nПечінка: {ret[11]} кг\n'
                                                     f'Консерви м’ясні: {ret[12]} кг\nКонсерви м’ясорослинні: {ret[13]} кг\n'
                                                     f'Риба: Хек: {ret[14]} кг\nСайда: {ret[15]} кг\nМинтай: {ret[16]} кг\n'
                                                     f'Риба копчена, вялена: {ret[17]} кг\nКонсерви рибні: {ret[18]} кг\n'
                                                     f'Сало: {ret[19]} кг\nМед: {ret[20]} кг\nДжем: {ret[21]} кг\n'
                                                     f'Масло вершкове: {ret[22]} кг\nОлія: {ret[23]} кг\nМаргарин: {ret[24]} кг\n'
                                                     f'Сир: {ret[25]} кг\nЦукор: {ret[26]} кг\nЯйце: {ret[27]} кг\n'
                                                     f'Крупи: Рис: {ret[28]} кг\nГречана: {ret[29]} кг\nПшоно: {ret[30]} кг\n'
                                                     f'Горох: {ret[31]} кг\nЯчнева: {ret[32]} кг\nПерлова: {ret[33]} кг\n'
                                                     f'Пшенична: {ret[34]} кг\nКукурудзяна: {ret[35]} кг\nБулгур: {ret[36]} кг\n'
                                                     f'Макаронні вироби: {ret[37]} кг\nБорошно пшен І гат.: {ret[38]} кг\n'
                                                     f'Чай: {ret[39]} кг\nСіль: {ret[40]} кг\nПерець: {ret[41]} кг\n'
                                                     f'Лавр. лист: {ret[42]} кг\nГірч. порошок: {ret[43]} кг\n'
                                                     f'Оцет: {ret[44]} кг\nТомат паста: {ret[45]} кг\nСухофрукти: {ret[46]} кг\n'
                                                     f'Соки плодово-ягідні: {ret[47]} кг\nФрукти свіжі: {ret[48]} кг\n'
                                                     f'Картопля: {ret[49]} кг\nКапуста свіжа: {ret[50]} кг\n'
                                                     f'Капуста маринована: {ret[51]} кг\nКапуста конс.: {ret[52]} кг\n'
                                                     f'Морква свіжа: {ret[53]} кг\nМорква конс.: {ret[54]} кг\n'
                                                     f'Буряк свіжий: {ret[55]} кг\nБуряк конс.: {ret[56]} кг\n'
                                                     f'Цибуля ріпчаста: {ret[57]} кг\nЦибуля (перо): {ret[58]} кг\n'
                                                     f'Огірки свіжі: {ret[59]} кг\nОгірки марин.: {ret[60]} кг\n'
                                                     f'Огірки конс.: {ret[61]} кг\nКонсерв. горошок, квасоля: {ret[62]} кг\n'
                                                     f'Салати овочеві: {ret[63]} кг\nДріжджі: {ret[64]} кг\nВода: {ret[65]} л\n'
                                                     f'Гексавіт: {ret[66]} др\nМолоко сухе: {ret[67]} кг\nПечиво: {ret[68]} кг\n'
                                                     f'ПНСП (норма 10): {ret[69]} к-т\nПНСП (норма 15): {ret[70]} к-т\n'
                                                     f'Корм для сл. собак: {ret[71]} кг\nМиючий засіб: {ret[72]} кг')


async def sql_cl_read(message):
    for ret in cur.execute('SELECT * FROM leftovers_border').fetchall():
        await bot.send_message(message.from_user.id, f'Підрозділ:{ret[1]}\nХто подав: {ret[-1]}')


async def sql_read_r(message):
    #return cur.execute('SELECT * FROM requests_border').fetchall()
    for ret in cur.execute('SELECT * FROM requests_border').fetchall():
        await bot.send_message(message.from_user.id, f'Підрозділ:{ret[0]}\nЗаявка:{ret[1]}\nХто подав: {ret[-1]}')


async def sql_parse_to_exel(message):
    # tm = time.ctime()
    # tm_to_create = tm[4:10]
    n_pidr = 'leftovers_border'
    n_zag = 'leftovers_zagin'
    format_file = '.xlsx'

    # name_file_p = n_pidr+tm_to_create+format_file
    # name_file_z = n_zag+tm_to_create+format_file

    name_file_p = n_pidr+format_file
    name_file_z = n_zag+format_file


    var_name = [('marker', 'Назва підрозділу', 'кількість о/с на харчуванні', 'строковики на харчуванні',
                   'о/с які харчуються на обід', 'сл. собак на харчуванні', 'середня (за день) кількість корму',
                   'м’ясо (тущі, напівтущі, чверть)', 'М’ясні блоки', 'М’ясо птиці', 'Сосиски, сардельки', 'Печінка',
                   'Консерви м’ясні', 'Консерви м’ясорослинні', 'Риба: Хек', 'Сайда', 'Минтай', 'Риба копчена, вялена',
                   'Консерви рибні', 'Сало', 'Мед', 'Джем', 'Масло вершкове', 'Олія', 'Маргарин', 'Сир', 'Цукор',
                   'Яйце',
                   'Крупи: Рис', 'Гречана', 'Пшоно', 'Горох', 'Ячнева', 'Перлова', 'Пшенична', 'Кукурудзяна', 'Булгур',
                   'Макаронні вироби', 'Борошно пшен І гат.', 'Чай', 'Сіль', 'Перець', 'Лавр. лист', 'Гірч. порошок',
                   'Оцет', 'Томат паста', 'Сухофрукти', 'Соки плодово-ягідні', 'Фрукти свіжі', 'Картопля', 'Капуста свіжа',
                   'Капуста маринована', 'Капуста конс.', 'Морква свіжа', 'Морква конс.', 'Буряк свіжий', 'Буряк конс.',
                   'Цибуля ріпчаста', 'Цибуля (перо)', 'Огірки свіжі', 'Огірки марин.', 'Огірки конс.',
                   'Консерв. горошок, квасоля', 'Салати овочеві', 'Дріжджі', 'Вода', 'Гексавіт', 'Молоко сухе',
                   'Печиво',
                   'ПНСП (норма 10)', 'ПНСП (норма 15)', 'Корм для сл. собак', 'Миючий засіб', '')]

    cur.executemany('INSERT INTO leftovers_zagin VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', var_name)
    cur.executemany('INSERT INTO leftovers_border VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', var_name)

    df_p = pd.read_sql("SELECT * FROM leftovers_border", base)
    df_p.to_excel(name_file_p)

    df_z = pd.read_sql("SELECT * FROM leftovers_zagin", base)
    df_z.to_excel(name_file_z)

    await bot.send_message(message.from_user.id, "OK")
    """
    time.sleep(3)
    await bot.send_document(message.from_user.id, ('leftovers_border.xlsx', file))
    await bot.send_document(message.from_user.id, ('leftovers_zagin.xlsx', file))
#open('C:/Users/User/PycharmProjects/TG Bot/pics/shema_sz.jpg', 'rb')
    """
async def sql_cl_r_read2():
    return cur.execute('SELECT * FROM requests_border').fetchall()


async def sql_cl_r_delete_command(data):
    cur.execute('DELETE FROM requests_border WHERE name_div_r == ?', (data,))
    base.commit()


async def sql_clear_command(message):
    cur.execute('DELETE FROM leftovers_zagin ;')
    cur.execute('DELETE FROM leftovers_border ;')
    base.commit()

