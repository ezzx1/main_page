from django.urls import path
from . import views

urlpatterns = [
    path('', views.app,name='home'),
    path('login', views.login,name='login'),
    path('sign up', views.sign_up,name='sign_up'),
]
