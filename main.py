#  Имя бота @Go_Pip_bot
from aiogram import Bot, Dispatcher, executor
from telegram_bot_pagination import InlineKeyboardPaginator
from time import sleep
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery, ContentTypes, InlineKeyboardButton,\
    ShippingQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import get_main_kb, get_product_menu, get_order_kb
from functions import get_products_by_category, get_information_about_product
from text import start_text, info, feedbacks, help_
from aiogram.dispatcher.filters.state import State, StatesGroup
from DataBase import db
from products import REGULAR_SHIPPING, PICKUP_SHIPPING, POST_SHIPPING
from random import randint
from pprint import pprint

try:
    db.create_table_users()
    print('Таблица создана')
except Exception as e:
    print(e)


PAYMENTS_PROVIDER_TOKEN = '1744374395:TEST:3df80783d8f7c5a67893'
bot = Bot(token='5242108987:AAFAdO7Rx3OJCi6RedUyPg8ioyKdBNS3iRk')
dp = Dispatcher(bot, storage=MemoryStorage())


async def send_product_page(user_id, page=1, call=None, msg=None):
    if msg:
        category = msg.text[:-2]
    else:
        category = call.data.split('#')[0]
    products = await get_products_by_category(category)

    paginator = InlineKeyboardPaginator(
        len(products),
        current_page=page,
        data_pattern=category + '#{page}'
    )
    paginator.add_after(InlineKeyboardButton('Вернуться к категориям', callback_data='BackToCategories'))

    if category in ('Аксессуары', 'Мячи'):
        paginator.add_before(
            InlineKeyboardButton('Добавить в корзину', callback_data='AddToCart#{}#{}'.format(category, page))
        )

    elif category in ('Майки', 'Худи', 'Шорты'):
        paginator.add_before(
            InlineKeyboardButton('38', callback_data='AddToCart#{}#{}#38'.format(category, page)),
            InlineKeyboardButton('40', callback_data='AddToCart#{}#{}#40'.format(category, page)),
            InlineKeyboardButton('42', callback_data='AddToCart#{}#{}#42'.format(category, page)),
        )
        paginator.add_before(
            InlineKeyboardButton('44', callback_data='AddToCart#{}#{}#44'.format(category, page)),
            InlineKeyboardButton('46', callback_data='AddToCart#{}#{}#46'.format(category, page)),
            InlineKeyboardButton('48', callback_data='AddToCart#{}#{}#48'.format(category, page)),
        )
        paginator.add_before(
            InlineKeyboardButton('50', callback_data='AddToCart#{}#{}#50'.format(category, page)),
            InlineKeyboardButton('52', callback_data='AddToCart#{}#{}#52'.format(category, page)),
            InlineKeyboardButton('54', callback_data='AddToCart#{}#{}#54'.format(category, page)),
        )
        paginator.add_before(
            InlineKeyboardButton(' ⬆Размеры ⬆', callback_data='pass'.format(category, page))
        )

    elif category == 'Носки':
        paginator.add_before(
            InlineKeyboardButton('S', callback_data='AddToCart#{}#{}#S'.format(category, page)),
            InlineKeyboardButton('M', callback_data='AddToCart#{}#{}#M'.format(category, page)),
            InlineKeyboardButton('L', callback_data='AddToCart#{}#{}#L'.format(category, page)),
            InlineKeyboardButton('XL', callback_data='AddToCart#{}#{}#XL'.format(category, page))
        )
        paginator.add_before(
            InlineKeyboardButton(' ⬆Размеры ⬆', callback_data='pass'.format(category, page))
        )

    else:
        paginator.add_before(
            InlineKeyboardButton('39', callback_data='AddToCart#{}#{}#39'.format(category, page)),
            InlineKeyboardButton('40', callback_data='AddToCart#{}#{}#40'.format(category, page)),
            InlineKeyboardButton('41', callback_data='AddToCart#{}#{}#41'.format(category, page)),
        )
        paginator.add_before(
            InlineKeyboardButton('42', callback_data='AddToCart#{}#{}#42'.format(category, page)),
            InlineKeyboardButton('43', callback_data='AddToCart#{}#{}#43'.format(category, page)),
            InlineKeyboardButton('44', callback_data='AddToCart#{}#{}#44'.format(category, page)),
        )
        paginator.add_before(
            InlineKeyboardButton('45', callback_data='AddToCart#{}#{}#45'.format(category, page)),
            InlineKeyboardButton('46', callback_data='AddToCart#{}#{}#46'.format(category, page)),
            InlineKeyboardButton('47', callback_data='AddToCart#{}#{}#47'.format(category, page)),
        )
        paginator.add_before(
            InlineKeyboardButton(' ⬆Размеры ⬆', callback_data='pass'.format(category, page))
        )

    await bot.send_photo(
        chat_id=user_id,
        photo=products[page - 1]['image'],
        caption=await get_information_about_product(products[page - 1]),
        reply_markup=paginator.markup, parse_mode='Markdown'
    )


class User(StatesGroup):
    order = State()


@dp.message_handler(commands='start')
async def cmd_start(message: Message):
    await message.answer(text=start_text, reply_markup=get_main_kb())


@dp.message_handler(content_types='text')
async def cmd_get_text(message: Message):
    if message.text == 'Информация ℹ':
        await message.answer(text=info, reply_markup=get_main_kb())

    elif message.text == 'Отзывы 👥':
        for text in feedbacks:
            sleep(0.8)
            await message.answer(text=text)
        await message.answer(text='Выберите действие:', reply_markup=get_main_kb())

    elif message.text == 'Сделать заказ 🛎':
        await message.answer('Выберите категорию:', reply_markup=get_product_menu())

    elif message.text == 'Помощь 🆘':
        await message.answer(help_)
        sleep(2)
        await message.answer('Выберите категорию:', reply_markup=get_product_menu())

    elif message.text in ('Аксессуары 🕶', 'Носки 🧦', 'Худи 💣', 'Шорты 🩳', 'Кроссовки 👟', 'Майки 🎽', 'Мячи 🏀'):
        await send_product_page(user_id=message.from_user.id,
                                page=1,
                                msg=message)

    elif message.text == 'Корзина 🗑':
        await message.answer('Что вы хотите сделать?', reply_markup=get_order_kb())

    else:
        await message.answer('Пожалуйста, чтобы не было недопонимания и ошибок, пользуйтесь кнопками)')
        sleep(2)
        await message.answer('Выберите действие:', reply_markup=get_main_kb())


@dp.callback_query_handler(text='BackToCategories')
async def return_to_categories_list(call: CallbackQuery):
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    await bot.send_message(
        chat_id=call.from_user.id, text='Возврат в меню с категориями')
    sleep(1.3)
    await call.message.answer('Выберите категорию:', reply_markup=get_product_menu())


@dp.callback_query_handler(lambda call: call.data.split('#')[0] == 'AddToCart')
async def add_to_order(call: CallbackQuery, state: FSMContext):
    if len(call.data.split('#')) == 4:
        _, category, page, size = call.data.split('#')
    else:
        _, category, page = call.data.split('#')
        size = 'Безразмерный'
    products = await get_products_by_category(category)

    async with state.proxy() as data:
        new_product = products[int(page) - 1]
        new_product['size'] = size

        if 'products' in data:
            products = data['products']
        else:
            data['products'] = list()
            products = data['products']
        products.append(new_product)

    await call.answer('Товар добавлен в корзину!')


@dp.callback_query_handler(Text(startswith='order'))
async def get_call(call: CallbackQuery, state: FSMContext):
    if call.data == 'order_clean':
        async with state.proxy() as data:
            if 'products' not in data:
                await call.answer('Вы еще ничего не добавили в корзину')
                return
            data.clear()
            await call.message.answer('Ваша корзина очищена!', reply_markup=get_product_menu())
            await call.message.answer('Выберите категорию:', reply_markup=get_product_menu())

    elif call.data == 'order_my':
        async with state.proxy() as data:
            if 'products' not in data:
                await call.answer('Вы еще ничего не добавили в корзину')
                return

            products = data['products']
            summary = {'mapping_dish_to_amount': dict()}

            for product in products:
                product_name = product['name']

                if 'size' in product:
                    size = product['size']
                    if size != 'Безразмерный':
                        product_name = product_name + ', размер: ' + size

                if product_name not in summary['mapping_dish_to_amount']:
                    summary['mapping_dish_to_amount'][product_name] = 1
                else:
                    summary['mapping_dish_to_amount'][product_name] += 1

            user_order = '\n'.join(
                [f'{count} x {name}' for name, count in summary['mapping_dish_to_amount'].items()])

            await call.message.edit_text(f'Ваша корзина:\n{user_order}')
            sleep(2)
            await call.message.answer('Что вы хотите сделать?', reply_markup=get_order_kb())

    else:
        async with state.proxy() as data:
            if 'products' not in data:
                await call.answer('Вы еще ничего не добавили в корзину')
                return

            products = data['products']
            prices = []
            summary = {'mapping_dish_to_amount': dict()}

            for product in products:
                prices.append(LabeledPrice(label=f"{product['name']}, размер {product['size']}",
                                           amount=product['price'] * 100))
                product_name = product['name']

                if 'size' in product:
                    size = product['size']
                    if size != 'Безразмерный':
                        product_name = product_name + ', размер: ' + size

                if product_name not in summary['mapping_dish_to_amount']:
                    summary['mapping_dish_to_amount'][product_name] = 1
                else:
                    summary['mapping_dish_to_amount'][product_name] += 1

            user_order = '\n'.join(
                [f'{count} x {name}' for name, count in summary['mapping_dish_to_amount'].items()])
            data['order'] = user_order

            message_to_user = 'Пожалуйста, убедитесь, что Вы добавили нужные Вам размеры)'

            await bot.send_invoice(
                call.message.chat.id,
                title='Заказ в онлайн магазине',
                description=message_to_user,
                provider_token=PAYMENTS_PROVIDER_TOKEN,
                currency='rub',
                photo_url='https://thumbs.dreamstime.com/b/%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%8C-%D0%B1%D1%83%D1%84%D0%B5%D1%80%D0%B0-%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD%D0%B0-%D1%86%D0%B2%D0%B5%D1%82%D0%B0-%D0%BF%D0%B8%D0%BA%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%B3%D0%BE%D0%BB%D1%83%D0%B1%D0%BE%D0%B9-187733011.jpg',
                photo_height=512,
                photo_width=512,
                photo_size=512,
                prices=prices,
                start_parameter='time-machine-example',
                payload=str(randint(10000000, 99999999)),
                is_flexible=True,
                need_shipping_address=True
            )


@dp.callback_query_handler(text='pass')
async def cmd_pass(call: CallbackQuery):
    await call.answer('Эта кнопка ничего не делает)')


@dp.callback_query_handler()
async def dishes_page_callback(call: CallbackQuery):
    page = int(call.data.split('#')[1])
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    await send_product_page(user_id=call.from_user.id,
                            page=page,
                            call=call)


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message='Не повезло, не фартануло, деньги ушли в никуда...')


@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: Message, state: FSMContext):
    await message.answer('Мы получили Ваш платеж за заказ')

    data = await state.get_data()
    user_order = data.get('order')
    await state.finish()

    pprint(message)
    id_order = message['successful_payment']["invoice_payload"]
    ship_type = message['successful_payment']["shipping_option_id"]
    region = message['successful_payment']['order_info']["shipping_address"]["state"]
    city = message['successful_payment']['order_info']["shipping_address"]["city"]
    street1 = message['successful_payment']['order_info']["shipping_address"]["street_line1"]
    street2 = message['successful_payment']['order_info']["shipping_address"]["street_line2"]
    place = region + ' ' + city + ' ' + street1 + ' ' + street2

    db.add_user(user_id=message.from_user.id,
                id_purchase=int(id_order),
                status='paid',
                purchase_text=user_order,
                ship_type=ship_type,
                place=place)

    await message.answer('Чтобы узнать подробности о доставке товара напишите @Yan_03_0')
    sleep(2)
    await message.answer('Если хотите заказать ещё что-то, введите /start')


@dp.shipping_query_handler()
async def choice_shipping(query: ShippingQuery):
    if query.shipping_address.country_code == 'RU':
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[
                                                        REGULAR_SHIPPING,
                                                        PICKUP_SHIPPING,
                                                        POST_SHIPPING
                                                        ], ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message='Сюда не доставляем')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
