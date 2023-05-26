from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo=models.CharField(max_length=50,verbose_name="Titulo")
    contenido=models.CharField(max_length=500,verbose_name="Contenido")
    imagen=models.ImageField(verbose_name="Imagen",upload_to='productos' )
    created=models.DateTimeField(auto_now_add=True,verbose_name="Contenido")
    updated=models.DateTimeField(auto_now_add=True,verbose_name="Contenido")

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    
    def __str__(self):
        return self.titulo