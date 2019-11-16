from flask_mail import Message
from application import mail
from application import app
from flask import render_template
from threading import Thread


def send_async_email(app, mes):
    # Контекст приложения необходим, чтобы предоставить доступ к кофигурациям, при отправке письма.
    with app.app_context():
        mail.send(mes)


def send_email(subject, sender, recipients, text_body, html_body):
    mes = Message(subject, sender=sender, recipients=recipients)
    mes.body = text_body
    mes.html = html_body
    Thread(target=send_async_email, args=(app, mes)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user, token=token),
               html_body=render_template('email/reset_password.html', user=user, token=token))
