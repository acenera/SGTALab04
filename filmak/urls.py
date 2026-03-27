from django.urls import path
from .. import htmlak
from . import views

urlpatterns = [
    path("", htmlak/erregistratu.html, name="register"),
]