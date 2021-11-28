from transitions import Machine

from db import get_or_create_user, db
from utils import keyboard, size_keyboard, payment_keyboard, accept_keyboard
from utils import PizzaOrder


def start(update, context):
    """ Opens the keyboard with a command selection """
    user_data = context.user_data
    update.message.reply_text('Здравствуйте. Чем могу помочь?', reply_markup=keyboard)


def new_order(update, context):
    """ start dialog """
    user_data = context.user_data
    if not user_data:
        client = PizzaOrder()
        machine = Machine(model=client, states=client.states, transitions=client.transitions,
                          initial='pizza')
        user_data['data'] = client
    user_data['data'].no()
    update.message.reply_text(user_data['data'].hello(), reply_markup=size_keyboard)


def size_pizza(update, context):
    """ accepts a response and asks about payment """
    user_data = context.user_data
    if user_data:
        if not user_data['data'].is_pizza():
            user_data['data'].no()
            update.message.reply_text(user_data['data'].hello(), reply_markup=size_keyboard)
        user_data['data'].measure()
        user_data['data'].size = update.message.text
        update.message.reply_text(user_data['data'].how_pay(), reply_markup=payment_keyboard)
    else:
        update.message.reply_text('Здравствуйте. Чем могу помочь?', reply_markup=keyboard)


def payment(update, context):
    """ accepts the answer and asks everything is correct """
    user_data = context.user_data
    if user_data:
        if user_data['data'].is_pizza():
            user_data['data'].no()
            update.message.reply_text(user_data['data'].hello(), reply_markup=size_keyboard)
        user_data['data'].payment_method()
        user_data['data'].payment = update.message.text
        update.message.reply_text(user_data['data'].yes_or_no(), reply_markup=accept_keyboard)
    else:
        update.message.reply_text('Здравствуйте. Чем могу помочь?', reply_markup=keyboard)


def accept_order(update, context):
    """ If the answer is yes - we thank the client, if no we return to the beginning of the dialogue. """
    user_data = context.user_data
    if user_data:
        if update.message.text == 'Нет' or user_data['data'].is_pizza():
            user_data['data'].no()
            update.message.reply_text(user_data['data'].hello(), reply_markup=size_keyboard)
        user = get_or_create_user(db, update.effective_user, update.message.chat.id, user_data['data'])
        user_data['data'].agreement()
        update.message.reply_text(user_data['data'].thanks(), reply_markup=keyboard)
    else:
        update.message.reply_text('Здравствуйте. Чем могу помочь?', reply_markup=keyboard)


def wrong_message(update, context):
    """ If the input is not correct, we return to the beginning. """
    user_data = context.user_data
    if user_data:
        user_data['data'].no()
        update.message.reply_text('Неправильный ввод! Давайте попробуем еще раз.')
        update.message.reply_text(user_data['data'].hello(), reply_markup=size_keyboard)
    else:
        update.message.reply_text('Здравствуйте. Чем могу помочь?', reply_markup=keyboard)



