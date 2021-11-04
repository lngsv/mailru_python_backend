# Django application server

## Prepare environment

### Activate virtual environment
```
clndr $ python3 -m venv <venv_dir_name>
clndr $ source <venv_dir_name>/bin/activate
```

### Install requirements
`(venv) clndr $ pip install -r requirements.txt`

### Run migrate (add proper database name, user and password to settings.py)
`(venv) clndr $ python manage.py migrate`

## Play with server

### Start server
`(venv) clndr $ python manage.py runserver`

### Send request
`curl -X POST 127.0.0.1:8000/events/new/ -d 'name=Halloween party' -d 'from_date=2021-10-30' -d 'to_date=2021-10-31' -d 'comment=Hooray!'` -> create new event, get id in response \
`GET http://127.0.0.1:8000/events/event/?id=0` -> see event `id` details \
`GET http://127.0.0.1:8000/events/list/` -> see all events \
`curl -X POST 127.0.0.1:8000/users/new/ -d 'name=Alan Gasiev' -d 'login=lngsv'` -> create new user, get id in response \
`GET http://127.0.0.1:8000/users/user/?id=0` -> see user `id` details \
`GET http://127.0.0.1:8000/users/list/` -> see all users

