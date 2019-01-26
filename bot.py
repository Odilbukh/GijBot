# -*- coding: utf8 -*-
import telebot
import datetime
from telebot import types
from telegramcalendar import create_calendar
import config

bot = telebot.TeleBot(config.token)

print(bot.get_me())

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}), username - {4} \n Текст - {3}." .format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text,
                                                                 message.from_user.username))
    print(answer)



@bot.message_handler(commands=["start"])
def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ["📖 Меню", "🛋 Интерьер"]])
    keyboard.add(*[types.KeyboardButton(name) for name in ["ℹ️ О нас", "📣 Новости"]])
    keyboard.add(*[types.KeyboardButton(name) for name in ["🍽 Забронировать столик"]])
    mess = bot.send_message(message.chat.id, "Выберите действие ⤵️", reply_markup=keyboard)
    bot.register_next_step_handler(mess, menu)

@bot.message_handler(content_types=["text"])
def menu(message):
    if message.text == "ℹ️ О нас":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a = "Уютный ресторан в национальном стиле расположился в самом зеленом уголке центра Ташкента, объединив под одной крышей бухарский стиль, европейский темперамент и колорит. \n \n 🏡  Адрес: ул. Лабзак, 103 \n Ориентир: Напротив Колледж Связи и рядом с рестораном Афсона \n ☎️  +998 98 809 22 62 \n 🕘  09:00 - 23:00"
        b = "https://teletype.in/@gijduvonbot/BJF7dmkIm"
        d = "https://teletype.in/@gijduvonbot/rJlR89rwQ"
        bot.send_message(message.chat.id, a,  parse_mode="HTML", reply_markup=keyboard)
        bot.send_message(message.chat.id, b, parse_mode="HTML", reply_markup=keyboard)
        bot.send_message(message.chat.id, d, parse_mode="HTML", reply_markup=keyboard)
        print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
              ',',
              '@' + str(message.from_user.username), ',', str(message.from_user.language_code))

    if message.text == "📣 Новости":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        n = "Оставайтесь в курсе новостей и акций. \n<b>Gijduvon Restoran наш официальный сайт:</b>\n👉 http://gijduvon.uz/"
        h = "Ищите нас в социальных сетях. \n Мы в Инстаграме: https://www.instagram.com/restaurant_gijduvon/ \n Наш Фейсбук страница: https://www.facebook.com/gjduvon.kafe"
        bot.send_message(message.chat.id, n, parse_mode="HTML", reply_markup=keyboard)
        bot.send_message(message.chat.id, h, parse_mode="HTML", reply_markup=keyboard)
        print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
              ',',
              '@' + str(message.from_user.username), ',', str(message.from_user.language_code))



    if message.text == "📖 Меню":
        bot.send_photo(message.chat.id, photo=open('picture/menu.jpg', 'rb'))
        print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
              ',',
              '@' + str(message.from_user.username), ',', str(message.from_user.language_code))


    if message.text == "🛋 Интерьер":
        bot.send_photo(message.chat.id, photo=open('picture/pic1.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo=open('picture/pic2.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo=open('picture/pic3.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo=open('picture/pic4.jpg', 'rb'))
        print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
              ',',
              '@' + str(message.from_user.username), ',', str(message.from_user.language_code))


    if message.text == "🍽 Забронировать столик":
        t = "Пожалуйста, представьтесь:"
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ["Главное меню"]])
        bot.send_message(message.chat.id, t, parse_mode="HTML", reply_markup=keyboard)
        bot.register_next_step_handler(message, number)
        to_chat_id = "587471037"
        bot.forward_message(to_chat_id, message.from_user.id, message.message_id)
        print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
              ',',
              '@' + str(message.from_user.username), ',', str(message.from_user.language_code))

    if message.text == "Главное меню":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ["📖 Меню", "🛋 Интерьер"]])
        keyboard.add(*[types.KeyboardButton(name) for name in ["ℹ️ О нас", "📣 Новости"]])
        keyboard.add(*[types.KeyboardButton(name) for name in ["🍽 Забронировать столик"]])
        bot.send_message(message.chat.id, "Выберите действие ⤵️", reply_markup=keyboard)
        bot.register_next_step_handler(message, menu)
        print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
              ',',
              '@' + str(message.from_user.username), ',', str(message.from_user.language_code))

def number(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ["Главное меню"]])
    button_phone = types.KeyboardButton(text="📞  Отправить номер телефона", request_contact=True)
    keyboard.add(button_phone)
    mess = bot.send_message(message.chat.id, "Очень приятно,  {name}. Оставьте, пожалуйста, Ваш номер телефона: ".format(name=message.text), reply_markup=keyboard)
    bot.register_next_step_handler(mess, get_calendar)
    print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
          ',',
          '@' + str(message.from_user.username), ',', str(message.from_user.language_code))


current_shown_dates={}
@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    now = datetime.datetime.now() #Current date
    chat_id = message.chat.id
    date = (now.year,now.month)
    current_shown_dates[chat_id] = date #Saving the current date in a dict
    markup= create_calendar(now.year,now.month)
    bot.send_message(message.chat.id, "Пожалуйста, выберите дату", reply_markup=markup)
    print(str(message.from_user.first_name), ',', str(message.from_user.last_name), ',', str(message.from_user.id),
          ',',
          '@' + str(message.from_user.username), ',', str(message.from_user.language_code))



@bot.callback_query_handler(func=lambda call: call.data == 'next-month')
def next_month(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if(saved_date is not None):
        year,month = saved_date
        month+=1
        if month>12:
            month=1
            year+=1
        date = (year,month)
        current_shown_dates[chat_id] = date
        markup= create_calendar(year,month)
        bot.edit_message_text("Пожалуйста, выберите дату", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")
    else:
        #Do something to inform of the error
        pass

@bot.callback_query_handler(func=lambda call: call.data == 'previous-month')
def previous_month(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if(saved_date is not None):
        year,month = saved_date
        month-=1
        if month<1:
            month=12
            year-=1
        date = (year,month)
        current_shown_dates[chat_id] = date
        markup= create_calendar(year,month)
        bot.edit_message_text("Пожалуйста, выберите дату", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")

    else:
        #Do something to inform of the error
        pass

@bot.callback_query_handler(func=lambda call: call.data[0:13] == 'calendar-day-')
def get_day(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if(saved_date is not None):
        day=call.data[13:]
        date = datetime.datetime(int(saved_date[0]),int(saved_date[1]),int(day))
        msg = bot.send_message(chat_id, str(date))
        bot.answer_callback_query(call.id, text="Дата выбрана")
        chat = "587471037"
        bot.forward_message(chat, call.message.chat.id, call.message.message_id)
        bot.register_next_step_handler(msg, person)

    else:
        #Do something to inform of the error
        pass

def person(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=0.2)
    keyboard.add(*[types.KeyboardButton(name) for name in ["1", "2", "3", "4", "5", "6"]])
    keyboard.add(*[types.KeyboardButton(name) for name in ["Главное меню"]])
    mess = bot.send_message(message.chat.id, "Укажите количество персон:", reply_markup=keyboard)
    bot.register_next_step_handler(mess, answer)

def answer(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ["Главное меню"]])
    bot.send_message(message.chat.id, "Спасибо! Держите телефон при себе, оператор свяжется с Вами в ближайшее время для подтверждения брони", reply_markup=keyboard)
    bot.register_next_step_handler(message, main_menu)


if __name__ == '__main__':
    bot.polling(none_stop=True)
