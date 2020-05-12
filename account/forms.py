from django import forms

#create a form using the forms class
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)#the widget allows html traet the password input as a type=password

    