from django.contrib import admin
from django.contrib.auth.models import Group, User


# Register your models here.
from gestionarchivo.models import registroarchivos

class registroarchivoAdmin(admin.ModelAdmin):
    list_display=("fechaingreso","guianro","usuario","descripcion","oficio","fechaentrega","enviadoa","observacion")
    search_fields=("fechaingreso", "guianro", "usuario") 
    list_filter=("fechaingreso",)
    date_hierarchy="fechaingreso"   

admin.site.site_header = 'Municipio de Loja 2020' 
admin.site.register(registroarchivos, registroarchivoAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
