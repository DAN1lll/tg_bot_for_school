import telebot 
from telebot import types 
 
bot = telebot.TeleBot('api-token')
@bot.message_handler(commands=['start']) 
def start(message): 
    bot.send_photo(message.chat.id, photo='http://photobook33.ru/wp-content/uploads/2015/12/%D0%A0%D0%B0%D0%B9%D0%BE%D0%BD-%D0%9C%D0%B8%D1%85%D0%B0%D0%BB%D0%B8-%D0%A1%D1%83%D0%B7%D0%B4%D0%B0%D0%BB%D1%8C-02.jpg' 
    ,caption= 'Для того чтобы управлять ботом следуй инструкциям на картинке!!! ',reply_markup=mm) 
 
mm = types.ReplyKeyboardMarkup(row_width=2) 
button1 = types.KeyboardButton("Михали-исторический район Суздаля") 
button2 = types.KeyboardButton("Контакты") 
button4 = types.KeyboardButton("Фотографии комплекса") 
button3 = types.KeyboardButton("Храмовый комплекс и школа") 
mm.add(button1,button2,button4,button3) 
 
@bot.message_handler(content_types=['text']) 
def handler(message): 
    if message.text == "Михали-исторический район Суздаля": 
        bot.send_message(message.chat.id, text = 'Михали – исторический район Суздаля, богатый своими достопримечательностями и археологическими находками.Михали – исторический район Суздаля, богатый своими достопримечательностями и археологическими находками.' 
                                        'В древности на месте, где река Мжара впадает в Каменку, располагалась слобода, принадлежавшая сыну Юрия Долгорукого - князю Михалке, поэтому и назвали - Михайловская.' 
                                        'Напротив слободы расположен большой луг, который окружен с трех сторон руслом Каменки.' 
                                        'В середине 19 века между реками Каменкой и Мжарой были обнаружены древние захоронения славян – языческие курганы. Сейчас Мжарский могильник является известным археологическим памятником и насчитывает около 359 курганов. Он был обнаружен в 1851г графом С.Уваровым и изучен в 20 веке.' 
                                        'В Михалях на вершине холма расположились три православных храма. Территориях храмов огорожена и ухожена, вход свободный.') 
    if message.text == "Храмовый комплекс и школа": 
        bot.send_photo(message.chat.id, photo=('http://photobook33.ru/wp-content/uploads/2015/12/%D0%A0%D0%B0%D0%B9%D0%BE%D0%BD-%D0%9C%D0%B8%D1%85%D0%B0%D0%BB%D0%B8-%D0%A1%D1%83%D0%B7%D0%B4%D0%B0%D0%BB%D1%8C-02.jpg'), 
                       caption='1-Храм Михаила Архангела' 
                        '\n''2-Храм Флора и Лавра' 
                        '\n''3-Храм Александра Невского' 
                        '\n''4-Здание школы' 
                        '\n''На территории ансамбля находится школа' 
                        '\n''В свою очередь сам ансамбль стоит на территории экопарка "Михалёвские тропы"',reply_markup=otvet) 
    if message.text == "Контакты": 
        bot.send_message(message.chat.id, 
                                        "\n"'Сайт школы - http://mihali-suzdal.ru/' 
                                        "\n"'Эл.почта школы - mihali-suzdal@yandex.ru' 
                                        "\n"'Группа экопарка "Михалёвские тропы" в ВК - https://vk.com/mihalipath?ysclid=lrrxvemgmo209245616') 
    if message.text == "Фотографии комплекса": 
        bot.send_message(message.chat.id, 'Выбери время года, в котором ты хочешь увидеть комплекс', reply_markup=seasons) 
 
 
# bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb')),   
#                                        telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb'))     ]) 
 
seasons = types.InlineKeyboardMarkup(row_width=2) 
zima = types.InlineKeyboardButton("Зимой", callback_data='zima1') 
vesna = types.InlineKeyboardButton("Весной", callback_data='vesna1') 
leto = types.InlineKeyboardButton("Летом", callback_data='leto1') 
osenb = types.InlineKeyboardButton("Осенью", callback_data='osenb1') 
seasons.add(zima,vesna,leto,osenb) 
 
 
otvet = types.InlineKeyboardMarkup(row_width=2) 
butto1 = types.InlineKeyboardButton("Храм Михаила Архангела", callback_data='hram1') 
butto2 =types.InlineKeyboardButton("Храм Флора и Лавра", callback_data='hram2') 
butto3 = types.InlineKeyboardButton("Храм Александра Невского", callback_data='hram3') 
butto4 = types.InlineKeyboardButton("Школа", callback_data='school') 
otvet.add(butto1,butto2,butto3,butto4) 
 
 
vvv = types.InlineKeyboardMarkup(row_width=2) 
bakkk = types.InlineKeyboardButton('Назад', callback_data= 'baccc') 
aaa = types.InlineKeyboardButton('Еще фотографии', callback_data= 'tot_ajnj1') 
vvv.add(aaa,bakkk) 
 
vvv2 = types.InlineKeyboardMarkup(row_width=2) 
bakkk = types.InlineKeyboardButton('Назад', callback_data= 'baccc') 
aaa2 =types.InlineKeyboardButton('Еще фотографии', callback_data= 'tot_ajnj2') 
vvv2.add(aaa2,bakkk) 
 
vvv3 = types.InlineKeyboardMarkup(row_width=2) 
bakkk = types.InlineKeyboardButton('Назад', callback_data= 'baccc') 
aa3 = types.InlineKeyboardButton('Еще фотографии', callback_data= 'tot_ajnj3') 
vvv3.add(aa3,bakkk) 
 
vvv4 = types.InlineKeyboardMarkup(row_width=2) 
bakkk = types.InlineKeyboardButton('Назад', callback_data= 'baccc') 
c2 = types.InlineKeyboardButton("О школе", callback_data='school_info') 
# aa4 = types.InlineKeyboardButton('Еще фотографии', callback_data= 'tot_ajnj4') 
vvv4.add(c2,bakkk) 
 
seasons1 = types.InlineKeyboardMarkup(row_width=2) 
vesna = types.InlineKeyboardButton("Весна", callback_data='vesna1') 
leto = types.InlineKeyboardButton("Лето", callback_data='leto1') 
osenb = types.InlineKeyboardButton("Осень", callback_data='osenb1') 
seasons1.add(vesna,leto,osenb) 
 
seasons2 = types.InlineKeyboardMarkup(row_width=2) 
zima = types.InlineKeyboardButton("Зима", callback_data='zima1') 
leto = types.InlineKeyboardButton("Лето", callback_data='leto1') 
osenb = types.InlineKeyboardButton("Осень", callback_data='osenb1') 
seasons2.add(zima,leto,osenb) 
 
seasons3 = types.InlineKeyboardMarkup(row_width=2) 
vesna = types.InlineKeyboardButton("Весна", callback_data='vesna1') 
zima = types.InlineKeyboardButton("Зима", callback_data='zima1') 
osenb = types.InlineKeyboardButton("Осень", callback_data='osenb1') 
seasons3.add(zima,vesna,osenb) 
 
seasons4 = types.InlineKeyboardMarkup(row_width=2) 
vesna = types.InlineKeyboardButton("Весна", callback_data='vesna1') 
leto = types.InlineKeyboardButton("Лето", callback_data='leto1') 
zima = types.InlineKeyboardButton("Зима", callback_data='zima1') 
seasons4.add(vesna,leto,zima) 
 
@bot.callback_query_handler(func=lambda c:True) 
def inlin(c): 
    if c.data == 'tot_ajnj4': 
        bot.send_media_group(c.message.chat.id,) 
    if c.data == 'school_info': 
        bot.send_message(c.message.chat.id, text='ABCD') 
    if c.data == 'hram1': 
        bot.send_photo(c.message.chat.id, photo='https://sobory.ru/pic/02350/02356_20130607_230434.jpg', caption = 'Храм Михаила Архангела' 
                       '\n''Памятник архитектуры. С 2004 года является частью ансанмбля церквей.' 
                        'Рядом с храмом Архангела Михаила находятся ещё две церкви: Флора и Лавра и Александра Невского.' 
                        'Храм Архангела Михаила был построен в 1769 году.' 
                        'Основной объём храма — большой четверик, бело-красное здание, украшенное богатым декором: тёмно-красные стены, узорчатые белые наличники окон.' 
                        'Над вторым ярусом окон проведён поясок, а под кровлей — карниз. Крест над церковью имеет сложный рисунок.' 
                        'С западной стороны к храму пристроена трапезная, соединяющая основной объём церкви с высокой колокольней в стиле классицизма.' 
                        'Колокольня увенчана стройным острым шпилем, который опирается на сферический купол-основание.' 
                        '(В настоящее время находится в реставрации)',reply_markup= vvv) 
    if c.data == 'hram2': 
        bot.send_photo(c.message.chat.id, photo='https://static02.rusroads.com/1200x630/photos/03/99/16bea4a6/3a974e5a6.jpg',caption='Храм Флора и Лавра' 
                       '\n''Памятник архитектуры. С 2004 года является частью ансамбля церквей.' 
                        'Рядом с храмом Флора и Лавра находятся ещё две церкви: Архангела Михаила и Александра Невского.'
                        'Храм был построен в 1803 году. К центральной части, более высокой, с западной стороны пристроен небольшой объём, похожий на меньшую клеть традиционных «зимних» суздальских храмов.' 
                        'Широкая алтарная часть квадратная, а не полукруглая, с тремя смежными окнами.' 
                        'Как и другие храмы комплекса, церковь Флора и Лавра была отреставрирована в начале 21 века и заново расписана.',reply_markup= vvv2) 
    if c.data == 'hram3': 
        bot.send_photo(c.message.chat.id, photo= 'https://sobory.ru/pic/02300/02357_20111121_215131.jpg',caption='Храм Александра Невского' 
                        '\n''Возведен в начале XX века и является единственной сохранившейся церковью Суздаля в русском стиле.' 
                        'Церковь Александра Невского практически единственный в Суздале храм, выполненный в русском стиле.' 
                        'Крестообразное в плане строение из белого камня богато изукрашено наличниками, резьбой, выложенными из облицовочного кирпича узорами. Пышный декор придает ему торжественность и зрительно приближает к древнерусским храмам.' 
                        'Расписанный шатер кровли увенчан небольшой луковичной главой, еще 4 главки стоят на башенках по углам основного здания. Главный фасад украшают мозаичные иконы и орнаменты. Интерьер расписан заново в современной манере, везде сияют позолота и хрусталь.' 
                        'В годы Советской власти храм был заброшен. В начале XXI века восстановлен и обнесен оградой вместе с близлежащим ансамблем из колокольни и двух церквей Михаила Архангела и Флора и Лавра.' 
                        '(В настоящее время находится в реставрации)' ,reply_markup= vvv3) 
    if c.data == 'school': 
        bot.send_photo(c.message.chat.id, photo='https://sobory.ru/pic/17950/17985_20150728_184730.jpg',caption= 
                       '\n''"ЧОУ" Православная СОШ имени святителя Арсения Элассонского г. Суздаль' 
                       '\n''',reply_markup= vvv4)     
 
 
    if c.data == 'zima1': 
        bot.send_media_group(c.message.chat.id, [telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb')),   
                                       telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb'))]) 
        bot.send_message(c.message.chat.id, "Комплекс зимой",reply_markup=seasons1) 
 
    if c.data == 'vesna1': 
        bot.send_media_group(c.message.chat.id, [telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb')),   
                                       telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb'))]) 
        bot.send_message(c.message.chat.id, "Комплекс весной",reply_markup=seasons2) 
 
    if c.data == 'leto1': 
        bot.send_media_group(c.message.chat.id, [telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb')),   
                                       telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb'))]) 
        bot.send_message(c.message.chat.id, "Комплекс летом",reply_markup=seasons3) 
 
    if c.data == 'osenb1': 
        bot.send_media_group(c.message.chat.id, [telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb')),   
                                       telebot.types.InputMediaPhoto(open('photo_1.jpg', 'rb'))]) 
        bot.send_message(c.message.chat.id, "Комплекс осенью",reply_markup=seasons4) 
  
         
    if c.data == 'baccc': 
        bot.send_photo(c.message.chat.id, photo=('http://photobook33.ru/wp-content/uploads/2015/12/%D0%A0%D0%B0%D0%B9%D0%BE%D0%BD-%D0%9C%D0%B8%D1%85%D0%B0%D0%BB%D0%B8-%D0%A1%D1%83%D0%B7%D0%B4%D0%B0%D0%BB%D1%8C-02.jpg'), 
                    caption='1-Храм Михаила Архангела' 
                    '\n''2-Храм Флора и Лавра' 
                    '\n''3-Храм Александра Невского' 
                    '\n''4-Здание школы' 
                    '\n''На территории ансамбля находится школа',reply_markup=otvet)                 
 
if __name__ == "__main__": 
    bot.polling(none_stop=True)

