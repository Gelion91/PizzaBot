from telegram import ReplyKeyboardMarkup
from transitions import State

reply_keyboard = [
    ['Заказать пиццу!']
]
buttons_size = ['Большую', 'Маленькую']
buttons_payment = ['Наличкой', 'По карте']
buttons_accept = ['Да', 'Нет']


keyboard = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=False)
size_keyboard = ReplyKeyboardMarkup.from_row(buttons_size, resize_keyboard=True)
payment_keyboard = ReplyKeyboardMarkup.from_row(buttons_payment, resize_keyboard=True)
accept_keyboard = ReplyKeyboardMarkup.from_row(buttons_accept, resize_keyboard=True)


class PizzaOrder:
    """finite state machine"""
    size = None
    payment = None

    states = ['pizza', 'pay', 'accept', 'thanks']

    states = [
        State(name='pizza', on_enter='hello'),
        State(name='pay', on_enter='how_pay'),
        State(name='accept', on_enter='yes_or_no'),
        State(name='thanks', on_enter='thanks')

    ]
    transitions = [
        {'trigger': 'measure', 'source': 'pizza', 'dest': 'pay'},
        {'trigger': 'payment_method', 'source': 'pay', 'dest': 'accept'},
        {'trigger': 'agreement', 'source': 'accept', 'dest': 'thanks'},
        {'trigger': 'no', 'source': '*', 'dest': 'pizza'}
    ]

    def hello(self):
        return "Какую вы хотите пиццу? Большую или маленькую?"

    def how_pay(self):
        return "Как вы будете платить?"

    def yes_or_no(self):
        return f"Вы хотите {self.size} пиццу, оплата - {self.payment}?".capitalize()

    def thanks(self):
        return "Спасибо за заказ."


