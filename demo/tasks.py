import time

from celery import shared_task

from aDemo.celery import app


@app.task
def background():
    print('start')
    # with open('text.txt', 'w') as f:
    #     f.write('test\n')


@shared_task
def index_task():
    print('start')
    time.sleep(5)
    print('end')



