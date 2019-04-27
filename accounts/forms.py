from django import forms


class UserLoginForm(forms.Form):
    """login users form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
