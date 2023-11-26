from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=1,widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre"}))
    precio = forms.IntegerField(min_value=1,required=False)
    descripcion = forms.CharField(max_length=250,widget=forms.Textarea(attrs={"rows":4}), required=False)
    agregados = forms.CharField(max_length=150, required=False)
    precio_agregados = forms.IntegerField(min_value=1,required=False)

    class Meta:
        model = Producto
        fields = '__all__'


class Contacto(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]