



@bot.message_handler(commands=['start'])
def start(message):
    keyboardreply = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button5 = types.KeyboardButton("1 курс")
    keyboardreply.add(button5)
    bot.send_message(message.chat.id, f"👋 Ассалому алайкум {message.from_user.first_name}! \n \n "
                                      f"Выберите ваш курс:", parse_mode="html", reply_markup=keyboardreply)



@bot.message_handler(content_types=["text"])
def get_text(message):
        if message.text == "1 курс":
            keyboardinl = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Анатомия", callback_data='Anatomiya')
            button2 = types.InlineKeyboardButton(text="Выбор курса", callback_data='vibor kurs')
            keyboardinl.add(button1)
            keyboardinl.add(button2)
            bot.send_message(message.chat.id, "Выберите нужный предмет:", reply_markup=keyboardinl)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
        if call.data == "Anatomiya":
            keyboardinl3 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text="Книги 📚", callback_data='Knigi-Anatomiya')
            keyboardinl3.add(button1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Выберите нужный материал:", reply_markup=keyboardinl3)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
        if call.data == "Knigi-Anatomiya":
            bot.send_message(message.chat.id, "Книги:")