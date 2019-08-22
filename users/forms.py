from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
        email = forms.EmailField()
        phone = forms.CharField(max_length=10)

        class Meta:
                model = User
                fields = ['username', 'email', 'phone', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()
        phone = forms.CharField(max_length=10)
        bio = forms.CharField(max_length=100)

        class Meta:
                model = User
                fields = ['username', 'email', 'phone', 'bio']


class ProfileUpdateForm(forms.ModelForm):
        class Meta:
                model = Profile
                fields = ['image']
