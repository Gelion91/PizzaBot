from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
from my_handlers import *
from utils import buttons_size, buttons_payment, buttons_accept


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def main():
    """Bot body"""
    mybot = Updater(settings.API_KEY, use_context=True)

    logging.info('Бот запускается')
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', start, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('Заказать пиццу!'), new_order, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text(buttons_size), size_pizza, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text(buttons_payment), payment, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text(buttons_accept), accept_order, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, wrong_message, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
