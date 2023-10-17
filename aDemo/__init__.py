from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app  # noqa


__all__ = ('celery_app', )


# install celery
# register celery in insall_apps
# set broker url
# create celery.py conf
# __ini__ register celery app
# create shared tasks to use it now


# CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_BROKER_URL = 'redis://default:vQVrxfpNxFGc3YpTaG1WnIAuEhX3bU10@redis-19662.c300.eu-central-1-1.ec2.cloud.redislabs.com:19662'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_TIMEZONE = 'Asia/Karachi'