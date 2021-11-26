PizzaBot
========

PizzaBot - бот для Telegram в котором вы можете заказать пиццу.

Установка
=========

Создайте виртуальное окружение и активируйте его. В виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt

Настройка
---------

Создайте файл settings.py добавьте туда следующие настройки

.. code-block::

    API_KEY = 'Ваш токен от BotFather'
    MONGO_LINK = "url вашего сервера mongoDB"
    MONGO_DB = "Название вашей базы данных"


Запуск
-------

В активированном виртуальном окружении выполните

.. code-block::

    python bot.py
