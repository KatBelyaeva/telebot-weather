import telebot
from telebot import types
from secret import API
from parser import text_result_minsk, text_result_mogilev, text_result_gomel, text_result_grodno, text_result_brest, text_result_vitebsk

bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,f"Здравствуйте {message.from_user.first_name}! Для того, чтобы ознакомиться с прогнозом погоды в Беларуси, нажмите /menu.")

@bot.message_handler(commands=['menu'])
def menu(message):
    my_buttons = types.InlineKeyboardMarkup(row_width=3)
    button_minsk = types.InlineKeyboardButton(text='Минск', callback_data='Minsk')
    button_mogilev = types.InlineKeyboardButton(text='Могилев', callback_data='Mogilev')
    button_gomel = types.InlineKeyboardButton(text='Гомель', callback_data='Gomel')
    button_vitebsk = types.InlineKeyboardButton(text='Витебск', callback_data='Vitebsk')
    button_grodno = types.InlineKeyboardButton(text='Гродно', callback_data='Grodno')
    button_brest = types.InlineKeyboardButton(text='Брест', callback_data='Brest')
    my_buttons.add(button_minsk, button_mogilev, button_brest, button_grodno, button_vitebsk, button_gomel)
    bot.send_message(message.chat.id, 'Выберите ваш город:', reply_markup=my_buttons)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'Minsk':
            bot.send_message(call.message.chat.id, f' Погода в Минске: {text_result_minsk}')

        elif call.data == 'Mogilev':
            bot.send_message(call.message.chat.id, f' Погода в Могилеве: {text_result_mogilev}')

        elif call.data == 'Gomel':
            bot.send_message(call.message.chat.id, f' Погода в Гомеле: {text_result_gomel}')

        elif call.data == 'Vitebsk':
            bot.send_message(call.message.chat.id, f' Погода в Витебске: {text_result_vitebsk}')

        elif call.data == 'Grodno':
            bot.send_message(call.message.chat.id, f' Погода в Гродно: {text_result_grodno}')

        elif call.data == 'Brest':
            bot.send_message(call.message.chat.id, f' Погода в Бресте: {text_result_brest}')

bot.polling(none_stop=True)