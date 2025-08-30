from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormularioCrearvino(forms.Form):
    marca = forms.CharField(max_length=20)
    año = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
