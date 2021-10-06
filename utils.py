from urllib.parse import quote
import re


def compose_url_params(params):
    return '?' + '&'.join(f"{param}={quote(value)}" for param, value in params.items())


def escape_markdown(text):
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)
