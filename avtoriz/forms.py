from django import forms


class AuthForm(forms.Form):
    login = forms.CharField(label='Логин', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
