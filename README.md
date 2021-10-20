# Back-end для регистрации и аутентификации.


## Установка
```bash
# Установка виртуальной среды и python зависимостей
virtualenv -p python3 --no-site-packages .virtual
source .virtual/bin/activate && cd application
pip3 install -r requirements.txt
```

Выполнение миграций после установки всех зависимостей:
```bash
python3 manage.py migrate
```

Запуск development сервера **(127.0.0.1:9401)**
```bash
python3 manage.py runserver 9401
```


## GraphQL API

### Список пользователей
```graphql

```
### Регистрация
```graphql

```
### Аутентификация
```graphql

```
