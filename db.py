from pymongo import MongoClient

import settings

db = MongoClient(settings.MONGO_LINK)[settings.MONGO_DB]


def get_or_create_user(db, effective_user, chat_id, order):
    order = {
        "user_id": effective_user.id,
        "first_name": effective_user.first_name,
        "last_name": effective_user.last_name,
        "username": effective_user.username,
        "chat_id": chat_id,
        "pizza_size": order.size,
        "payment": order.payment,
    }
    db.clients.insert_one(order)
    return order