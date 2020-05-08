from django import  forms
from .models import registroarchivos
class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = registroarchivos
        fields = (
            'fechaingreso',
            'guianro',
            'usuario', 
            'descripcion', 
            'oficio', 
            'fechaentrega',
            'enviadoa',
            'observacion',
            'atendido',
        )
        widgets = {
            #'fechaingreso': forms.DateInput(format='%d/%m/%Y'),
            'usuario': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese Usuario'
                }
            ),
        }

    def clean_fecha(self):
        fecha = self.clean_data['fechaingreso']
        if fecha > datenow():
            raise forms.ValidationError('Fecha Incorrecta')
        return fecha