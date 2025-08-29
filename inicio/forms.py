from django import forms

class FormularioCrearvino(forms.Form):
    marca = forms.CharField(max_length=20)
    año = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
