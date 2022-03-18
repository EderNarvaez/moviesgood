from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,  verbose_name='Título')
    image = models.ImageField(
        upload_to='images/', verbose_name='Imagen', null=True)
    description = models.TextField(null=True, verbose_name='Descripción')

    def __str__(self):
        fila = "Título: " + self.title + " - " + "Descripción: " + self.description
        return fila
# Este codigo permite borrar los archivos fisicos de las imagenes, revisar por quie no funciona

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
