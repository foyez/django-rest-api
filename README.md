# django-rest-api

## Docker Commands

```bash
$ docker build .
$ docker-compose build
$ docker-compose run app sh -c "django-admin.py startproject app ." # docker-compose run <service-name> commands
$ docker-compose run --rm app sh -c "python manage.py startapp core"
$ docker-compose run --rm app sh -c "python manage.py test"
$ docker-compose run --rm app sh -c "python manage.py makemigrations core"
$ docker-compose up
```