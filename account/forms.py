from django import forms

#login form
#this form willbe used to authenticate users against databse
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    #passwordInput widget to render its html input element