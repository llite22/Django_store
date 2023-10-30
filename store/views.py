from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.

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


def login(request):
    context = {}
    return render(request, 'store/login.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)

def pool(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'store/pool.html', {'data': data})
    else:
        form = FeedbackForm()
    return render(request, 'store/pool.html', {'form': form})


