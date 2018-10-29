from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:resource>', views.index, name='films'),
    path('<str:resource>/<int:item_id>', views.detail, name='detail'),
    path('films/<int:film_id>/shows', views.film_shows, name='film_shows'),
    path('shows/<int:show_id>/seats', views.show_seats, name='show_seats'),
    path('check_in/<int:ticket_id>', views.check_in, name='check_in'),
]
