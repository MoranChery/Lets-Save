import os


class Config(object):
    # Flask
    MODULE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_DIR = os.path.dirname(MODULE_DIR)
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024 * 1024 * 1024
    SECRET_KEY = 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'

    # Celery configurations
    CELERY_BROKER_URL = 'redis://localhost:9090/0'
    CELERY_RESULT_BACKEND = 'rpc://'
    CELERY_ACCEPT_CONTENT = ['json', 'npm']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'UTC'
    CELERY_ENABLE_UTC = True
    CELERY_SEND_SENT_EVENT = True

    # API
    API_PREFIX = '/api/v1'
    MESSAGES_PER_PAGE = 2
    TOPICS_PER_PAGE = 2

    # Database
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:16941694@127.0.0.1:5432/lets_improve'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
