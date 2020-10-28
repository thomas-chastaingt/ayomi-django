from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#custom register form with differents fields
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


#custom edit profil with only email
class EditForm(UserChangeForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["email"]

