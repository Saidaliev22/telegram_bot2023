import telebot
from telebot import types

bot = telebot.TeleBot("6386172369:AAFwCWxCWf3622XAFkbHVu2Rs3CmizkUJf4")


#КОМАНДЫ
@bot.message_handler(commands=['start'])
def start(message):
    keyboardreply = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("1 курс")
    button2 = types.KeyboardButton("2 курс")
    button3 = types.KeyboardButton("3 курс")
    button4 = types.KeyboardButton("4 курс")
    button5 = types.KeyboardButton("5 курс")
    button6 = types.KeyboardButton("6 курс")
    keyboardreply.add(button1, button4)
    keyboardreply.add(button2, button5)
    keyboardreply.add(button3, button6)

    keyboardinl = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text="Поделиться", switch_inline_query="\n\nВ телеграмботе MED STUDENTS вы можете найти:"
                                                                                "\n\n⭐️Медицинские книги📚"
                                                                                "\n⭐️Тесты и итоги📒"
                                                                                "\n⭐️Видеоролики📹 и ответы на экзаменационных вапросах📓"
                                                                                "\n⭐️Методички и много интересной информации о медицине🩺 и ТГМУ🏠"
                                                                                "\n\n\nЧтобы исползовать бот подписываете на @MedStudentstjBot")
    keyboardinl.add(button1)

    bot.send_message(message.chat.id, f"👋 Ассалому алайкум, {message.from_user.first_name}! \n \n "
                                      f"<b>Добро пожаловать в наш телеграм бот @MedStudentstjBot</b>\n \n"
                                      f"Чтобы поддержать нас, поделитесь друзьям ссылка бота!", parse_mode="html", reply_markup=keyboardinl)
    bot.send_message(message.chat.id, "Выберите ваш курс:", reply_markup=keyboardreply)

#Предметы 5-го курса
@bot.message_handler(content_types=["text"])
def get_text(message):
        if message.text == "5 курс":
            keyboardinl1 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Анестизиология и реаниматология", callback_data='Anestiziology+reanimotology')
            button2 = types.InlineKeyboardButton(text="Внутренние болезни", callback_data='Vnytrenniy-bolezni')
            button3 = types.InlineKeyboardButton(text="Гинекология", callback_data='Ginekology')
            button4 = types.InlineKeyboardButton(text="Детская хирургия", callback_data='Detskaya-khirurgiya')
            button5 = types.InlineKeyboardButton(text="Педиатрия", callback_data='Pediatriya')
            button6 = types.InlineKeyboardButton(text="Политология", callback_data='Politology')
            button7 = types.InlineKeyboardButton(text="Психиатрия", callback_data='Psikhiatriya')
            button8 = types.InlineKeyboardButton(text="Семейная медицина", callback_data='Semeynaya-medicine')
            button9 = types.InlineKeyboardButton(text="Сосудистая хирургия", callback_data='Sosudistaya-khirurgiya')
            button10 = types.InlineKeyboardButton(text="Социальная гигиена", callback_data='Soc-gigiena')
            button11 = types.InlineKeyboardButton(text="Стоматология", callback_data='Stomatology')
            button12 = types.InlineKeyboardButton(text="Травматология и ВПХ", callback_data='Travmatology')
            button13 = types.InlineKeyboardButton(text="Урология", callback_data='Urology')
            button14 = types.InlineKeyboardButton(text="Фтизиатрия", callback_data='Ftiziatriya')
            button15 = types.InlineKeyboardButton(text="Эпидемиология", callback_data='Epidemiology')
            button16 = types.InlineKeyboardButton(text="◀️Выбор курса", callback_data='Vibor-kursa')
            keyboardinl1.add(button1)
            keyboardinl1.add(button2, button3)
            keyboardinl1.add(button4, button5)
            keyboardinl1.add(button6, button7)
            keyboardinl1.add(button8, button9)
            keyboardinl1.add(button10, button11)
            keyboardinl1.add(button12, button13)
            keyboardinl1.add(button14, button15)
            keyboardinl1.add(button16)
            bot.send_message(message.chat.id, "Выберите нужный предмет:", reply_markup=keyboardinl1)



#Кнопки предметы 5-го курса
@bot.callback_query_handler(lambda callback: callback.data)
def viborpredmet(predmet):
        if predmet.data == "Anestiziology+reanimotology":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Anestiziology+reanimotology")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Anestiziology+reanimotology')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Anestiziology+reanimotology')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Анестизиология и реаниматология\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Vnytrenniy-bolezni":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Vnytrenniy-bolezni")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Vnytrenniy-bolezni')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Vnytrenniy-bolezni')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Внутренние болезни\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Ginekology":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Ginekology")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Ginekology')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Ginekology')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Гинекология\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Detskaya-khirurgiya":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Detskaya-khirurgiya")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Detskaya-khirurgiya')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Detskaya-khirurgiya')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Детская хирургия\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Pediatriya":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Pediatriya")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Pediatriya')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Pediatriya')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Педиатрия\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Politology":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Politology")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Politology')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Politology')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Политология\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Psikhiatriya":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Psikhiatriya")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Psikhiatriya')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Psikhiatriya')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Психиатрия\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Semeynaya-medicine":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Semeynaya-medicine")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Semeynaya-medicine')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Semeynaya-medicine')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Семейная медицина\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Sosudistaya-khirurgiya":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Sosudistaya-khirurgiya")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Sosudistaya-khirurgiya')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Sosudistaya-khirurgiya')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Сосудистая хирургия\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Soc-gigiena":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Soc-gigiena")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Soc-gigiena')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Soc-gigiena')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Социальная гигиена\n\n:", reply_markup=keyboardinl2)

        elif predmet.data == "Stomatology":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Stomatology")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Stomatology')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Stomatology')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Стоматология\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Travmatology":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Travmatology")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Travmatology')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Travmatology')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Травматология и ВПХ\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Urology":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Urology")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Urology')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Urology')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Урология\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Ftiziatriya":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Ftiziatriya")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Ftiziatriya')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Ftiziatriya')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Фтизиатрия\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Epidemiology":
            keyboardinl2 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data="Knigi-Epidemiology")
            button2 = types.InlineKeyboardButton(text="Экзамен 💾", callback_data='Ekzamen-Epidemiology')
            button3 = types.InlineKeyboardButton(text="Темы (Лекции+Видеоролики)", callback_data='Temi-Epidemiology')
            button4 = types.InlineKeyboardButton(text="◀️Назад", callback_data='Nazad-k-vibor-predmet')
            keyboardinl2.add(button1,button2)
            keyboardinl2.add(button3)
            keyboardinl2.add(button4)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="✅Эпидемиология\n\nВыберите нужный материал:", reply_markup=keyboardinl2)

        elif predmet.data == "Vibor-kursa":
            keyboardreply = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button1 = types.KeyboardButton("1 курс")
            button2 = types.KeyboardButton("2 курс")
            button3 = types.KeyboardButton("3 курс")
            button4 = types.KeyboardButton("4 курс")
            button5 = types.KeyboardButton("5 курс")
            button6 = types.KeyboardButton("6 курс")
            keyboardreply.add(button1, button4)
            keyboardreply.add(button2, button5)
            keyboardreply.add(button3, button6)
            bot.edit_message_text(chat_id=predmet.message.chat.id, message_id=predmet.message.id, text="Выберите ваш курс:", reply_markup=keyboardreply)



@bot.message_handler()
def info(message):
        bot.reply_to(message, 'Я вас не понял 😞. Пожалуйста, используйте команды или кнопки!')



bot.polling(none_stop=True)