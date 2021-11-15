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
`curl http://127.0.0.1:8000/users/ -d 'name=Alan Gasiev' -d 'username=lngsv'` -> create new user \
`curl http://127.0.0.1:8000/users/<id>/` -> see user `id` details \
`curl http://127.0.0.1:8000/users/` -> see all users \
`curl http://127.0.0.1:8000/users/<id>/ -X PATCH -d 'bio=About myself'` -> partial update user \
`curl http://127.0.0.1:8000/users/<id>/ -X PUT ...` -> update user (all fields required) \
`curl http://127.0.0.1:8000/events/ -d 'name=Halloween party' -d 'from_date=2021-10-30 13:58' -d 'to_date=2021-10-31 12:44' -d 'comment=Hooray!' -d 'creator_id=<existing user id>'` -> create new event \
`curl http://127.0.0.1:8000/events/<id>/` -> see event `id` details \
`curl http://127.0.0.1:8000/events/` -> see all events \
`curl http://127.0.0.1:8000/events/<id>/ -d 'comment=New comment' -X PATCH` -> update event `id` \
`curl http://127.0.0.1:8000/events/<id>/ -X DELETE` -> delete event `id` \
`curl http://127.0.0.1:8000/events/<id>/ -d 'from_date=1999-11-12 14:45' -d 'to_date=1998-11-12 14:45' -X PATCH` -> trigger validation error (`from_date` > `to_date`) \


