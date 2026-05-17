from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    
    # NUEVO CAMPO: Guarda el enlace directo de la imagen de Cloudinary
    imagen = models.URLField(blank=True, null=True)

    # Campos de macros que ya tienes guardados abajo...
    calorias = models.CharField(max_length=50, blank=True, null=True)
    proteinas = models.CharField(max_length=50, blank=True, null=True)
    carbohidratos = models.CharField(max_length=50, blank=True, null=True)
    azucares = models.CharField(max_length=50, blank=True, null=True)
    sodio = models.CharField(max_length=50, blank=True, null=True)
    vitaminas = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo