from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('news/', views.news, name="news"),
    path('catalog/', views.catalog, name="catalog"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('pool/', views.pool, name="pool"),
]
