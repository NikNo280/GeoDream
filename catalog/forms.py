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

    def correct_password(self):
        password_value = self.data["password"]
        password_repeat = self.data["password_repeat"]
        if password_repeat == password_value:
            return True
        return False

    def error_value(self):
        user_value = self.data["username"]
        mail = self.data["mail"]
        if CustomUser.objects.filter(email__iexact=mail).exists():
            return "error_mail", "Данная почта уже сужествует"
        if CustomUser.objects.filter(username__iexact=user_value).exists():
            return "error_name", "Данное имя уже сужествует"
        if not self.correct_password():
            return "error_password", "Пароли не совпадают"

    def user_return(self):
        return CustomUser.objects.create_user(username=self.data["username"], email=self.data["mail"],
                                              password=self.data["password"])


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def correct_password(self):
        password_value = self.data["password"]
        password_repeat_value = self.data["password_repeat"]
        if password_value == password_repeat_value:
            return True
        return False
