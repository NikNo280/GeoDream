from django import forms
from .models import Places
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class PlacesForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'verified')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')