import os
from datetime import timedelta

WEATHER_API_KEY = 'bf622f5098b641e1bff92907231110'
WEATHER_DEFAULT_CITY = 'Moscow, Russia'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'data.db')
SECRET_KEY = 'wlqklaLKADKWj29u31'
REMEMBER_COOKIE_DURATION = timedelta(days=30)
