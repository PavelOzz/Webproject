from django.shortcuts import render
from django.http import HttpResponse
from .forms import SvyazForm
from .models import menu

def menu_home(request):
    mennu = menu.objects.all()
    return render(request, 'main/Menu.html', {'mennu':mennu})

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about-us.html')

def obratnaya_svyaz(request):
    error = ''
    if request.method == "POST":
        form = SvyazForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была не верной'

    form = SvyazForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/obratnaya-svyaz.html', data)

