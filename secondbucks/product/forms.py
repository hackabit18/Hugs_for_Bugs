from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import State,UserDetails, Product

class UserSignupForm(forms.ModelForm):
    email = forms.CharField(required=True)
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model=UserDetails
        fields=['state','phone','img']


class SellProductRegistrationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name', 'category', 'state', 'descripton', 'price', 'img']
    
class ShareProductRegistrationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name', 'category', 'state', 'descripton', 'day_of_return', 'img']