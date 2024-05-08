# forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser  # Importing CustomUser model from models.py


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
