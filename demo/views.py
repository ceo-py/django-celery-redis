import time

from django.http import HttpResponse
from demo.tasks import index_task


# Create your views here.
def index(request):
    start = time.time()
    for _ in range(40):
        index_task.delay()

    end = time.time()

    return HttpResponse(f'Fast Execute in {end - start}')


def index_slow(request):
    start = time.time()
    index_task()
    end = time.time()

    return HttpResponse(f'Slow Execute in {end - start}')
