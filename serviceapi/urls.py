from django.urls import path

from . import views
from . import films

urlpatterns = [
    path('', views.index, name='index'),
    path('films/index', films.index, name='index'),
]
