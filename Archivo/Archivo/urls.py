"""Archivo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from gestionarchivo import views
urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('admin/', admin.site.urls),
    path('busqueda_archivos/', views.busqueda_archivos),
    path('busqueda_fecha/', views.busqueda_archivosf),
    path('buscar/', views.buscar),
    path('buscarfecha/',views.buscarfecha),
    path('registro/add',views.addregister.as_view(), name='registro_add'), 
    path('listado/',views.registroarchivoListView.as_view(),name='listado'), 
    path('listadoexternos/<nombre>/', views.ListaRegistroUsuario.as_view(),),
    path('busqueda_usuario/', views.ListTramitebyUsuario.as_view(),),
    path('actualizar/<pk>/', views.registroarchivosupdate.as_view(),name='modificar_registro'),
    path('success/', views.SuccessView.as_view(),name='correcto'),
    path('borrar/<pk>/', views.borrarregistro.as_view(),name='borrar_registro'),
    path('registronuevo/',views.Registrar_Tramite.as_view(), name='nuevo_registro'),
    path('nuevoregistro/',views.NewRegistro.as_view(), name='registronuevo'),
    path('resume_foundation/',views.ResumenFoundationView.as_view(), name='ResumenFoundation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
