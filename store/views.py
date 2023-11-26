from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth import authenticate, login
def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def news(request):
    context = {}
    return render(request, 'store/news.html', context)


def catalog(request):
    context = {}
    return render(request, 'store/catalog.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def resurs(request):
    context = {}
    return render(request, 'store/resurs.html', context)


def pool(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'store/pool.html', {'data': data})
    else:
        form = FeedbackForm()
    return render(request, 'store/pool.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('login')
    else:
        regform = UserCreationForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'store/registration.html', {'regform': regform, 'year': datetime.now().year, }
    )

