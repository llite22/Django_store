from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from .models import Comment
from .models import Blog


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    age = forms.IntegerField(label='Ваш возраст', min_value=14, max_value=120)
    email = forms.EmailField(label='Email')
    rate_site = forms.ChoiceField(label='Оцените сайт',
                                  choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                           (1, 'Очень плохо')], widget=forms.RadioSelect)
    rate_design = forms.ChoiceField(label='Оцените дизайн',
                                    choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                             (1, 'Очень плохо')], widget=forms.RadioSelect)
    rate_features = forms.MultipleChoiceField(label='Оцените возможности сайта',
                                              choices=[(1, 'Новости'), (2, 'Каталог'), (3, 'Чат')],
                                              widget=forms.CheckboxSelectMultiple)

    sites = forms.ChoiceField(label='Оцените по сравнению с другими сайтами',
                              choices=[(1, 'Лучше других'), (2, 'Как большинство'), (3, 'Хуже других')],
                              widget=forms.Select)
    feedback = forms.CharField(label='Ваш отзыв', widget=forms.Textarea)


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Пароль'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": "Комментарий"}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "description", "content", "image",)
        labels = {"title": "Заголовок", "description": "Краткое содержание", "content": "Полное содержание",
                  "image": "Картинка"}
