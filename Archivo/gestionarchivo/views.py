import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.views.generic.edit import FormView
from django.db.models import Q 
from gestionarchivo.models import registroarchivos
from .forms2 import PruebaForm
from .forms import RegistroForm
# import models
#from datetime import datetime

# Create your views here.

def busqueda_archivos(request):
    return render(request, "busqueda_archivos.html")

def busqueda_archivosf(request):
    return render(request, "busqueda_archivosf.html")

def buscar(request):
    if request.POST["prd"]:
        archivo=request.POST["prd"]
        if len(archivo) > 25:
            mensaje="Texto de búsqueda demasiado largo"
        else:
            registro=registroarchivos.objects.filter(usuario__icontains=archivo)
            return render(request, "resultado_busqueda.html", {"registro":registro, "query":archivo})
        #   mensaje= "Archivo buscado: %r" %request.GET["prd"]
    else:
        mensaje="No has ingresado nada"

    return HttpResponse(mensaje)

def buscarfecha(request):
    mensaje= "NO hay nada"
    if request.POST["prd"]:
        archivo=request.POST["prd"]
        tipo = type(archivo)
        fecha_dt = datetime.datetime.strptime(archivo,"%Y-%m-%d").date()
        #fecha_dt = datetime.strptime(archivo,'%Y-%m-%d')
        tipo = type(fecha_dt)
        print (tipo, fecha_dt)
        
        #if type(tipo) is datetime.date:
        #if 'datetime.date' in str(type(tipo)):
            
        #    mensaje = "Estoy validando dato"
        
        #mensaje=datetime.datetime.now()
        
        #f (archivo)<>null:
        #    mensaje="Fecha no valida"
        #else:
        #    print(archivo)
        registro=registroarchivos.objects.filter(fechaingreso__range=(fecha_dt,fecha_dt))
        return render(request, "resultado_busqueda.html", {"registro":registro, "query":archivo})
        #   mensaje= "Archivo buscado: %r" %request.GET["prd"]
        #else:
        #    mensaje = "No es valido"
    else:
        mensaje="No has ingresado nada"

    return HttpResponse(mensaje)


class ResumenFoundationView(TemplateView):
    template_name= 'resumefoundation.html'

class addregister(CreateView):
    """ vista para registrar nuevo registro """
    template_name = 'addregister.html'
    model = registroarchivos
    #fields = ['fechaingreso','guianro', 'usuario', 'descripcion', 'oficio', 'fechaentrega', 'enviadoa', 'observacion']
    fields = ('__all__')
    success_url = '/'
    ## reverse_lazy('persona_app:correcto')
    ## persona_app es el nombre que se le pone en en la ruta y correcto es el name de la ruta
    ## en las urls.py se app_name = "persona_app" eso nos indica todas las rutas
    ## path('success/', views.SuccessView.as_view()), name= 'correcto')
    ## reverse_lazy nos permite redireccionar. y mas cosas

    #def form_valid(self, form):
    #    registro = form.save() 
        ## registro = form.save(commit=false)
        ##registro.fullname = registro.name + ' ' + registro.lastname
        ##registro.save() esto actualiza la informacion
    #    return super(addregister, self).form_valid(form)



    
class registroarchivoListView(ListView):
    #model = registroarchivos
    template_name = "lista.html"
    context_object_name = 'listaNumeros'
    paginate_by = 10
    ordering = 'fechaingreso'
    

    #queryset = ['0', '10', '30', '50']

    def get_queryset(self):
    # Escribo el codigo
        usuarios = self.request.GET.get("nombre", '')
        listaNumeros = registroarchivos.objects.filter(Q(usuario__icontains=usuarios) | Q(guianro__icontains=usuarios))
        return listaNumeros
        
class ListaRegistroUsuario(ListView):
    template_name = 'listae.html'
   #queryset= registroarchivos.objects.filter(usuario='SAFETY')

    def get_queryset(self):
        # Escribo el codigo
        usuarios = self.kwargs['nombre']
        listaNumeros = registroarchivos.objects.filter(usuario__icontains=usuarios) 
        return listaNumeros

class ListTramitebyUsuario(ListView):
    #template_name = 'listaxusuario.html' 
    template_name = 'listae.html'
    context_object_name = 'listaNumeros'
    paginate_by = 25
    def get_queryset (self):
        print('*****************')
        palabra_clave = self.request.GET.get("kword", '')
        print('========', palabra_clave)
        listaNumeros = registroarchivos.objects.filter(usuario__icontains=palabra_clave)
        print('lista resultado', listaNumeros)
        return listaNumeros

class SuccessView(TemplateView):
    template_name = "success.html"

class registroarchivosupdate(UpdateView):
    template_name="actualiza.html"
    model= registroarchivos
    fields = ('__all__')
    success_url = reverse_lazy('correcto')

class borrarregistro(DeleteView):
    template_name="borrado.html"
    model= registroarchivos
    success_url = reverse_lazy('correcto')


class Registrar_Tramite(CreateView):
    template_name="addregistro.html"
    model = registroarchivos
    form_class = PruebaForm
    success_url = reverse_lazy('correcto')

class NewRegistro(FormView):
    template_name= 'nuevoregistro.html'
    form_class = RegistroForm
    success_url = '/'

    def form_valid(self, form):
        fechai = form.cleaned_data['fechaingreso']
        guianro = form.cleaned_data['guianro']
        return super(NewRegistro,self).form_valid(form)

class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = 'home.html'
    