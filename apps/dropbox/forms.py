__author__ = 'kevin'

from django import forms

class login(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Pasword = forms.CharField(widget=forms.PasswordInput())

class register(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Pasword = forms.CharField(widget=forms.PasswordInput())

class crear(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())