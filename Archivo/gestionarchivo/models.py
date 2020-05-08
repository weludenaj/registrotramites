from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class registroarchivos(models.Model):
    fechaingreso=models.DateField(null=False, blank=False, verbose_name="Fecha")
    guianro=models.CharField(max_length=20, verbose_name="Tramite Nro", null=False, blank=False, unique=False)
    usuario=models.CharField(max_length=200, verbose_name="Usuario", null=False, blank=False)
    descripcion=models.TextField(max_length=500, verbose_name="Descripcion", null=False, blank=False)
    oficio=models.CharField(max_length=50, verbose_name="Numero Oficio", null=True, blank=True)
    fechaentrega=models.DateField(null=True, verbose_name="Fecha Entrega")
    enviadoa=models.TextField(null=True, blank=True,max_length=250, verbose_name="Enviado a")
    observacion=RichTextField(null=True, blank=True,max_length=500, verbose_name="Observacion")
    atendido=models.BooleanField('Atendido', default=False)
    documentos=models.FileField(upload_to='media', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Tramite'
        verbose_name_plural = 'Tramites Externos'
        ordering = ['-fechaingreso']
      ##  unique_together =('fechaingreso', 'guianro')
    def __str__(self):
        return 'Fecha %s Guia %s Usuario %s Descripcion %s Oficio %s Entregado %s Enviado a %s Observacion %s Atendido %s' % (self.fechaingreso,self.guianro, self.usuario, self.descripcion, self.oficio, self.fechaingreso, self.enviadoa, self.observacion, self.atendido )