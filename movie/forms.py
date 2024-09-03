from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Filme

from django.forms.widgets import PasswordInput, TextInput

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        exclude = ['slug']
        labels = {
            "titulo":"Tilulo"
        }

class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())