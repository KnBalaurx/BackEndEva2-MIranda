from django import forms
from clienteApp.models import Cliente

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'