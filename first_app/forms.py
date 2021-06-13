
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerForm (UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class testview (forms.Form):
    email = forms.EmailField()
