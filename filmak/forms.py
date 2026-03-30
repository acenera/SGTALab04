from django import forms
from .models import filmak_filma


class RegisterForm(forms.Form):
    Erabiltzailea = forms.CharField(max_length=30, required=True)
    Izena = forms.CharField(max_length=30, required=True)
    Abizena = forms.CharField(max_length=30, required=True)
    Email = forms.EmailField(max_length=75, required=True)
    Pasahitza = forms.CharField(max_length=128, widget=forms.PasswordInput, required=True)
    Pasahitza_Errepikatu = forms.CharField(max_length=128, widget=forms.PasswordInput, required=True)

class LoginForm(forms.Form):
    Erabiltzailea = forms.CharField(max_length=30, required=True)
    Pasahitza = forms.CharField(max_length=128, widget=forms.PasswordInput, required=True)

class BozkatuForm(forms.Form):
    filmak = forms.ModelMultipleChoiceField(
        queryset=filmak_filma.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
class ZaleakForm(forms.Form):
    filmak = forms.ModelMultipleChoiceField(queryset=filmak_filma.objects.all(),
        widget=forms.ModelMultipleChoiceField,
        required=True)