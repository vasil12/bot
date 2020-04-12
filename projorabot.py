import telebot
import random
from telebot import types

bot = telebot.TeleBot("1224619024:AAGo7cVQx8gpxIpJ1GyRVu8jK_Ws2zW5VT8")
X = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    #picture = open('/pythonprogect/hello.png', 'rb')
    #bot.send_photo(message.chat.id, picture)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton("play")

    markup.add(item3)

    bot.send_message(message.chat.id,
                     "hello {0.first_name}.\n my name -<b> {1.first_name}</b>,I will study decide equations.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text', 'audio'])
def echo_all(message):
    if message.chat.type == 'private':
        global X1, X2, X
        if (message.text == 'play') or (message.text == 'new'):
            X1 = random.randint(-100, 100)
            X2 = random.randint(-100, 100)
            X = X2 - X1
            bot.send_message(message.chat.id, str(X1) + ' + X = ' + str(X2) + '\n input X')
        elif message.text == str(X):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item3 = types.KeyboardButton("new")

            markup.add(item3)
            bot.send_message(message.chat.id, 'True', reply_markup=markup)
            X1 = random.randint(-100, 100)
            X2 = random.randint(-100, 100)
            X = X2 - X1
            bot.send_message(message.chat.id, str(X1) + ' + X = ' + str(X2) + '\n input X')
        elif message.text != str(X):
            markup2 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("help", callback_data='hel')
            item2 = types.InlineKeyboardButton("I can decide", callback_data='can')
            markup2.add(item1, item2)
            bot.send_message(message.chat.id, 'False', reply_markup=markup2)
        else:
            bot.send_message(message.chat.id, 'I don\'t know ')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'hel':
                markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton(str(X))
                item2 = types.KeyboardButton(str(X + random.randint(-5, 5)))
                item3 = types.KeyboardButton(str(X + random.randint(-5, 5)))
                markup1.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, 'choose answer', reply_markup=markup1)
            elif call.data == 'can':
                bot.send_message(call.message.chat.id, 'I just wanted to help😢')

            # remove inline buttons
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
            #                      reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text="you can, I belive in you, just repeat")
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
