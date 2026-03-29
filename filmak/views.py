from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, BozkatuForm
from .models import filmak_filma, filmak_bozkatzailea, Bozkatzailea
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def erregistratu(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            erabiltzailea = form.cleaned_data['Erabiltzailea']
            izena = form.cleaned_data['Izena']
            abizena = form.cleaned_data['Abizena']
            email = form.cleaned_data['Email']
            pasahitza = form.cleaned_data['Pasahitza']
            pasahitzaErrepikatu = form.cleaned_data['Pasahitza_Errepikatu']
            if pasahitza != pasahitzaErrepikatu:
                form.add_error('Pasahitza_Errepikatu', 'Pasahitzak ez datoz bat')
            else:
                #erregistroa egin
                try:
                    erab = User.objects.create_user(username=erabiltzailea, first_name=izena, last_name=abizena,email=email, password=pasahitza)
                    erab.save()
                    return redirect("login")
                except:
                    form.add_error('Izena', 'erabiltzalea erregistratuta dago.')
    else:
        form = RegisterForm()
    return render(request, "filmak/erregistratu.html", {'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            erabiltzailea = form.cleaned_data['Erabiltzailea']
            pasahitza = form.cleaned_data['Pasahitza']
            user = authenticate(username=erabiltzailea, password=pasahitza)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    request.session['erabiltzailea'] = erabiltzailea
                    return redirect("menu")
                else:
                    form.add_error('Erabiltzailea', 'kontua desgaituta dago')
            else:
                form.add_error('Erabiltzailea', 'Kredentzial okerrak')
    else:
        form = LoginForm()
    return render(request, "filmak/login.html", {'form':form})

@login_required(login_url='login')
def menu(request):
    return render(request, "filmak/menu.html", {'username': request.session['erabiltzailea']})

@login_required(login_url='login')
def filmenZerrenda(request):
    filma_lista = filmak_filma.objects.all()
    paginator = Paginator(filma_lista, 10)  # Show 10 films per page
    page = request.GET.get('page')
    try:
        filmak = paginator.page(page)
    except PageNotAnInteger:
        filmak = paginator.page(1)
    except EmptyPage:
        filmak = paginator.page(paginator.num_pages)

    return render(request, "filmak/FilmenZerrenda.html", {'filmak': filmak})

@login_required(login_url='login')
def filmakBozkatu(request):
    if request.method == "POST":
        form = BozkatuForm(request.POST)
        if form.is_valid():
            try:
                bozkatzailea = Bozkatzailea.objects.create(user=request.user)
            except:
                bozkatzailea = Bozkatzailea.objects.get(user=request.user)
            filmak = form.cleaned_data['filmak']
            for filma in filmak:
                filma.bozkak += 1
                filma.save()
                filmak_bozkatzailea.objects.create(erabiltzailea=bozkatzailea, filma=filma)
            return redirect('menu')
    else:
        form = BozkatuForm()
    return render(request, "filmak/filmakBozkatu.html", {'form': form})

@login_required(login_url='login')
def bozkatutakoak(request):
    if request.method == "POST":
        ezabatzekoa=request.POST.get('film')
        filma=filmak_filma.objects.get(pk=ezabatzekoa)
        filma.bozkak -=1
        filma.save()
        filmak_bozkatzailea.objects.get(erabiltzailea__user=request.user, filma=filma).delete()
        return redirect('bozkatutakoak')
    erlazioak=filmak_bozkatzailea.objects.filter(erabiltzailea__user=request.user)
    filmak=filmak_filma.objects.filter(id__in=erlazioak.values_list('filma_id', flat=True))
    return render(request, "filmak/bozkatutakoak.html", {'filmak': filmak})