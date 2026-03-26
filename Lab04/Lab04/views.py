from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect

def nire_bista(request):
    if request.method == 'POST':
        erabiltzailea = request.POST.get('username')
        pasahitza = request.POST.get('password')
        user = authenticate(username=erabiltzailea, password=pasahitza)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Berbideratu erabiltzailea hurrengo orrira
            else:
                # Erakutsi errorea: kontua desgaituta dago
        else:
            # Erakutsi errorea: kredentzial okerrak


def logout_bista(request):
    logout(request)
    return redirect("")