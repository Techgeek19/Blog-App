from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect

class registerform(forms.ModelForm):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Enter Username'}), 
        required= True, max_length=50) 
    email= forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control','placeholder': 'Enter Email'}),   
        required= True, max_length=50)
    first_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Enter First Name'}),
        required= True, max_length=50)
    last_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Enter Last Name'}),
        required= True, max_length=50)
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'Enter Password'}),
        required= True, max_length=50)

    class Meta():
        model= User
        fields= ['username', 'email','first_name', 'last_name', 'password']    

class loginform(forms.Form):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Enter Username'}), 
        required= True, max_length=50) 
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'Enter Password'}),
        required= True, max_length=150)

class postform(forms.ModelForm):

    class Meta:
        model= Post
        fields= ['title', 'slug','author', 'content', 'status']  
