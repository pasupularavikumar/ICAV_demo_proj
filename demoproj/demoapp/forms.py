from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.core.validators import RegexValidator
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from .models import *



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'