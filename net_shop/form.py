from django import forms
from .models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tên đăng nhập', malength=30)
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

