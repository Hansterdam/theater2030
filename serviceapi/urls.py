from django.urls import path

from . import views
from . import films

urlpatterns = [
    path('', views.index, name='index'),
    path('films', views.film_index, name='films'),
    path('films/<int:film_id>', views.film_detail, name='detail'),
]
