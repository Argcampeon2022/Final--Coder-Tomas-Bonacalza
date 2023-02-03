from django.db import models

class Usuario(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    contraseña= models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - E-Mail: {self.email} - Contraseña: {self.contraseña}"