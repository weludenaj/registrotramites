from django import forms

class RegistroForm(forms.Form):
    fechaingreso=forms.DateField()
    guianro=forms.CharField(max_length=20)
    usuario=forms.CharField(max_length=200)
    descripcion=forms.CharField(max_length=500)
    oficio=forms.CharField(max_length=50)
    fechaentrega=forms.DateField()
    enviadoa=forms.CharField(max_length=250)
    observacion=forms.CharField(max_length=500)

     