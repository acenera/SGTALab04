from django.urls import path
from . import templates
from . import views

urlpatterns = [
    path("erregistratu", views.erregistratu, name="erregistratu"),
    path("login", views.login, name="login"),
    path("", views.login, name="login"),
    path("menu", views.menu, name="menu"),
    path("filmen_zerrenda", views.filmenZerrenda, name="filmenZerrenda"),
    path("bozkatu", views.filmakBozkatu, name="filmakBozkatu"),
    path("bozkatutakoak", views.bozkatutakoak, name="bozkatutakoak")
]