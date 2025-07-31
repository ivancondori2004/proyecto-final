from django import forms

class FormularioContacto(forms.Form):
    
    nombre = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(attrs={'class': 'controls'})
    )

    email = forms.CharField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'controls'})
    )

    contenido = forms.CharField(
        label="Contenido",
        required=True,
        widget=forms.Textarea(attrs={'class': 'controls'})
    )
