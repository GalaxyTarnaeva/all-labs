import telebot
from telebot import types
from collections import defaultdict

bot = telebot.TeleBot("6028249804:AAEgLrAoEsbEI3Tm4PHbnxh1Iv0nrWt8dCU")

user_by_messages = defaultdict(list) # присваивается переменнВой то, что пишет пользователь
messages = []

# -------------------------------------------------------------------------------------------------------------------- #
@bot.message_handler(commands=['start']) # что будет делать, если будет команда старт
def start_command(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True) # чтобы бот выводил кнопку
    item1 = types.KeyboardButton('Создать список дел 📝')
    markup1.add(item1)
    bot.send_message(message.chat.id, "<b>Привет, я бот тайм-менджмента, давай составим твой список дел! </b>",
                     parse_mode='html', reply_markup=markup1) # мод хтмл, чтобы менять текст (более жирный и тп) реплей... -  вывод кнопки
# -------------------------------------------------------------------------------------------------------------------- #
@bot.message_handler(content_types=['text']) # что будет делать при тексте
def new(message):
    if message.text == 'Создать список дел 📝': # если нажмут кнопку список дел
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('➕ Добавить дело')
        item23 = types.KeyboardButton('📋 Список')
        markup2.add(item2, item23)
        bot.send_message(message.chat.id, "<b>Выбери функцию 😇</b>", parse_mode='html', reply_markup=markup2)

# -------------------------------------------------------------------------------------------------------------------- #

    elif message.text == '➕ Добавить дело': # если нажмут кнопку добавить дело
        msg11 = bot.send_message(message.chat.id, "<b>Для продолжения напиши и отправь любое сообщение</b>", parse_mode='html')
        bot.register_next_step_handler(msg11, f) # ждет сообщение от пользователя

    elif message.text == '📋 Список': # если нажмут кнопку список
        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item24 = types.KeyboardButton('✍️ Закончить дело')
        item25 = types.KeyboardButton('🗑 Очистить список')
        item15 = types.KeyboardButton('🔙')
        markup9.add(item24, item25)
        markup9.add(item15)
        bot.send_message(message.chat.id, '\n'.join(messages), reply_markup=markup9) # функция помогает занести в список messages то что пишет пользователь

# -------------------------------------------------------------------------------------------------------------------- #

    elif message.text == '✍️ Закончить дело':
        markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item26 = types.KeyboardButton('1')
        item27 = types.KeyboardButton('2')
        item28 = types.KeyboardButton('3')
        item29 = types.KeyboardButton('4')
        item30 = types.KeyboardButton('5')
        item31 = types.KeyboardButton('6')
        item32 = types.KeyboardButton('7')
        item33 = types.KeyboardButton('8')
        item34 = types.KeyboardButton('9')
        item35 = types.KeyboardButton('10')
        item15 = types.KeyboardButton('🔙')
        markup10.add(item26, item31)
        markup10.add(item27, item32)
        markup10.add(item28, item33)
        markup10.add(item29, item34)
        markup10.add(item30, item35)
        markup10.add(item15)
        bot.send_message(message.chat.id, "<b>📤 Выберите номер дела, которое хотите удалить! </b>", parse_mode='html',
                                                                                            reply_markup=markup10)

    elif message.text == '1':
        del messages[0]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '2':
        del messages[1]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '3':
        del messages[2]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '4':
        del messages[3]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '5':
        del messages[4]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '6':
        del messages[5]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '7':
        del messages[6]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '8':
        del messages[7]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '9':
        del messages[8]
        bot.send_message(message.chat.id, '\n'.join(messages))

    elif message.text == '10':
        del messages[9]
        bot.send_message(message.chat.id, '\n'.join(messages))

# -------------------------------------------------------------------------------------------------------------------- #

    elif message.text == '🗑 Очистить список':
        messages.clear()
        bot.send_message(message.chat.id, "<b>Список очищен ♻️ </b>", parse_mode='html')

    elif message.text == '🔙':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('➕ Добавить дело')
        item23 = types.KeyboardButton('📋 Список')
        markup2.add(item2, item23)
        bot.send_message(message.chat.id, "<b>Выбери функцию 😇</b>", parse_mode='html', reply_markup=markup2)

# -------------------------------------------------------------------------------------------------------------------- #

@bot.message_handler(commands=[]) # после того как пользователь удалит дело он мог снова ввести дело
def f(message):
    msg10 = bot.send_message(message.chat.id, '<b>Введи своё дело: </b>', parse_mode='html')
    bot.register_next_step_handler(msg10, f2)

def f2(message):
    st = '{}'.format(message.text)
    messages.append(st)
    bot.send_message(message.chat.id, '\n'.join(messages))

bot.infinity_polling(none_stop = True, interval=0)