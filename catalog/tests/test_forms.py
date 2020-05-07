from django.test import TestCase
from catalog.forms import *

class TestForm(TestCase):

    def test_registration(self):
        form_data = {'mail': 'Default@gmail.com', 'username': 'Default', 'password': 'Default',
                     'password_repeat': 'Default'}
        form = CustomUserCreationForm(data=form_data)
        assert form.user_return()
        assert form.correct_password()
        form_data = {'mail': 'Default@gmail.com', 'username': 'Default', 'password': 'Default',
                     'password_repeat': 'Default'}
        form = CustomUserCreationForm(data=form_data)
        assert form.error_value()[1] == "Данная почта уже сужествует"
        form_data = {'mail': 'NoneDefault@gmail.com', 'username': 'Default', 'password': 'Default',
                     'password_repeat': 'Default'}
        form = CustomUserCreationForm(data=form_data)
        assert form.error_value()[1] == "Данное имя уже сужествует"
        form_data = {'mail': 'NoneDefault@gmail.com', 'username': 'NoneDefault', 'password': 'NoneDefault',
                     'password_repeat': 'Default'}
        form = CustomUserCreationForm(data=form_data)
        assert form.error_value()[1] == "Пароли не совпадают"

    def test_changepassword(self):
        form_data = {'old_password': 'Default', 'password': 'Default',
                     'password_repeat': 'Default'}
        form = CustomUserChangeForm(data=form_data)
        assert form.correct_password()
        form_data = {'old_password': 'Default', 'password': 'Default',
                     'password_repeat': 'default'}
        form = CustomUserChangeForm(data=form_data)
        assert not form.correct_password()