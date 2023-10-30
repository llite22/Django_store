from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Email')
    rate_site = forms.ChoiceField(label='Оцените сайт',
                                  choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                           (1, 'Очень плохо')], widget=forms.RadioSelect)
    rate_content = forms.ChoiceField(label='Оцените контент',
                                     choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                              (1, 'Очень плохо')], widget=forms.RadioSelect)
    rate_design = forms.ChoiceField(label='Оцените дизайн',
                                    choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                             (1, 'Очень плохо')], widget=forms.RadioSelect)
    rate_features = forms.MultipleChoiceField(label='Оцените возможности сайта',
                                              choices=[(1, 'Новости'), (2, 'Форум'), (3, 'Чат')],
                                              widget=forms.CheckboxSelectMultiple)

    sites = forms.ChoiceField(label='Оцените по сравнению с другими сайтами',
                              choices=[(1, 'Лучше других'), (2, 'Как большинство'), (3, 'Хуже других')],
                              widget=forms.Select)
    feedback = forms.CharField(label='Ваш отзыв', widget=forms.Textarea)
