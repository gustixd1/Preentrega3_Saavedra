from django import forms

class FormGato(forms.Form):
    nombre = forms.CharField(max_length=50)
    raza = forms.CharField(max_length=50)
    fecha_nacimiento = forms.CharField(max_length=50)
    
class FormPerro(forms.Form):
    nombre = forms.CharField(max_length=50)
    raza = forms.CharField(max_length=50)
    fecha_nacimiento = forms.CharField(max_length=50)
    
class FormMascota(forms.Form):
    nombre = forms.CharField(max_length=50)
    especie = forms.CharField(max_length=50)
    fecha_nacimiento = forms.CharField(max_length=50)

class FormBusqueda(forms.Form):
    nombre = forms.CharField(max_length=50)