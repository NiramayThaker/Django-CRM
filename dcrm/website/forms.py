from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']


class AddRecodForm(forms.Form):
    class Meta:
        model = Record
        fields = "__all__"
