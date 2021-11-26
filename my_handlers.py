from transitions import Machine
from db import db, get_or_create_user
from utils import keyboard, size_keyboard, payment_keyboard, accept_keyboard
from utils import PizzaOrder


client = PizzaOrder()
machine = Machine(model=client, states=client.states, transitions=client.transitions,
                  initial='pizza')


def start(update, context):
    """ Opens the keyboard with a command selection """
    update.message.reply_text('Здравствуйте. Чем могу помочь?', reply_markup=keyboard)


def new_order(update, context):
    """ start dialog """
    client.no()
    update.message.reply_text(client.hello(), reply_markup=size_keyboard)


def size_pizza(update, context):
    """ accepts a response and asks about payment """
    if not client.is_pizza():
        client.no()
        update.message.reply_text(client.hello(), reply_markup=size_keyboard)
    client.measure()
    client.size = update.message.text
    update.message.reply_text(client.how_pay(), reply_markup=payment_keyboard)


def payment(update, context):
    """ accepts the answer and asks everything is correct """
    if client.is_pizza():
        client.no()
        update.message.reply_text(client.hello(), reply_markup=size_keyboard)
    client.payment_method()
    client.payment = update.message.text
    update.message.reply_text(client.yes_or_no(), reply_markup=accept_keyboard)


def accept_order(update, context):
    """ If the answer is yes - we thank the client, if no we return to the beginning of the dialogue. """
    user = get_or_create_user(db, update.effective_user, update.message.chat.id, client)
    if update.message.text == 'Нет' or client.is_pizza():
        client.no()
        update.message.reply_text(client.hello(), reply_markup=size_keyboard)
    client.agreement()
    update.message.reply_text(client.thanks(), reply_markup=keyboard)


def wrong_message(update, context):
    """ If the input is not correct, we return to the beginning. """
    user = get_or_create_user(db, update.effective_user, update.message.chat.id, update.message)
    client.no()
    update.message.reply_text('Неправильный ввод! Давайте попробуем еще раз.')
    update.message.reply_text(client.hello(), reply_markup=size_keyboard)



