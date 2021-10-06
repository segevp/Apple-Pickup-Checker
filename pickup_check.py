from inventory import InventoryLookup
from telebot import TelegramBot
from utils import escape_markdown
from argparse import ArgumentParser

AVAILABLE_MESSAGE = r"""*The Item {model_name} is Available\!*
Available in the following stores:
"""
UNAVAILABLE_MESSAGE = "*{model}* is currently *not available* at the {num_stores} nearest stores"


def format_available_store(store_json):
    store_name = escape_markdown(store_json['storeName'])
    store_url = escape_markdown(store_json['reservationUrl'])
    distance = escape_markdown(store_json['storeDistanceWithUnit'])
    return f"""\\- [Apple {store_name}]({store_url}) \\({distance}\\)"""


def get_args():
    parser = ArgumentParser()
    parser.add_argument("token")
    parser.add_argument("chat_id")
    parser.add_argument("model")
    parser.add_argument("zipcode")
    args = parser.parse_args()
    print(args)


def run(model, zipcode, token, chat_id):
    bot = TelegramBot(token)
    stock = InventoryLookup(model=model, zipcode=zipcode)
    if not stock.available_stores:
        message = UNAVAILABLE_MESSAGE.format(model=stock.model_name, num_stores=len(stock.stores))
        bot.send_message(chat_id, message)
        print("NOT ", end='')
    else:
        message = AVAILABLE_MESSAGE.format(model_name=stock.model_name) \
                  + "\n".join(format_available_store(store) for store in stock.available_stores)
        bot.send_message(chat_id, message)
    print("AVAILABLE")


if __name__ == '__main__':
    args = vars(get_args())
    run(**args)
