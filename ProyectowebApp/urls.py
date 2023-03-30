from django.urls import path

from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"),
    path('productos',views.productos, name="Productos"),
    path('tienda',views.tienda, name="Tienda"),
    path('acerca',views.acerca, name="Acerca"),
    path('contacto',views.contacto, name="Contacto"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)