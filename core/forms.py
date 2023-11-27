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





class MunicipalidadForm(forms.ModelForm):
    class Meta:
        model = Municipalidad
        fields = '__all__'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'

class AdultoMayorForm(forms.ModelForm):
    class Meta:
        model = adulto_mayor
        fields = '__all__'

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

class MaterialesForm(forms.ModelForm):
    class Meta:
        model = Materiales
        fields = '__all__'

class TalleresForm(forms.ModelForm):
    class Meta:
        model = Talleres
        fields = '__all__'

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class BonoForm(forms.ModelForm):
    class Meta:
        model = Bono
        fields = '__all__'



class PostulacionTallerForm(forms.ModelForm):
    class Meta:
        model = postulacion_taller
        fields = '__all__'

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        # Añade el atributo 'type' y la clase 'datepicker' para especificar que son campos de fecha
        self.fields['fecha_inicio'].widget.attrs['type'] = 'text'
        self.fields['fecha_inicio'].widget.attrs['class'] = 'datepicker'
        self.fields['fecha_termino'].widget.attrs['type'] = 'text'
        self.fields['fecha_termino'].widget.attrs['class'] = 'datepicker'






class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class PostulacionInstructorForm(forms.ModelForm):
    class Meta:
        model = postulacion_instructor
        fields = '__all__'

class CredencialesForm(forms.ModelForm):
    class Meta:
        model = Credencial
        fields = '__all__'        