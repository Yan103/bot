from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def get_main_kb():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_info = KeyboardButton('Информация ℹ')
    btn_feedbacks = KeyboardButton('Отзывы 👥')
    btn_start_order = KeyboardButton('Сделать заказ 🛎')
    menu.add(btn_info, btn_feedbacks)
    menu.add(btn_start_order)
    return menu


def get_product_menu():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_balls = KeyboardButton('Мячи 🏀')
    btn_t_shirts = KeyboardButton('Майки 🎽')
    btn_shoes = KeyboardButton('Кроссовки 👟')
    btn_shorts = KeyboardButton('Шорты 🩳')
    btn_hoodie = KeyboardButton('Худи 💣')
    btn_socks = KeyboardButton('Носки 🧦')
    btn_acs = KeyboardButton('Аксессуары 🕶')
    btn_order = KeyboardButton('Корзина 🗑')
    btn_help = KeyboardButton('Помощь 🆘')
    menu.add(btn_balls, btn_shoes).add(btn_t_shirts, btn_shorts).add(btn_hoodie, btn_socks)\
        .add(btn_acs, btn_help).add(btn_order)
    return menu


def get_order_kb():
    order = InlineKeyboardMarkup()
    order.add(InlineKeyboardButton(text='Мой заказ', callback_data='order_my'),
              InlineKeyboardButton(text='Оформить', callback_data='order_make'),
              InlineKeyboardButton(text='Очистить', callback_data='order_clean'))
    order.add(InlineKeyboardButton(text='Вернуться к категориям', callback_data='BackToCategories'))
    return order


def get_user_post_kb():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu.add(KeyboardButton(text='Данные заказа'),
             KeyboardButton(text='Заказ получен'))
    menu.add(KeyboardButton(text='Отменить заказ'))
    return menu
