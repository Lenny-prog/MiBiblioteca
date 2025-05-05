from django.db import models
from django.conf import settings

 
# Create your models here.
 
class Libro(models.Model):
    ESTADOS = [
        ('PR', 'Por leer'),
        ('LE', 'Leyendo'),
        ('LD', 'Leído'),
    ]
 
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='PR')
    resena = models.TextField(blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

 
    def __str__(self):
        return self.titulo
 