from django.contrib.auth.forms import UserCreationForm
from .models import Users

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ("username", "email")