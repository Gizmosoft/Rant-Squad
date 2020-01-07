from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:                             #information about your class.
        model = User                        #Every entries goes into the same table
        fields = ['name','username','email','password']
