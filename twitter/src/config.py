import os


dsn = {
    "dbname": os.environ.get('POSTGRES_DB'),
    "host": os.environ.get('POSTGRES_HOST'),
    "post": os.environ.get('POSTGRES_POST'),
    "user": os.environ.get('POSTGRES_USER'),
    "password": os.environ.get('POSTGRES_PASSWORD')
}