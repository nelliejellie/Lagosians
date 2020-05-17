from django import forms
from django.contrib.auth.models import User
from .models import Profile

#create a form using the forms class
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)#the widget allows html traet the password input as a type=password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')# created forms for the fields

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("password don't match")
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}
#the usereditform allows user edit their names and email as given in the fields variable

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'date_of_birth', 'photo'}
#this allows users edit the custom profile model