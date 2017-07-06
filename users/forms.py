from django import forms

class LoginForm(forms.Form):
    default_attributes = {
        'class': 'form-control'
    }

    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs=default_attributes), )
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=default_attributes), )
