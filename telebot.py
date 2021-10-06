from utils import compose_url_params
from requests import post

TELEGRAM_API_URL = "https://api.telegram.org"
TELEGRAM_BOT_URL = TELEGRAM_API_URL + "/bot{token}"
TELEGRAM_SEND_MESSAGE_URL = "/sendMessage"


class TelegramBot:
    def __init__(self, token):
        self.token = token

        self.bot_url = TELEGRAM_BOT_URL.format(token=self.token)

    def send_message(self, chat_id, text):
        send_message_url = self.bot_url + TELEGRAM_SEND_MESSAGE_URL
        params = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "MarkdownV2",
            "disable_web_page_preview": "true"
        }
        formatted_url = f"{send_message_url}/{compose_url_params(params)}"
        response = post(formatted_url)
        return response.status_code
