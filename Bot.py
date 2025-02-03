import winrate
import transactions
import ROI
import telebot
import time
import schedule
from time import sleep
from threading import Thread

TOKEN = '7316210049:AAEM0fEPCEpxYti-nNEJGLB36gD1l3K9qoQ'
bot = telebot.TeleBot(TOKEN)
user_chat_ids = set()
markup = 0
def reconnect():
    try:
        TOKEN = '7316210049:AAEM0fEPCEpxYti-nNEJGLB36gD1l3K9qoQ'
        bot = telebot.TeleBot(TOKEN)
    except:
        reconnect()

f = open('9.csv')

wallets =[]
for s in f:
    wallets.append((list(map(str, s.split('\n'))))[0])




@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "Бот присылает уведомления о совершении сделки одним из криптоинсайдерских кошельков. "
        "Вам остается только не пропускать сообщения и покупать активы на бирже.\n"
        "Мы отслеживаем более 1000 счетов путем декодирования блокчейна. Можно добавлять и анализировать как свои кошельки, так и по умолчанию пользоваться нашей базой. "
        "Мы выступаем против инсайдерской торговли и считаем, что информация должна быть доступна всем! "
        "Ни одна спекуляция на рынке не останется незамеченной :)\n"
        "Удачной торговли!\n"
        "Авторы проекта: VADIM PANKOV & FAUSTMIDAS"
    )
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('Отслеживать кошельки', 'Проверить кошелек', 'Купить подписку')
    chat_id = message.chat.id
    if chat_id not in user_chat_ids:
        user_chat_ids.add(chat_id)  # Add chat_id to the set if not already added
        bot.send_message(chat_id, welcome_message,reply_markup=markup)




@bot.message_handler(func=lambda message: True)
def handler(message):
    threading_schedule = Thread(target=setup_schedule)
    if message.text.find("0x") > -1:
        ind = message.text
        tr = transactions.run(ind)
        wr = winrate.main(ind)
        roi = ROI.getROI(ind)
        mes = "Wallet " + "\n" + ind + "\n" + "Winrate " + "\n" + str(wr) + "\n" + "ROI " + "\n" + str(roi) + "\n" + "Transactions: " + "\n" + tr + "\n"
        bot.reply_to(message, mes)

    elif message.text == 'Отслеживать кошельки':
        bot.reply_to(message, "Теперь каждый час вы будете получать уведомления")
        threading_schedule = Thread(target=setup_schedule)
        threading_schedule.start()
        markup.add('Выключить уведомления', 'Проверить кошелек', 'Купить подписку')
    elif message.text == 'Выключить уведомления':
        threading_schedule.stop()
    elif message.text == 'Проверить кошелек':
        bot.reply_to(message, "Введите номер кошелька")

    elif message.text == 'Купить подписку':
        bot.reply_to(message, "Купи слона")
    elif message.text == 'Админка':
        bot.reply_to(message, "админка")
    else:
        bot.reply_to(message, "Please choose a valid option from the menu.")






# Function that sends an hourly message to all known user chat IDs
def send_hourly_message():
    mes = text()
    if len(mes)>0:
        for chat_id in user_chat_ids:
            try:
                bot.send_message(chat_id, mes)
            except:
                reconnect()
                bot.send_message(chat_id, mes)
    else:
        for chat_id in user_chat_ids:
            try:
                bot.send_message(chat_id, "no transactions")
            except:
                reconnect()
                bot.send_message(chat_id, "no transactions")


def setup_schedule():
    schedule.every().minute.do(send_hourly_message)
    while True:
        schedule.run_pending()
        time.sleep(1)


def text():
    mes = ""
    for i in range(0, 10):
        tr = transactions.run(wallets[i])
        #print(tr)
        if len(tr) > 0:
            wr = winrate.main(wallets[i])
            roi = ROI.getROI(wallets[i])
            mes += "Wallet " + "\n" + str(wallets[i]) + "\n" + "Winrate " + "\n" + str(wr) + "\n" + "ROI " + "\n" + str(roi) + "\n" +  "Transactions: " +"\n" + tr +"\n"

    return mes



def bot_polling():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as _ex:
            print(_ex)
            sleep(15)

if __name__ == '__main__':
    from threading import Thread

    # Thread to keep the bot polling (listening)
    threading_bot = Thread(target=bot_polling)
    threading_bot.start()
    threading_bot.join()


