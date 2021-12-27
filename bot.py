import telebot
from telebot import types
from stock_quotes import get_quotes

bot = telebot.TeleBot("5008953624:AAGFrj1ufr3Nl2tIgo0fJv2yyyJugC6n12M")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "В хелпе будут команды")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Зарегистрироваться', callback_data='registration')
    item2 = types.InlineKeyboardButton('Просмотреть инструменты', callback_data='instruments')
    markup.add(item, item2)
    bot.send_message(message.chat.id, "Привет, я бот трейдер, буду давать тебе"
                                      " бесплатные сигналы на покупку и продажу", reply_markup=markup)

@bot.message_handler(commands=['signal'])
def signal(message,symbol1,symbol2):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Назад', callback_data='back')
    markup.add(item)
    strReturn = get_quotes(symbol1,symbol2)
    bot.send_message(message.chat.id, "Вы выбрали инструмент : "+symbol1+'/'+symbol2+'\n'+strReturn, reply_markup=markup)


@bot.message_handler(commands=['signals'])
def signalsList(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('EUR/USD', callback_data='eur_usd')
    item1 = types.InlineKeyboardButton('USD/PLN', callback_data='usd_pln')
    item2 = types.InlineKeyboardButton('USD/RUB', callback_data='usd_rub')
    item3 = types.InlineKeyboardButton('USD/CAD', callback_data='usd_cad')
    item4 = types.InlineKeyboardButton('USD/CHF', callback_data='usd_chf')
    item5 = types.InlineKeyboardButton('Назад', callback_data='back_start')
    # item5 = types.InlineKeyboardButton('USD/CNH', callback_data='usd_cnh')
    # item6 = types.InlineKeyboardButton('USD/DKK', callback_data='usd_dkk')
    # item7 = types.InlineKeyboardButton('USD/JPY', callback_data='usd_jpy')
    # item8 = types.InlineKeyboardButton('USD/MXN', callback_data='usd_mxn')
    # item9 = types.InlineKeyboardButton('USD/NOK', callback_data='usd_nok')
    # item10 = types.InlineKeyboardButton('USD/SEK', callback_data='usd_sek')
    # item11 = types.InlineKeyboardButton('USD/SGD', callback_data='esd_sgd')
    # item12 = types.InlineKeyboardButton('USD/TRY', callback_data='usd_try')
    # item13 = types.InlineKeyboardButton('USD/ZAR', callback_data='usd_zar')
    markup.add(item, item1,item2,item3,item4)
               # item5,item6,item7,item8,item9,
               # item10,item11,item12,item13)

    bot.send_message(message.chat.id, 'Выберите инструмент для торговли', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'registration':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Позже добавлю')
        elif call.data == 'instruments':
            signalsList(message=call.message)
        elif call.data == 'eur_usd':
            signal(message=call.message,symbol1="EUR",symbol2="USD")
        elif call.data == 'usd_pln':
            signal(message=call.message,symbol1="USD",symbol2="PLN")
        elif call.data == 'usd_rub':
            signal(message=call.message,symbol1="USD",symbol2="RUB")
        elif call.data == 'usd_cad':
            signal(message=call.message,symbol1="USD",symbol2="CAD")
        elif call.data == 'usd_chf':
            signal(message=call.message,symbol1="USD",symbol2="CHF")
        elif call.data == 'back':
            signalsList(message=call.message)
        elif call.data == 'back_start':
            start(message=call.message)


bot.polling()




