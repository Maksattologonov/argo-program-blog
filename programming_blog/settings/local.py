import environ
env = environ.Env()


SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='not secret)')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

DATABASES = {
    'default': env.db(
        'DATABASE_URL', default='psql://myprojectuser:password@localhost:5432/postgres'
    )
}

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])
