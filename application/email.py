from flask_mail import Message
from application import mail
from flask import current_app
from threading import Thread


def send_async_email(app, mes):
    # Контекст приложения необходим, чтобы предоставить доступ к кофигурациям, при отправке письма.
    with app.app_context():
        mail.send(mes)


def send_email(subject, sender, recipients, text_body, html_body):
    mes = Message(subject, sender=sender, recipients=recipients)
    mes.body = text_body
    mes.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), mes)).start()

