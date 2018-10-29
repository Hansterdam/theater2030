from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('<str:resource>', views.index),
    path('<str:resource>/<int:item_id>', views.detail),
    path('films/<int:film_id>/shows', views.film_shows),
    path('shows/<int:show_id>/seats', views.show_seats),
    path('check_in/<int:ticket_id>', views.check_in),
]
