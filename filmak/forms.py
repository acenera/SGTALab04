from django import forms
from .models import filmak_filma
from django.utils.translation import gettext_lazy as _


class RegisterForm(forms.Form):
    Erabiltzailea = forms.CharField(max_length=30, required=True, label=_("Erabiltzailea"))
    Izena = forms.CharField(max_length=30, required=True, label=_("Izena"))
    Abizena = forms.CharField(max_length=30, required=True, label=_("Abizena"))
    Email = forms.EmailField(max_length=75, required=True, label=_("Email"))
    Pasahitza = forms.CharField(max_length=128, widget=forms.PasswordInput, required=True, label=_("Pasahitza"))
    Pasahitza_Errepikatu = forms.CharField(max_length=128, widget=forms.PasswordInput, required=True, label=_("Pasahitza Errepikatu"))

class LoginForm(forms.Form):
    Erabiltzailea = forms.CharField(max_length=30, required=True, label=_("Erabiltzailea"))
    Pasahitza = forms.CharField(max_length=128, widget=forms.PasswordInput, required=True, label=_("Pasahitza"))

class BozkatuForm(forms.Form):
    filmak = forms.ModelMultipleChoiceField(
        queryset=filmak_filma.objects.all(),
        required=True
    )
class ZaleakForm(forms.Form):
    filmak = forms.ModelChoiceField(
        queryset=filmak_filma.objects.all(),
        required=True
    )