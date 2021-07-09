from celery import Celery
from flask import Flask

def configure_celery(app: Flask):

    celery = Celery(__name__, include=['celery_tasks.worker_tasks'])

    """Configures celery_tasks instance from app, using it's config"""
    TaskBase = celery.Task

    class ContextTask(TaskBase):  # pylint: disable=too-few-public-methods
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)


    # https://docs.celeryproject.org/en/stable/userguide/configuration.html
    celery.conf.update(
        broker_url=app.config['CELERY_BROKER_URL'],
        timezone=app.config['CELERY_TIMEZONE'],
        result_backend=app.config['CELERY_RESULT_BACKEND'],
        accept_content=app.config['CELERY_ACCEPT_CONTENT'],
        task_serializer=app.config['CELERY_TASK_SERIALIZER'],
        result_serializer=app.config['CELERY_TASK_SERIALIZER'],
        worker_hijack_root_logger=False,
        # beat_schedule=app.config['CELERYBEAT_SCHEDULE'],  # app.config.get('CELERYBEAT_SCHEDULE', {}),
        worker_redirect_stdouts_level='ERROR',
        task_always_eager=app.config.get('CELERY_ALWAYS_EAGER', False),
    )
    celery.Task = ContextTask
    return celery
