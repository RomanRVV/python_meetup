# Сервис PythonMeetup

Бот созданный для комфортного проведения конференций. 
Дает возможность через него задать вопрос докладчику, посмотреть адресованные Вам вопросы, узнать план мероприятия и менять время проведения докладов.


### Содержание

- [Как установить](#как-установить)
- [Как запустить](#как-запустить)
- [Как пользоваться ботом](#как-пользоваться-ботом)
- [Как пользоваться административной панелью](#как-пользоваться-административной-панелью)


### Как установить
Для запуска вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте файл **.env** вида:
```properties
TG_TOKEN=YOUR_TG_TOKEN
```
Токен для Телеграм бота вы можете получить https://telegram.me/BotFather

Создайте базу данных:

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
Создайте суперпользователя
```sh
python3 manage.py createsuperuser
```


### Как запустить
Для запуска бота используйте команду
```sh
python manage.py runbot
```

Для запуска административной панели используйте команду
```sh
python manage.py runserver
```

### Как пользоваться ботом

Вводим команду `/start` и открывается меню 

Если вы являетесь организатором ваше меню выглядит следующим образом

<img width="551" alt="Меню организатора" src="https://github.com/RomanRVV/python_meetup/assets/129319859/8b759275-2814-4625-9b27-d86816ce0ac7">

- `План мероприятия` - есть возможность посмотреть информацию о предыдущем, текущем и следующем докладе, 
задать вопрос спикеру по выбранному докладу, а также посмотреть всю программу конференции
- `Перенос доклада` – сдвигает следующий доклад на определенное время вперед


Меню спикера 

<img width="545" alt="Меню спикера" src="https://github.com/RomanRVV/python_meetup/assets/129319859/c26efbef-0c1b-4230-b59f-1bbcbf7c6b81">

- `Посмотреть вопросы` – можно посмотреть адресованные Вам вопросы, также будет указан никнейм спросившего
- `План мероприятия` - такая же кнопка как у организатора и участника
- `О боте` - описание бота


Меню участника

<img width="544" alt="Меню участника" src="https://github.com/RomanRVV/python_meetup/assets/129319859/a3cd6191-4627-4f8d-93d1-507f44d5552c">

- `План мероприятия` - такая же кнопка как у организатора и спикера
- `О боте` - описание бота


### Как пользоваться административной панелью

Для входа в админ-панель откройте ссылку /admin (например http://127.0.0.1:8000/admin) и введите логин и пароль суперпользователя

`Вопросы`

<img width="640" alt="вопросы" src="https://github.com/RomanRVV/python_meetup/assets/129319859/20ed4d25-01d8-42ab-ab0c-817de64ee4fa">


В этой вкладке отображаются все заданные вопросы с указанием задавшего вопрос и отвечающего.

Можно добавить вопрос нажав `ADD ВОПРОС`

`Доклады`

<img width="634" alt="доклады" src="https://github.com/RomanRVV/python_meetup/assets/129319859/6b4f8810-bf71-42cb-9f0e-9019070ab2a2">


В этой вкладке отображаются доклады с указанием докладчика, временем начала и конца доклада.

Можно добавить доклад нажав `ADD ДОКЛАД`

`Мероприятия` 

<img width="656" alt="Мероприятия" src="https://github.com/RomanRVV/python_meetup/assets/129319859/892edee0-386b-4eef-a665-cde7e1e5817e">


В этой вкладке отображаются мероприятия с указанием даты, место проведения, программой мероприятия, также со списком спикеров.

Можно добавить мероприятие нажав `ADD МЕРОПРИЯТИЕ`

`Участники`

<img width="674" alt="участники" src="https://github.com/RomanRVV/python_meetup/assets/129319859/2a5f5284-b3e0-4660-96cf-4f9714a3f3a2">


В этой вкладке отображаются участники мероприятия с указанием их никнейма и id телеграмм чата.

Можно добавить участника нажав `ADD УЧАСТНИК`. При добавлении можно указать его роль(докладчик или организатор),
в зависимости от выбранной роли поменяется меню в боте(см. Как пользоваться ботом)
