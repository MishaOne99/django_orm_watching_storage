# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников вашего банка.

## Как установить

Python3.12 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```

## Настройка

В каталоге ``` project ```, создайте файл ``` .env ```. В нём добавляете следующие константы:

DB_ENGINE = ['Django Engine'](https://docs.djangoproject.com/en/5.0/ref/settings/#engine)

DB_HOST = [Django Host](https://docs.djangoproject.com/en/5.0/ref/settings/#host)

DB_PORT = [Django Port](https://docs.djangoproject.com/en/5.0/ref/settings/#port)

DB_NAME = [Django Name](https://docs.djangoproject.com/en/5.0/ref/settings/#name)

DB_USER = [Django User](https://docs.djangoproject.com/en/5.0/ref/settings/#user)

DB_PASSWORD = [Django Password](https://docs.djangoproject.com/en/5.0/ref/settings/#password)

SECRET_KEY = [Django Secret Key](https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key)

DEBUG = [Django Debug](https://docs.djangoproject.com/en/5.0/ref/settings/#debug)

ALLOWED_HOSTS = [Django Allowed Hosts](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Как запустить 

В командной строке введите команду:

```python
python manage.py runserver
```