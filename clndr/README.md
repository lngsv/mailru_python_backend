# Django application server

## Prepare environment

### Activate virtual environment
```
clndr $ python3 -m venv <venv_dir_name>
clndr $ source <venv_dir_name>/bin/activate
```

### Install requirements
`(venv) clndr $ pip install -r requirements.txt`

### Start postgres
* (For MacOS): `brew services start postgres`
* create `clndr` database
* create `local_settings.py` file with `PG_USER=<Postgres username>` and `PG_PASSWORD=<Postgres password>` in it

### Run migrate (add proper database name, user and password to settings.py)
`(venv) clndr $ python manage.py migrate`

## Play with server

### Start server
`(venv) clndr $ python manage.py runserver`

### Use admin
* Create superuser `(venv) clndr $ python manage.py createsuperuser`
* Go to `127.0.0.1:8000/admin/`

### Or send http requests
`curl -X POST 127.0.0.1:8000/users/new/ -d 'name=Alan Gasiev' -d 'login=lngsv'` -> create new user, get id in response \
`GET http://127.0.0.1:8000/users/user/<id>` -> see user `id` details \
`GET http://127.0.0.1:8000/users/list/` -> see all users
`curl -X POST 127.0.0.1:8000/events/new/ -d 'name=Halloween party' -d 'from_date=2021-10-30 13:58' -d 'to_date=2021-10-31 12:44' -d 'comment=Hooray!' -d 'creator_id=<existing user id>'` -> create new event, get id in response \
`GET http://127.0.0.1:8000/events/event/<id>` -> see event `id` details \
`GET http://127.0.0.1:8000/events/list/` -> see all events \
`curl -X POST 127.0.0.1:8000/events/update/<id>` -d 'comment=New comment'` -> update event `id` \
`curl -X POST 127.0.0.1:8000/events/delete/<id>` -> delete event `id` \

