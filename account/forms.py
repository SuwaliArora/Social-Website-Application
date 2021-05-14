from django import forms
from django.forms import fields
from django.contrib.auth.models import User

#login form
#this form willbe used to authenticate users against databse
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    #passwordInput widget to render its html input element
    
#sign up form to allow user registration on website
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        #to check if the both passwords are same or not
        if cd['password'] != cd['password2'] :
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
