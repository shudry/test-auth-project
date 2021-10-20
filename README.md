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
query{
  users{
    isSuperuser
    username
    firstName
    lastName
    email
    isStaff
    dateJoined
    password
  }
}
```

```json
{
  "data": {
    "users": [
      {
        "isSuperuser": false,
        "username": "0d62dd93-5a06-4559-9f57-49ede0ae697d",
        "firstName": "User Name",
        "lastName": "",
        "email": "test@gmail.com",
        "isStaff": false,
        "dateJoined": "2021-10-20T06:54:16.543951+00:00",
        "password": "pbkdf2_sha256$260000$FcX5uk8QTGbxIAdSK32V6T$C8bRLp6o8AoRlceWeWi/Cr8lWkoYtVrPvT1jkHaS7sE="
      },
      ...
    ]
  }
}
```

## Регистрация

##### Коды ошибок **`errorCode`**
* Если почта указанна не корректно, выводится ошибка **`invalid_email`**
* Пользователь уже существует - **`user-already-exist`**
* Не валидная длина пароля (от 8 до 24) - **`invalid_password`**


```graphql
// Create new user
mutation{
    registration(email: "test@gmail.com", name: "TestName", password: "testpassword"){
        success
        errorCode
        user {
            isSuperuser
            username
            firstName
            lastName
            email
            isStaff
            dateJoined
            password
        }
    }
}
```

```json
// Результат выполнения запроса registration (успешный)
{
  "data": {
    "registration": {
      "user": {
        "isSuperuser": false,
        "username": "2f5df6b6-57a4-40be-bee0-abf2ec18fa83",
        "firstName": "TestName",
        "lastName": "",
        "email": "test@gmail.com",
        "isStaff": false,
        "dateJoined": "2021-10-20T06:57:08.784855+00:00",
        "password": "pbkdf2_sha256$260000$FcX5uk8QTGbxIAdSK32V6T$C8bRLp6o8AoRlceWeWi/Cr8lWkoYtVrPvT1jkHaS7sE="
      },
      "success": true,
      "errorCode": null
    }
  }
}
```

```json
// Результат выполнения запроса registration (неуспешный)
{
  "data": {
    "registration": {
      "user": null,
      "success": false,
      "errorCode": "user-already-exist"
    }
  }
}
```

\* Поле `password` добавлено для того, что-бы увидеть в каком виде сохраняется пароль в базе. Для `production` поле удаляется.

### Аутентификация
```graphql
mutation{
    login(email: "test@gmail.com", password: "testpassword"){
        payload
        refreshExpiresIn
        token
    }
}
```

```json
{
  "data": {
    "login": {
      "payload": {
        "email": "test@gmail.com",
        "exp": 1634716289,
        "origIat": 1634715089
      },
      "refreshExpiresIn": 1635319889,
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNodW1pbG8uZG15dHJ5QGdtYWlsLmNvbSIsImV4cCI6MTYzNDcxNjI4OSwib3JpZ0lhdCI6MTYzNDcxNTA4OX0.INfxznujYN0T3xAGLnMg6S2Lfmb-fUPqW_HTl38RdKc"
    }
  }
}
```
