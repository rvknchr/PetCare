from django.urls import path
from . import views


urlpatterns = [
    path('/', views.index, name='index'),
    path('/donate/', views.donate, name='donate'),
    path('/chatbot/', views.chatbot, name='chatbot'),
    path('/login/', views.login, name='login'),
    path('/registration/', views.registration, name='registration'),
    path('/logout/', views.logout, name='logout'),
]