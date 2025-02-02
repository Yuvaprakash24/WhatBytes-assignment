from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
    password = None  # Exclude the password field from the form
    email = None 
    remove_profile_picture = forms.BooleanField(required=False, label="Remove profile picture")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'profile_picture']