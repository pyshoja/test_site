
from django import forms
from account.models import User
from django.contrib.auth.forms import UserCreationForm

class registerForm (UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class testview (forms.Form):
    email = forms.EmailField()
