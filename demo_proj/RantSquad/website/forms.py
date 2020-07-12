# from django.contrib.auth.models import User
from django import forms
# from .models import Profile
#
# class RegisterForm(forms.ModelForm):
#     # name        = forms.CharField(max_length=40, required=True, help_text='Required')
#     username    = forms.CharField(max_length=20, required=True, help_text='Required')
#     # email       = forms.EmailField(max_length=254, help_text='Required')
#     password    = forms.CharField(widget=forms.PasswordInput, help_text='Required')
#     bio         = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols':50}))
#
#     class Meta:                             #information about your class.
#         model = Profile                       #Every entries goes into the same table
#         fields = ['username','bio','password']
#
# class LoginForm(forms.ModelForm):
#     username    = forms.CharField(max_length=20, required=True, help_text='Required')
#     password    = forms.CharField(help_text='Required', widget=forms.PasswordInput)
#
#     class Meta:                             #information about your class.
#         model = Profile                       #Every entries goes into the same table
#         fields = ['username','password']
