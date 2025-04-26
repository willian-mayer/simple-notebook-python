from django.db import models

class Cuaderno(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Hoja(models.Model):
    cuaderno = models.ForeignKey(Cuaderno, related_name='hojas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Contenido(models.Model):
    hoja = models.ForeignKey(Hoja, related_name='contenidos', on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f"Contenido de {self.hoja.titulo}"
