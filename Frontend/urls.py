from django.urls import path
from Frontend import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('roomspage/', views.roomspage, name='roomspage'),
]
