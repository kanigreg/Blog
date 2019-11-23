# Микроблог
### О проете

Этот проект создан с целью изучения back-end разработки.
Туториал вы можете найти в [этом блоге](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Вы также можете [посмотреть](https://kangry-microblog.herokuapp.com/) проект в дейтсвии. 

### Что реализованно?

* Регистрация, аутентификация пользователей
* Профиль пользователя
* Система подписок
* Смена пароля с помощью почтового оповещения
* Локализация (`ru`, `en`)
* Полнотекстовый поиск


### Установка

В корневом каталоге:
```shell script
virtualenv venv
source venv/bin/activate
pip install -r requarements.txt
```

### Настройка

В корневом каталоге создайте файл `.env` для переменных окружения. Пример:
```dotenv
SECRET_KEY=<Ваш серетный ключ>

# Элекронная почта
MAIL_SERVER=smtp.googlemail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=<имя пользователя почты>
MAIL_PASSWORD=<пароль почты>

# Сервис перевода текста
YANDEX_TRANSLATOR_KEY=<API ключ яндекса>

# Движок полнотекстового поиска
ELASTICSEARCH_URL=<URL Elasticsearch>

# Опционально
ELASTICSEARCH_USERNAME=<Логин Elasticsearch>
ELASTICSEARCH_PASSWORD=<Пароль Elasticsearch>
```

### Запуск

```shell script
export FLASK_APP=microblog.py
flask run
```
