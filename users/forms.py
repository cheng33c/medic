from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ("username", "email")