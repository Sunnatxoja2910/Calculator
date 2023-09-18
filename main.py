from telebot import types, TeleBot

import func
from func import add_user
from button import buttons
bot = TeleBot("6685829273:AAFZpJ3w5F7sz1zyn4gR5FMN6ucgvmSbeIA")



@bot.message_handler(commands=['start'])
def start(message:types.Message):
    add_user(message.chat.id)
    bot.send_message(message.chat.id, "Salamalekom botka xush kebsiz",reply_markup=buttons)

@bot.callback_query_handler(func=lambda a:a.data)
def cdrest(message:types.CallbackQuery):
    def sonlar(n):


        func.changeson(message.from_user.id, n)
        data = func.get_son(message.from_user.id)
        matn = ""
        for i in data:
            matn += i
            try:
                bot.edit_message_text(f"hozirgi holat:\n\n{matn}", message.from_user.id,
                                      message.message.id, reply_markup=buttons)
            except:
                pass

    def amallar(amal):
        func.changeamal(message.from_user.id, amal)
        func.change_belgi(message.from_user.id)
        data = func.get_son(message.from_user.id)
        matn = ""
        for i in data:
            matn += i
        try:
            bot.edit_message_text(f"hozirgi holat:\n\n{matn}", message.from_user.id,
                                  message.message.id, reply_markup=buttons)
        except:
            pass
    match message.data:
        case "1":
            sonlar(1)
        case "2":
            sonlar(2)
        case "3":
            sonlar(3)
        case "4":
            sonlar(4)
        case "5":
            sonlar(5)
        case "6":
            sonlar(6)
        case "7":
            sonlar(7)
        case "8":
            sonlar(8)
        case "9":
            sonlar(9)
        case "0":
            sonlar(0)
        case "*":
            amallar("*")
        case "+":
            amallar("+")
        case "+":
            amallar("+")
        case "/":
            amallar("/")
        case "-":
            amallar("-")
        case "RESULT":
            # try:
                bot.edit_message_text(f"Natija\n\n{func.GetRes(message.from_user.id)}",message.from_user.id,message.message.id,reply_markup=buttons)
            # except:
            #     bot.send_message(message.from_user.id,"ishlamadi")
        case "CLEAR":
            bot.edit_message_text(f"{func.clear(message.from_user.id)}",message.from_user.id,message.message.id,reply_markup=buttons)






bot.polling(none_stop=True)
