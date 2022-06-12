from django import forms
from django.forms import ModelForm,TextInput,Textarea
from .models import svyaz

class SvyazForm(ModelForm):
   class Meta:
       model = svyaz
       fields = ['name','phone_number','email','message']
       widgets ={
           "name":TextInput(attrs={
               'class':'form-control',
               'placeholder':'Имя'
           }),
           "phone_number": TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Номер телефона'
           }),
           "email": TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Email'
           }),
           "message": Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Введите ваше сообщение'
           }),
        }