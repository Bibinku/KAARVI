from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('roomspage/', views.roomspage, name="roomspage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('savehomecontact/', views.savehomecontact, name="savehomecontact"),
    path('singleroom/<int:Rid>/', views.singleroom, name="singleroom"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('ourservices/', views.ourservices, name="ourservices"),
]
