from django.urls import path

from demo.views import index, index_slow

urlpatterns = [
    path("", index, name='index'),
    path("slow/", index_slow, name='index_slow'),
]
