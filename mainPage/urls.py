from django.conf.urls import url
from mainPage import views
from django.urls import path
 
urlpatterns = [
    path("login", views.login, name="login"),
]