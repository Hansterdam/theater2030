from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:resource>', views.index, name='films'),
    path('<str:resource>/<int:film_id>', views.detail, name='detail'),
    path('films/<int:film_id>/shows', views.film_shows, name='film_shows')
]
