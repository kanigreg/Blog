import json
import requests
from flask_babel import _
from application import app
from requests.utils import requote_uri


def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATOR_KEY' not in app.config or not app.config['YANDEX_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    key = app.config['YANDEX_TRANSLATOR_KEY']
    lang = source_language
    if dest_language:
        lang = '{}-{}'.format(source_language, dest_language)
    r = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        key, text, lang
    ))
    if r.status_code != 200:
        return _('Error: the translate server failed.')
    return json.loads(r.content.decode('utf-8-sig')).get('text')
